from mySqlalchemy.models import User, Project, TrainExperiment, TrainLog
from mySqlalchemy.database import db_session
import graphene 
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from sqlalchemy import and_

from .schemas.user_schema import UserSQL, CreateUser, DeleteUser
from .schemas.project_schema import ProjectSQL, CreateProject
from .schemas.train_experiment_schema import TrainExperimentSQL, CreateTrainExperiment
from .schemas.train_log_schema import TrainLogSQL, CreateTrainLog

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    
    ### for user ###########################################################################################
    all_users = SQLAlchemyConnectionField(
        UserSQL.connection#, sort=UserSQL.sort_argument() # allow only single column sorting
    )

    find_user = graphene.Field(UserSQL, user_name=graphene.String())
    def resolve_find_user(root, info, **kwargs):
        query = UserSQL.get_query(info)
        user_name = kwargs.get('user_name')
        
        query = query.filter(User.user_name==user_name)
        objs = query.first()
        
        return objs
    
    ### For project ######################################################################################
    all_projects = SQLAlchemyConnectionField(
        ProjectSQL.connection#, sort=UserSQL.sort_argument() # allow only single column sorting
    )

    find_project = graphene.Field(ProjectSQL, user_name=graphene.String(), project_name=graphene.String())
    def resolve_find_project(root, info, **kwargs):
        query = ProjectSQL.get_query(info)
        
        # you can also use and_ with filter() eg: filter(and_(param1, param2)).first()
        if 'project_name' in kwargs.keys():
            project_name = kwargs.get('project_name')
            query = query.filter(Project.project_name==project_name)
        if 'user_name' in kwargs.keys():
            user_name = kwargs.get("user_name")
            user_db = db_session.query(User).filter_by(user_name=user_name).first()
            query = query.filter(Project.user==user_db)
        objs = query.first()
        
        return objs
        
    ### For exeriment ######################################################################################
    all_train_experiments = SQLAlchemyConnectionField(
        TrainExperimentSQL.connection#, sort=TrainExperimentSQL.sort_argument()
    )
    
    find_train_experiment = graphene.Field(TrainExperimentSQL, user_name=graphene.String(), project_name=graphene.String(), experiment=graphene.Int())
    def resolve_find_train_experiment(root, info, **kwargs):
        query = TrainExperimentSQL.get_query(info)
        
        if 'experiment' in kwargs.keys():
            experiment = kwargs.get('experiment')
            query = query.filter(TrainExperiment.id==experiment)
        if 'project_name' in kwargs.keys():
            project_name = kwargs.get("project_name")
            project_db = db_session.query(Project).filter_by(project_name=project_name).first()
            query = query.filter(TrainExperiment.project==project_db)
        if 'user_name' in kwargs.keys():
            user_name = kwargs.get("user_name")
            user_db = db_session.query(User).filter_by(user_name=user_name).first()
            query = query.filter(TrainExperiment.user==user_db)
        objs = query.first()
        
        return objs
        
    ### For log ######################################################################################
    all_train_logs = SQLAlchemyConnectionField(
        TrainLogSQL.connection
    )
    
    # find_train_log = graphene.Field(TrainLogSQL, project=graphene.String(), experiment=graphene.Int())
    # def resolve_find_train_log(root, info, **kwargs):
    #     query = TrainLogSQL.get_query(info)
    #     project_name = kwargs.get('project_name')
    #     experiment_index = kwargs.get("experiment_index")
        
    #     query = query.filter(TrainLog.project_name==project_name)
    #     query = query.filter(TrainLog.experiment_index==experiment_index)
    #     objs = query.all()
        
    #     return objs
    
    # ### disable sorting over this field 
    # all_train_logs = SQLAlchemyConnectionField(
    #     TrainLogSQL.connection, sort=None
    # )
    
class myMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    create_project = CreateProject.Field()
    create_train_experiment = CreateTrainExperiment.Field()
    create_train_log = CreateTrainLog.Field()
    
    
schema = graphene.Schema(query=Query, mutation=myMutation, types=[UserSQL, ProjectSQL, TrainExperimentSQL, TrainLogSQL])