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
        log = graphene.types.json.JSONString(required=True)
        
    done = graphene.Boolean()
    verbose = graphene.String()
    train_log = graphene.Field(TrainLogSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        if "log" in kwargs.keys():
            train_log_db = TrainLog(log=kwargs.get("log"))
            if 'train_experiment_id' in kwargs.keys():
                train_experiment_db = db_session.qeury(TrainExperiment).filter_by(id=kwargs.get('train_experiment_id')).first()
                train_experiment_db.train_logs.append(train_log_db)
                train_log_db.train_experiment = train_experiment_db
            db_session.add(train_log_db)
            db_session.commit()
            done = True 
            verbose = "Sueccessfully done"
        else:
            done = False 
            verbose = "A log must be provided"
        
        return CreateTrainLog(done=done, verbose=verbose)
        