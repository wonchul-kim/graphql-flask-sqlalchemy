from myDB.mySqlalchemy.models import User
from myDB.mySqlalchemy.database import db_session
import graphene 
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserSQL(SQLAlchemyObjectType):
    class Meta:
        model = User 
        interfaces = (graphene.relay.Node,)

class CreateUser(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        description = graphene.String(required=False)
        
    done = graphene.Boolean()
    verbose = graphene.String()
    user = graphene.Field(UserSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        user_name = kwargs.get("user_name")
        if not db_session.query(User).filter_by(user_name=user_name).first():
            user_db = User(user_name=user_name)
            
            db_session.add(user_db)
            db_session.commit()
            done = True
            verbose = "Successfully done"
        
        else:
            done = False
            verbose = "That user-name already exists"
            
        return CreateUser(done=done, verbose=verbose)
    
class DeleteUser(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        
    done = graphene.Boolean()
    verbose = graphene.String()
    user = graphene.Field(UserSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        if 'user_name' in kwargs.keys():
            user_name = kwargs.get("user_name")
            
            if db_session.query(User).filter_by(user_name=user_name).first():
                db_session.query(User).filter_by(user_name=user_name).delete()
                db_session.commit()
                done = True
                verbose = "Successfully done"
            else:
                done = False
                verbose = "There is no such user-name"
            
        else:
            done = False 
            verbose = "A user-name must be provided"
        
        return DeleteUser(done=done, verbose=verbose) 
    
class UpdateUser(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        new_user_name = graphene.String(required=True)
        
    done = graphene.Boolean()
    verbose = graphene.String()
    user = graphene.Field(UserSQL)
    
    @classmethod 
    def mutate(root, info, _, **kwargs):
        if 'user_name' in kwargs.keys() and "new_user_name" in kwargs.keys():
            user_name = kwargs.get("user_name")
            new_user_name = kwargs.get("new_user_name")
            
            try:        
                db_session.query(User).filter_by(user_name=user_name).first().user_name = new_user_name
                db_session.commit()
                done = True
                verbose = "done"
            except:
                done = False
                verbose = "There is no such user-name"
            
        else:
            done = False 
            verbose = "User-name and new user-name must be provided"
        
        return UpdateUser(done=done, verbose=verbose) 