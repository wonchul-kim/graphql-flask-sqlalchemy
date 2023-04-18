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
        user_name = graphene.String(required=False)
        project_name = graphene.String(required=False)
        
    done = graphene.Boolean()
    verbose = graphene.String()
    train_experiment = graphene.Field(TrainExperimentSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        if "dataset_info" in kwargs.keys() and "parameters" in kwargs.keys():
            train_experiment_db = TrainExperiment(dataset_info=kwargs.get('dataset_info'), parameters=kwargs.get('parameters'), \
                                                    description=kwargs.get('description'))
            if 'user_name' in kwargs.keys():
                user_db = db_session.query(User).filter_by(user_name=kwargs.get("user_name")).first()
                user_db.train_experiments.append(train_experiment_db)
                train_experiment_db.user = user_db
            if 'project_name' in kwargs.keys():
                project_db = db_session.query(Project).filter_by(project_name=kwargs.get('project_name')).first()
                project_db.train_experiments.append(train_experiment_db)
                train_experiment_db.project = project_db
            db_session.add(train_experiment_db)
            db_session.commit()
            done = True 
            verbose = "Seccessfully done"
        else:
            done = False 
            verbose = "Dataset_info and parameters must be provided "
        
        return CreateTrainExperiment(done=done, verbose=verbose)
        
        