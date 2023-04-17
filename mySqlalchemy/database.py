from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker 

# engine = create_engine('sqlite:///database.sqlite3')#, convert_unicode=True)
engine = create_engine('postgresql://aiv:aiv11011@192.168.11.177/aivdl')

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

