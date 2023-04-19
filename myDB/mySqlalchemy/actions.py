from myDB.mySqlalchemy.database import engine, Base, db_session
from myDB.mySqlalchemy.models import User, Project, TrainExperiment, TrainLog

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def save_user_db(user_name):
    user_db = User(user_name=user_name)
    db_session.add(user_db)
    db_session.commit()
    
    return user_db
    
def save_project_db(project_name, description, user_db):
    project_db = Project(project_name=project_name, description=description)
    project_db.user = user_db 
    user_db.projects.append(project_db)
    db_session.add(project_db)
    db_session.commit()
    
    return project_db
    
def save_experiment_db(dataset_info, parameters, user_db, project_db):
    experiment_db = TrainExperiment(dataset_info=dataset_info, parameters=parameters)
    experiment_db.project = project_db
    experiment_db.user = user_db
    user_db.train_experiments.append(experiment_db)
    project_db.train_experiments.append(experiment_db)
    db_session.add(experiment_db)
    db_session.commit()
    
    return experiment_db

def save_log_db(log, experiment_db):
    log_db = TrainLog(log=log)
    db_session.add(log_db)
    experiment_db.train_logs.append(log_db)
    log_db.train_experiment = experiment_db
    db_session.commit()
    
    return log_db
    
def make_fake_db():
    ### create the fixtures 
    user_db1 = save_user_db("wonchul1")
    user_db2 = save_user_db("wonchul2")
    user_db3 = save_user_db("wonchul3")
    user_db4 = save_user_db("wonchul4")
    user_db5 = save_user_db("wonchul5")
    user_db6 = save_user_db("wonchul6")
    
    
    project_db1 = save_project_db('interojo', 'abc', user_db1)
    project_db2 = save_project_db('interojo', 'edf', user_db1)
    project_db3 = save_project_db("interojo", 'fds', user_db1)
    project_db4 = save_project_db("centeral", 'alfekjawelkfjawelkfjawlkefj', user_db2)
    project_db5 = save_project_db("central", 'aaaaaaaaaa', user_db2)
    project_db6 = save_project_db("interojo", 'alfekjawelkfjawelkfjawlkefj', user_db2)
    project_db7 = save_project_db("central", 'aaaaaaaaaa', user_db3)
    project_db8 = save_project_db("interojo", 'alfekjawelkfjawelkfjawlkefj', user_db4)
    project_db9 = save_project_db("central", 'aaaaaaaaaa', user_db5)
    project_db10 = save_project_db("interojo", 'aaaaaaaaaa', user_db5)
    project_db11 = save_project_db("samkee", 'aaaaaaaaaa', user_db5)
    
    
    experiment_db1 = save_experiment_db({"datasets": "interojo_ver1", "input_dir": 'a'}, {"a": 1, "b": 2, "c": "a"}, user_db1, project_db1)
    experiment_db2 = save_experiment_db({"datasets": "interojo_ver2", "input_dir": 'b'}, {"a": 10, "b": 20, "c": "b"}, user_db1, project_db1)
    experiment_db3 = save_experiment_db({"datasets": "interojo_ver3", "input_dir": 'c'}, {"a": 100, "b": 200, "c": "c"}, user_db1, project_db1)
    experiment_db4 = save_experiment_db({"datasets": "central_ver1", "input_dir": 'i'}, {"a": 1, "b": 2, "c": "a"}, user_db2, project_db2)
    experiment_db5 = save_experiment_db({"datasets": "central_ver2", "input_dir": 'j'}, {"a": 10, "b": 20, "c": "b"}, user_db2, project_db2)
    experiment_db6 = save_experiment_db({"datasets": "interojo_ver4", "input_dir": 'a'}, {"a": 1, "b": 2, "c": "a"}, user_db2, project_db1)
    experiment_db7 = save_experiment_db({"datasets": "interojo_ver5", "input_dir": 'b'}, {"a": 10, "b": 20, "c": "b"}, user_db3, project_db1)
    experiment_db8 = save_experiment_db({"datasets": "interojo_ver6", "input_dir": 'c'}, {"a": 100, "b": 200, "c": "c"}, user_db3, project_db1)
    experiment_db9 = save_experiment_db({"datasets": "samkee_ver1", "input_dir": 'i'}, {"a": 1, "b": 2, "c": "a"}, user_db3, project_db3)
    experiment_db10 = save_experiment_db({"datasets": "sakmee_ver2", "input_dir": 'j'}, {"a": 10, "b": 20, "c": "b"}, user_db3, project_db3)
    experiment_db11 = save_experiment_db({"datasets": "samkee_ver3", "input_dir": 'a'}, {"a": 1, "b": 2, "c": "a"}, user_db3, project_db3)
    experiment_db12 = save_experiment_db({"datasets": "interojo_ver7", "input_dir": 'b'}, {"a": 10, "b": 20, "c": "b"}, user_db4, project_db1)
    experiment_db13 = save_experiment_db({"datasets": "interojo_ver8", "input_dir": 'c'}, {"a": 100, "b": 200, "c": "c"}, user_db4, project_db1)
    experiment_db14 = save_experiment_db({"datasets": "central_ver3", "input_dir": 'i'}, {"a": 1, "b": 2, "c": "a"}, user_db4, project_db2)
    experiment_db15 = save_experiment_db({"datasets": "central_ver4", "input_dir": 'j'}, {"a": 10, "b": 20, "c": "b"}, user_db4, project_db2)
    
    save_log_db({"epoch": 0, "train_loss": 0.3, "val_loss": 0.2, "lr": 0.01}, experiment_db1)
    save_log_db({"epoch": 1, "train_loss": 0.2, "val_loss": 0.1, "lr": 0.001}, experiment_db1)
    save_log_db({"epoch": 2, "train_loss": 0.1, "val_loss": 0.05, "lr": 0.0005}, experiment_db1)
    save_log_db({"epoch": 0, "train_loss": 10, "val_loss": 10, "lr": 0.1}, experiment_db2)
    save_log_db({"epoch": 1, "train_loss": 5, "val_loss": 5, "lr": 0.01}, experiment_db2)
    save_log_db({"epoch": 0, "train_loss": 100, "val_loss": 100, "lr": 10}, experiment_db4)
        
def filter_by_project(project_name):
    return Project.query.filter_by(project_name=project_name)
    