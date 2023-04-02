from flask import Flask 
from flask_graphql import GraphQLView
from mySqlalchemy.database import init_db

app = Flask(__name__)
app.debug = True 

if __name__ == '__main__':
    init_db()
    app.run()
    