from flask import Flask 
from flask_graphql import GraphQLView

from myDB.mySqlalchemy.database import db_session 
from myDB.myGraphql.schema import schema

app = Flask(__name__)
app.debug = True 

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

@app.teardown_appcontext 
def shutdown_session(exception=None):
    db_session.remove()
    
if __name__ == '__main__':
    from myDB.mySqlalchemy.actions import init_db, make_fake_db
    # init_db()
    # make_fake_db()
    app.run()
    