from flask import Flask 
from flask_graphql import GraphQLView

from mySqlalchemy.database import init_db, db_session 
from mySqlalchemy.schema import schema

app = Flask(__name__)
app.debug = True 

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

@app.teardown_appcontext 
def shutdown_session(exception=None):
    db_session.remove()
    
if __name__ == '__main__':
    init_db()
    app.run()
    
example_query = """
{
  allEmployees(sort: [NAME_ASC, ID_ASC]) {
    edges {
      node {
        id
        name
        department {
          id
          name
        }
        role {
          id
          name
        }
      }
    }
  }
}
"""