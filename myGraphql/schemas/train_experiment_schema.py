from typing_extensions import Required
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
        dataset_info = graphene.types.json.JSONString(required=True)
        parameters = graphene.types.json.JSONString(required=True)
        user_name = graphene.String(required=True)
        project_name = graphene.String(required=True)
        description = graphene.String(required=False)
        
    experiment_id = graphene.Int()
    done = graphene.Boolean()
    verbose = graphene.String()
    train_experiment = graphene.Field(TrainExperimentSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        project_name = kwargs.get("project_name")
        user_name = kwargs.get('user_name')
        dataset_info=kwargs.get('dataset_info')
        parameters=kwargs.get('parameters')
        description=kwargs.get('description')
        
        user_db = db_session.query(User).filter_by(user_name=user_name).first()
        project_db = db_session.query(Project).filter_by(user_id=user_db.id, project_name=project_name).first()
        
        train_experiment_db = TrainExperiment(project_id=project_db.id, dataset_info=dataset_info, \
                                                parameters=parameters, description=description)
    
        project_db.train_experiments.append(train_experiment_db)
        train_experiment_db.project = project_db
        db_session.add(train_experiment_db)
        db_session.commit()
        db_session.refresh(train_experiment_db)
        done = True 
        verbose = "Seccessfully done"
        
        return CreateTrainExperiment(done=done, verbose=verbose, experiment_id=train_experiment_db.id)
