from ast import Expression
from myDB.mySqlalchemy.models import User, Project, TrainExperiment, TrainLog
from myDB.mySqlalchemy.database import db_session
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
        user_name = graphene.String(required=True)
        project_name = graphene.String(required=True)
        log = graphene.types.json.JSONString(required=True)
        
    done = graphene.Boolean()
    verbose = graphene.String()
    train_log = graphene.Field(TrainLogSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        project_name = kwargs.get("project_name")
        user_name = kwargs.get('user_name')
        
        user_db = db_session.query(User).filter_by(user_name=user_name).first()
        project_db = db_session.query(Project).filter_by(user_id=user_db.id, project_name=project_name).first()
        train_experiment_db = db_session.query(TrainExperiment).filter_by(project_id=project_db.id).order_by(TrainExperiment.id.desc()).first()
        
        train_log_db = TrainLog(log=kwargs.get("log"))
        train_experiment_db.train_logs.append(train_log_db)
        train_log_db.train_experiment = train_experiment_db
        db_session.add(train_log_db)
        db_session.commit()
        done = True 
        verbose = "Sueccessfully done"
        
        return CreateTrainLog(done=done, verbose=verbose)
        
