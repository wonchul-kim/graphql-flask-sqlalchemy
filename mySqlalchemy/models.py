import sqlalchemy
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, JSON, func, TIMESTAMP, Table
from sqlalchemy.orm import relationship

from mySqlalchemy.database import Base 

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    description = Column(String, nullable=True)

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    description = Column(String, nullable=True)

    ### User
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    user = relationship("User", backref=sqlalchemy.orm.backref("projects", cascade="all,delete"))
    
class TrainExperiment(Base):
    __tablename__ = 'train_experiment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dataset_info = Column(JSON, nullable=False)
    parameters = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    description = Column(String, nullable=True)
    
    ### User
    user_id = Column(String, ForeignKey("user.id", ondelete="CASCADE"))
    user = relationship("User", backref=sqlalchemy.orm.backref("train_experiments", cascade="all,delete"))
    
    ### Project
    project_id = Column(Integer, ForeignKey("project.id", ondelete="CASCADE"))
    project = relationship("Project", backref=sqlalchemy.orm.backref("train_experiments", cascade="all,delete"))
    
class TrainLog(Base):
    __tablename__ = 'train_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    log = Column(JSON, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    accessed_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
    
    ### TrainExperiment
    train_experiment_id = Column(Integer, ForeignKey('train_experiment.id', ondelete="CASCADE"))
    train_experiment = relationship("TrainExperiment", backref=sqlalchemy.orm.backref("train_logs", cascade="all,delete"))

class ServerStatus(Base):
    __tablename__ = 'server_status'
    server_name = Column(String, primary_key=True)
    server_status = Column(String, nullable=False)
    server_info = Column(JSON, nullable=True)
    
    user_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.current_timestamp())
