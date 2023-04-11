from mySqlalchemy.models import User
from mySqlalchemy.database import db_session
import graphene 
from graphene import relay 
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserSQL(SQLAlchemyObjectType):
    class Meta:
        model = User 
        interfaces = (relay.Node,)


class CreateUser(graphene.mutation):
    class Arguemtns:
        user_name = graphene.String()
        
    ok = graphene.Boolean()
    user = graphene.Field(UserSQL)
    
    @classmethod 
    def mutate(root, info, **kwargs):
        user_db = User(user_name=kwargs.get("user_name"), )