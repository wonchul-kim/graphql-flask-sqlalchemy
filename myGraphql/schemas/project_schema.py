from mySqlalchemy.models import Project
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
        project_name = graphene.String()
        author_name = graphene.String()
        description = graphene.String()

    ok = graphene.Boolean()
    project = graphene.Field(ProjectSQL)
    
    @classmethod 
    def mutate(root, info, _, **args):
        project_db = Project(project_name=args.get('project_name'), author_name=args.get('author_name'), description=args.get('description'))
        db_session.add(project_db)
        db_session.commit()
        ok = True 
        
        return CreateProject(project=project_db, ok=ok)
    