from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, JSON, func 
from sqlalchemy.orm import backref, relationship

from mySqlalchemy.database import Base 

class Project(Base):
    __tablename__ = 'project'
    project_name = Column(String, primary_key=True)
    author_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    upated_at = Column(DateTime, default=func.now())
    description = Column(String, nullable=True)
    
class TrainExperiment(Base):
    __tablename__ = 'train_experiment'
    experiment_index = Column(Integer, primary_key=True)
    project_name = Column(String, ForeignKey("project.project_name"))
    project = relationship(Project, backref=backref('project', uselist=True, cascade='delete,all'))

class TrainLog(Base):
    __tablename__ = 'train_log'
    epoch = Column(Integer, primary_key=True)
    log = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=func.now())
    description = Column(String, nullable=True)
    # project_name = Column(String, ForeignKey("project.project_name"))
    # project = relationship(Project, backref=backref('project', uselist=True, cascade='delete,all'))
    experiment_index = Column(Integer, ForeignKey("train_experiment.experiment_index"))
    experiment = relationship(TrainExperiment, backref=backref('experiment', uselist=True, cascade='delete,all'))
