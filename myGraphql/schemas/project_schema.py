from mySqlalchemy.models import Project, User
from mySqlalchemy.database import db_session
import graphene 
from graphene_sqlalchemy import SQLAlchemyObjectType

class ProjectSQL(SQLAlchemyObjectType):
    class Meta:
        model = Project 
        interfaces = (graphene.relay.Node,)

class CreateProject(graphene.Mutation):
    class Arguments:
        project_name = graphene.String(required=True)
        user_name = graphene.String(required=True)
        description = graphene.String(required=False)

    done = graphene.Boolean()
    verbose = graphene.String()
    project = graphene.Field(ProjectSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        project_name = kwargs.get("project_name")
        user_name = kwargs.get('user_name')
        description=kwargs.get('description')
        
        user_db = db_session.query(User).filter_by(user_name=user_name).first()
        project_db = db_session.query(Project).filter_by(user_id=user_db.id, project_name=project_name).first()
        
        if not project_db: 
            project_db = Project(project_name=project_name, description=description)
            user_db.projects.append(project_db)
            project_db.user = user_db
            db_session.add(project_db)
            db_session.commit()
            done = True 
            verbose = "Successfully done"
        else:
            done = False 
            verbose = "That pair of user({}) and project({}) is already exists".format(user_name, project_name)
            
        return CreateProject(done=done, verbose=verbose)
    
class DeleteProject(graphene.Mutation):
    class Arguments:
        project_name = graphene.String(required=True)

    done = graphene.Boolean()
    verbose = graphene.String()
    project = graphene.Field(ProjectSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        if 'project_name' in kwargs.keys():
            project_name = kwargs.get("project_name")

            if db_session.query(Project).filter_by(project_name=project_name).first():
                db_session.query(Project).filter_by(project_name=project_name).delete()
                db_session.commit()
                done = True 
                verbose = "Successfully done"
            else:
                done = False 
                verbose = "There is no such project-name"
        else:
            done = False 
            verbose = "A project-name must be provided"
            
        return DeleteProject(done=done, verbose=verbose)
    
class UpdateProject(graphene.Mutation):
    class Arguments:
        project_name = graphene.String(required=True)
        new_project_name = graphene.String(required=True)

    done = graphene.Boolean()
    verbose = graphene.String()
    project = graphene.Field(ProjectSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        if 'project_name' in kwargs.keys() and 'new_project_name' in kwargs.keys():
            project_name = kwargs.get("project_name")
            new_project_name = kwargs.get('new_project_name')
            
            print(">>>>> ", project_name, new_project_name)
            
            try: 
                db_session.query(Project).filter_by(project_name=project_name).first().project_name = new_project_name
                db_session.commit()
                done = True 
                verbose = "Successfully done"
            except:
                done = False 
                verbose = "There is no such project-name"
        else:
            done = False 
            verbose = "Project-name and new project-name must be provided"
            
        return UpdateProject(done=done, verbose=verbose)