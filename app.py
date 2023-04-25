from flask import Flask 
from flask_graphql import GraphQLView
from flask_socketio import SocketIO
from myDB.mySqlalchemy.database import db_session 
from myDB.myGraphql.schema import schema

app = Flask(__name__)
host = '192.168.11.177'
port = 5000
debug = True 

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

socketio = SocketIO(app, async_mode=None, cors_allowed_origins="*")

@app.teardown_appcontext 
def shutdown_session(exception=None):
    db_session.remove()
    
if __name__ == '__main__':
    from myDB.mySqlalchemy.actions import init_db, make_fake_db
    # init_db()
    # make_fake_db()
    # app.run(host='192.168.11.177', port=5000)
    socketio.run(app, host=host, port=port, debug=debug)
    