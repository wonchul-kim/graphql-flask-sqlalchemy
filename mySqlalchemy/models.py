from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, JSON, func, TIMESTAMP, Table
from sqlalchemy.orm import relationship

from mySqlalchemy.database import Base 

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    
    projects = relationship("Project", backref="user", cascade="all, delete-orphan")
    train_experiments = relationship("TrainExperiment", backref="user", cascade='all, delete-orphan')

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    description = Column(String, nullable=True)

    user_name = Column(String, ForeignKey("user.user_name"))
    train_experiments = relationship("TrainExperiment", backref="project", cascade='all, delete-orphan')

class TrainExperiment(Base):
    __tablename__ = 'train_experiment'
    experiment_index = Column(Integer, primary_key=True, autoincrement=True)
    dataset_info = Column(JSON, nullable=False)
    parameters = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())

    user_name = Column(String, ForeignKey("user.user_name"))
    project_name = Column(String, ForeignKey("project.project_name"))
    train_logs = relationship("TrainLog", backref="train_experiment", cascade="all, delete-orphan")
    
class TrainLog(Base):
    __tablename__ = 'train_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    log = Column(JSON, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    
    experiment_index = Column(Integer, ForeignKey('train_experiment.experiment_index'))

class ServerStatus(Base):
    __tablename__ = 'server_status'
    server_name = Column(String, primary_key=True)
    server_status = Column(String, nullable=False)
    server_info = Column(JSON, nullable=True)
    
    user_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())

    
    
    

