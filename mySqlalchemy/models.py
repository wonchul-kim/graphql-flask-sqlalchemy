from codecs import backslashreplace_errors
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, JSON, func, TIMESTAMP
from sqlalchemy.orm import backref, relationship

from mySqlalchemy.database import Base 

class Project(Base):
    __tablename__ = 'project'
    project_name = Column(String, primary_key=True, unique=True)
    author_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    upated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    description = Column(String, nullable=True)
    
    experiment_indexes = relationship("TrainExperiment", backref="project")  
    train_logs = relationship("TrainLog", backref="project")  

class TrainExperiment(Base):
    __tablename__ = 'train_experiment'
    experiment_index = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    dataset_info = Column(JSON, nullable=False)
    parameters = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=func.now())

    project_name = Column(String, ForeignKey("project.project_name"))
    train_logs = relationship("TrainLog", backref="train_experiment")

class TrainLog(Base):
    __tablename__ = 'train_log'
    epoch = Column(Integer, primary_key=True)
    log = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=func.now())
    description = Column(String, nullable=True)

    project_name = Column(String, ForeignKey("project.project_name"))
    experiment_index = Column(String, ForeignKey("train_experiment.experiment_index"))

class ServerStatus(Base):
    __tablename__ = 'server_status'
    server_name = Column(String, primary_key=True)
    server_status = Column(String, nullable=False)
    server_info = Column(JSON, nullable=True)
    user_name = Column(String, nullable=True)
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    
    
    

