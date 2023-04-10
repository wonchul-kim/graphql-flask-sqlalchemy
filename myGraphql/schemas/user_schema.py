from mySqlalchemy.models import User
from mySqlalchemy.database import db_session
import graphene 
from graphene import relay 
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserSQL(SQLAlchemyObjectType):
    class Meta:
        model = User 
        interfaces = (relay.Node,)
