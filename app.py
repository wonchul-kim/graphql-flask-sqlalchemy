from flask import Flask 
from flask_graphql import GraphQLView
from flask_socketio import SocketIO
from myDB.mySqlalchemy.database import db_session 
from myDB.myGraphql.schema import schema

app = Flask(__name__)

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

socketio = SocketIO(app, async_mode=None, cors_allowed_origins="*")

@app.teardown_appcontext 
def shutdown_session(exception=None):
    db_session.remove()
    
if __name__ == '__main__':
    # from myDB.mySqlalchemy.actions import init_db, make_fake_db
    # init_db()
    # make_fake_db()
    # app.run(host='192.168.11.177', port=5000)
    import os
    from dotenv import load_dotenv
    print(os.path.exists("myDB/dockers/flask/.env"))
    load_dotenv("myDB/dockers/flask/.env")
    host = str(os.environ.get("FLASK_HOST"))
    port = int(os.environ.get("FLASK_PORT"))
    debug = bool(os.environ.get("FLASK_DEBUG"))

    socketio.run(app, host=host, port=port, debug=debug)
    