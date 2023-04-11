from mySqlalchemy.models import User, Project, TrainExperiment
from mySqlalchemy.database import db_session
import graphene 
from graphene import relay 
from graphene_sqlalchemy import SQLAlchemyObjectType

class TrainExperimentSQL(SQLAlchemyObjectType):
    class Meta:
        model = TrainExperiment
        interfaces = (relay.Node,)
        
class CreateTrainExperiment(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=False)
        project_name = graphene.String(required=False)
        dataset_info = graphene.types.json.JSONString(required=True)
        parameters = graphene.types.json.JSONString(required=True)
        
    done = graphene.Boolean()
    train_experiment = graphene.Field(TrainExperimentSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        train_experiment_db = TrainExperiment(project_name=kwargs.get('project_name'), description=kwargs.get('description'))
        db_session.add(train_experiment_db)
        if 'user_name' in kwargs.keys():
            user_db = db_session.query(User).filter_by(user_name=kwargs.get("user_name")).first()
            train_experiment_db.user = user_db
        if 'project_name' in kwargs.keys():
            train_experiment_db.project = db_session.qeury(Project).filter_by(project_name=kwargs.get('project_name')).first()
        db_session.commit()
        done = True 
        
        return CreateTrainExperiment(train_experiment=train_experiment_db, done=done)
        