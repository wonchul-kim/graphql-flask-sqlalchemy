from mySqlalchemy.database import engine, Base, db_session
from mySqlalchemy.models import Project, TrainExperiment, TrainLog

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def save_project_db(project_name):
    ##FIXME: check if the project name already exists
    project_db = Project(project_name=project_name)
    db_session.add(project_db)
    db_session.commit()
    
    return project_db
    
def save_experiment_db(project_db, dataset_info, parameters):
    experiment_db = TrainExperiment(project=project_db, dataset_info=dataset_info, parameters=parameters)
    db_session.add(experiment_db)
    db_session.commit()
    
    return experiment_db

def save_log_db(experiment_db, epoch, log):
    log_db = TrainLog(experiment=experiment_db, epoch=epoch, log=log)
    db_session.add(log_db)
    db_session.commit()
    
    return log_db
    
def make_fake_db():
    ### create the fixtures 
    interojo_db = save_project_db('interojo')
    central_db = save_project_db('central')
    
    interojo_experiment_db_1 = save_experiment_db(interojo_db, {"datasets": "interojo_ver2", "input_dir": 'abcdefghi'}, {"a": 1, "b": 2, "c": "abc"})
    interojo_experiment_db_2 = save_experiment_db(interojo_db, {"datasets": "interojo_ver22", "input_dir": 'ii'}, {"a": 100, "b": 20, "c": "abc"})

    save_log_db(interojo_experiment_db_1, 0, {"epoch": 0, "train_loss": 0.3, "val_loss": 0.2, "lr": 0.01})
    save_log_db(interojo_experiment_db_1, 1, {"epoch": 1, "train_loss": 0.2, "val_loss": 0.1, "lr": 0.001})
    
def filter_by_project(project_name):
    return Project.query.filter_by(project_name=project_name)
    