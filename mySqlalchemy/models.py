from codecs import backslashreplace_errors
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, JSON, func, TIMESTAMP, Table
from sqlalchemy.orm import backref, relationship

from mySqlalchemy.database import Base 

class User(Base):
    __tablename__ = 'user'
    user_name = Column(String, primary_key=True, unique=True)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    
    projects = relationship("Project", back_populates='users')
        
class Project(Base):
    __tablename__ = 'project'
    project_name = Column(String, primary_key=True, unique=True)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    description = Column(String, nullable=True)
    
    user_name = Column(String, ForeignKey("user.user_name"))
    users = relationship("User", back_populates='projects')
    train_experiments = relationship("TrainExperiment", back_populates='projects')
    
class TrainExperiment(Base):
    __tablename__ = 'train_experiment'
    experiment_index = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    dataset_info = Column(JSON, nullable=False)
    parameters = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    
    user_name = Column(String, ForeignKey("user.user_name"))
    project_name = Column(String, ForeignKey("project.project_name"))
    projects = relationship("Project", back_populates='train_experiments')
    train_logs = relationship("TrainLog", back_populates='train_experiments')
    
class TrainLog(Base):
    __tablename__ = 'train_log'
    # epoch = Column(Integer, primary_key=True)
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    log = Column(JSON, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    
    user_name = Column(String, ForeignKey("user.user_name"))
    project_name = Column(String, ForeignKey("project.project_name"))
    experiment_index = Column(Integer, ForeignKey("train_experiment.experiment_index"))
    train_experiments = relationship("TrainExperiment", back_populates='train_logs')
    
class ServerStatus(Base):
    __tablename__ = 'server_status'
    server_name = Column(String, primary_key=True)
    server_status = Column(String, nullable=False)
    server_info = Column(JSON, nullable=True)
    user_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())

    
    
    

