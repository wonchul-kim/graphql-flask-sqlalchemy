from mySqlalchemy.database import engine, Base, db_session
from mySqlalchemy.models import Project, TrainExperiment, TrainLog

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def save_project_db(project_name, author_name, description):
    ##FIXME: check if the project name already exists
    project_db = Project(project_name=project_name, author_name=author_name, description=description)
    db_session.add(project_db)
    db_session.commit()
    
    return project_db
    
def save_experiment_db(project_name, dataset_info, parameters):
    experiment_db = TrainExperiment(project_name=project_name, dataset_info=dataset_info, parameters=parameters)
    db_session.add(experiment_db)
    db_session.commit()
    
    return experiment_db

def save_log_db(project_name, experiment_index, log):
    log_db = TrainLog(project_name=project_name, experiment_index=experiment_index, log=log)
    db_session.add(log_db)
    db_session.commit()
    
    return log_db
    
def make_fake_db():
    ### create the fixtures 
    save_project_db('interojo', 'wonchul1', 'abc')
    save_project_db('central', 'wonchul2', 'edf')
    
    save_experiment_db('interojo', {"datasets": "interojo_ver1", "input_dir": 'a'}, {"a": 1, "b": 2, "c": "a"})
    save_experiment_db('interojo', {"datasets": "interojo_ver2", "input_dir": 'b'}, {"a": 10, "b": 20, "c": "b"})
    save_experiment_db('interojo', {"datasets": "interojo_ver3", "input_dir": 'c'}, {"a": 100, "b": 200, "c": "c"})
    save_experiment_db('interojo', {"datasets": "central_ver1", "input_dir": 'i'}, {"a": 1, "b": 2, "c": "a"})
    save_experiment_db('interojo', {"datasets": "central_ver2", "input_dir": 'j'}, {"a": 10, "b": 20, "c": "b"})

    save_log_db('interojo', 0, {"epoch": 0, "train_loss": 0.3, "val_loss": 0.2, "lr": 0.01})
    save_log_db('interojo', 0, {"epoch": 1, "train_loss": 0.2, "val_loss": 0.1, "lr": 0.001})
    save_log_db('interojo', 0, {"epoch": 2, "train_loss": 0.1, "val_loss": 0.05, "lr": 0.0005})
    save_log_db('interojo', 2, {"epoch": 0, "train_loss": 10, "val_loss": 10, "lr": 0.1})
    save_log_db("interojo", 1, {"epoch": 1, "train_loss": 5, "val_loss": 5, "lr": 0.01})
    save_log_db("central", 0, {"epoch": 0, "train_loss": 100, "val_loss": 100, "lr": 10})
        
def filter_by_project(project_name):
    return Project.query.filter_by(project_name=project_name)
    