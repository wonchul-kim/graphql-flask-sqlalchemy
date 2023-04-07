from mySqlalchemy.models import Project, TrainExperiment, TrainLog

import graphene 
from graphene import relay 
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from sqlalchemy import and_

class ProjectSQL(SQLAlchemyObjectType):
    class Meta:
        model = Project 
        interfaces = (relay.Node,)

# class CreateProject(graphene.Mutation):
#     class Arguments:
#         project_name = graphene.String()
#         author_name = graphene.String()
    

class TrainExperimentSQL(SQLAlchemyObjectType):
    class Meta:
        model = TrainExperiment
        interfaces = (relay.Node,)
        
class TrainLogSQL(SQLAlchemyObjectType):
    class Meta:
        model = TrainLog 
        interfaces = (relay.Node,)
        
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    
    # ### allow only single column sorting 
    # all_projects = SQLAlchemyConnectionField(
    #     ProjectSQL.connection, sort=ProjectSQL.sort_argument()
    # )

    ### allow sorting over multiple columns, by default over the primary key
    project = SQLAlchemyConnectionField(ProjectSQL)
    find_project = graphene.Field(ProjectSQL, project_name=graphene.String())
    all_projects = SQLAlchemyConnectionField(
        ProjectSQL.connection
    )

    def resolve_find_project(root, info, **args):
        query = ProjectSQL.get_query(info)
        project_name = args.get('project_name')
        
        # you can also use and_ with filter() eg: filter(and_(param1, param2)).first()
        return query.filter(Project.project_name==project_name).first()
    
    
    all_train_experiments = SQLAlchemyConnectionField(
        TrainExperimentSQL.connection
    )
    all_train_logs = SQLAlchemyConnectionField(
        TrainLogSQL.connection
    )
    
    # ### disable sorting over this field 
    # all_train_logs = SQLAlchemyConnectionField(
    #     TrainLogSQL.connection, sort=None
    # )
    
    
schema = graphene.Schema(query=Query)