from mySqlalchemy.models import Project, TrainExperiment, TrainLog

import graphene 
from graphene import relay 
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

class ProjectQuery(SQLAlchemyObjectType):
    class Meta:
        model = Project 
        interfaces = (relay.Node,)

class TrainExperimentQuery(SQLAlchemyObjectType):
    class Meta:
        model = TrainExperiment
        interfaces = (relay.Node,)
        
class TrainLogQuery(SQLAlchemyObjectType):
    class Meta:
        model = TrainLog 
        interfaces = (relay.Node,)
        
        
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    
    # ### allow only single column sorting 
    # all_projects = SQLAlchemyConnectionField(
    #     ProjectQuery.connection, sort=ProjectQuery.sort_argument()
    # )

    ### allow sorting over multiple columns, by default over the primary key
    all_projects = SQLAlchemyConnectionField(
        ProjectQuery.connection
    )
    all_train_experiments = SQLAlchemyConnectionField(
        TrainExperimentQuery.connection
    )
    all_train_logs = SQLAlchemyConnectionField(
        TrainLogQuery.connection
    )
    
    # ### disable sorting over this field 
    # all_train_logs = SQLAlchemyConnectionField(
    #     TrainLogQuery.connection, sort=None
    # )
    
    
schema = graphene.Schema(query=Query)