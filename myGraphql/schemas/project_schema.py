from mySqlalchemy.models import Project, User
from mySqlalchemy.database import db_session
import graphene 
from graphene import relay 
from graphene_sqlalchemy import SQLAlchemyObjectType

class ProjectSQL(SQLAlchemyObjectType):
    class Meta:
        model = Project 
        interfaces = (relay.Node,)

class CreateProject(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=False)
        project_name = graphene.String(required=True)
        description = graphene.String(required=False)

    done = graphene.Boolean()
    project = graphene.Field(ProjectSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        project_db = Project(project_name=kwargs.get('project_name'), description=kwargs.get('description'))
        db_session.add(project_db)
        if 'user_name' in kwargs.keys():
            user_db = db_session.query(User).filter_by(user_name=kwargs.get("user_name")).first()
            project_db.user = user_db
        db_session.commit()
        done = True 
        
        return CreateProject(project=project_db, done=done)
    