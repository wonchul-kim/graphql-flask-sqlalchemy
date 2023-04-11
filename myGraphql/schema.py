from mySqlalchemy.models import User, Project, TrainExperiment, TrainLog
from mySqlalchemy.database import db_session
import graphene 
from graphene import relay 
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from sqlalchemy import and_

from .schemas.user_schema import UserSQL, CreateUser
from .schemas.project_schema import ProjectSQL, CreateProject
from .schemas.train_experiment_schema import TrainExperimentSQL, CreateTrainExperiment
from .schemas.train_log_schema import TrainLogSQL, CreateTrainLog

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    
    # ### allow only single column sorting 
    # all_projects = SQLAlchemyConnectionField(
    #     ProjectSQL.connection, sort=ProjectSQL.sort_argument()
    # )

    ### for user ###########################################################################################
    find_user = graphene.Field(UserSQL, user_name=graphene.String())
    all_users = SQLAlchemyConnectionField(
        UserSQL.connection
    )

    def reolve_find_user(root, info, **kwargs):
        query = UserSQL.get_query(info)
        user_name = kwargs.get('user_name')
        
        query = query.filter(User.user_name==user_name)
        
        return query


    ### For project ######################################################################################
    find_project = graphene.Field(ProjectSQL, project_name=graphene.String())
    all_projects = SQLAlchemyConnectionField(
        ProjectSQL.connection
    )

    def resolve_find_project(root, info, **args):
        query = ProjectSQL.get_query(info)
        project_name = args.get('project_name')
        
        # you can also use and_ with filter() eg: filter(and_(param1, param2)).first()
        return query.filter(Project.project_name==project_name)
    
    # ### For exeriment ######################################################################################
    # find_train_experiment = graphene.Field(TrainExperimentSQL, experiment=graphene.Int())
    # all_train_experiments = SQLAlchemyConnectionField(
    #     TrainExperimentSQL.connection
    # )
    
    # def resolve_find_train_experiment(root, info, **args):
    #     query = TrainExperimentSQL.get_query(info)
    #     # project_name = args.get("project_name")
    #     experiment = args.get('experiment')
        
    #     # query = query.filter(TrainExperiment.project_name==project_name)
    #     query = query.filter(TrainExperiment.experiment==experiment)
    #     objs = query.first()
        
    #     return objs
        
        


    
    # ### For log ######################################################################################
    # find_train_log = graphene.Field(TrainLogSQL, project=graphene.String(), experiment=graphene.Int())
    # all_train_logs = SQLAlchemyConnectionField(
    #     TrainLogSQL.connection
    # )
    
    # # def resolve_find_train_log(root, info, **args):
    # #     query = TrainLogSQL.get_query(info)
    # #     project_name = args.get('project_name')
    # #     experiment_index = args.get("experiment_index")
        
    # #     query = query.filter(TrainLog.project_name==project_name)
    # #     query = query.filter(TrainLog.experiment_index==experiment_index)
    # #     objs = query.all()
        
    # #     return objs
    
    # # ### disable sorting over this field 
    # # all_train_logs = SQLAlchemyConnectionField(
    # #     TrainLogSQL.connection, sort=None
    # # )
    
class myMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_project = CreateProject.Field()
    create_train_experiment = CreateTrainExperiment.Field()
    create_train_log = CreateTrainLog.Field()
    
    
schema = graphene.Schema(query=Query, mutation=myMutation, types=[UserSQL, ProjectSQL, TrainExperimentSQL, TrainLogSQL])