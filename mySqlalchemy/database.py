from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker 

engine = create_engine('sqlite:///database.sqlite3')#, convert_unicode=True)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    '''
    import all modules here that might define models so that
    they will be registered properly on the metadata.  Otherwise
    you will have to import them first before calling init_db()
    '''
    from mySqlalchemy.models import Project, TrainExperiment, TrainLog

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    ### create the fixtures 
    interojo_project = Project(project_name='interojo')
    db_session.add(interojo_project)
    central_project = Project(project_name='central')
    db_session.add(central_project)
    
    
    interojo_train_exp_1 = TrainExperiment(project=interojo_project, experiment_index=1)
    db_session.add(interojo_train_exp_1)
    interojo_train_exp_2 = TrainExperiment(project=interojo_project, experiment_index=2)
    db_session.add(interojo_train_exp_2)


    # train_log_data = {"epoch": 0, "train_loss": 0.3, "val_loss": 0.2, "lr": 0.01}
    # interojo_train_log = TrainLog(project=interojo_project)
    epoch = 0
    interojo_train_log = TrainLog(experiment=interojo_train_exp_1, epoch=0, log='{"epoch": 0, "train_loss": 0.3, "val_loss": 0.2, "lr": 0.01}')
    db_session.add(interojo_train_log)
    interojo_train_log = TrainLog(experiment=interojo_train_exp_1, epoch=1, log='{"epoch": 1, "train_loss": 0.2, "val_loss": 0.1, "lr": 0.001}')
    db_session.add(interojo_train_log)
    
    db_session.commit()