from mySqlalchemy.models import User
from mySqlalchemy.database import db_session
import graphene 
from graphene import relay 
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserSQL(SQLAlchemyObjectType):
    class Meta:
        model = User 
        interfaces = (relay.Node,)


class CreateUser(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        description = graphene.String(required=False)
        
    done = graphene.Boolean()
    user = graphene.Field(UserSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        user_name = kwargs.get("user_name")
        user_db = User(user_name=user_name)
        
        db_session.add(user_db)
        db_session.commit()
        done = True
        
        return CreateUser(user=user_db, done=done)