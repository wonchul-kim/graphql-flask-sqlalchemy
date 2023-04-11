from ast import Expression
from mySqlalchemy.models import TrainExperiment, TrainLog
from mySqlalchemy.database import db_session
import graphene 
from graphene import relay 
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from sqlalchemy import and_

class TrainLogSQL(SQLAlchemyObjectType):
    class Meta:
        model = TrainLog 
        interfaces = (relay.Node,)
        
class CreateTrainLog(graphene.Mutation):
    class Arguments:
        train_experiment_id = graphene.Int()
        log = graphene.types.json.JSONString()
        
    done = graphene.Boolean()
    train_log = graphene.Field(TrainLogSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        train_log_db = TrainLog(project_name=kwargs.get('project_name'), description=kwargs.get('description'))
        db_session.add(train_log_db)
        if 'train_experiment_id' in kwargs.keys():
            train_log_db.train_experiment_id = db_session.qeury(TrainExperiment).filter_by(id=kwargs.get('train_experiment_id')).first()
        db_session.commit()
        done = True 
        
        return CreateTrainLog(train_log=train_log_db, done=done)
        