# import requests

# url = 'http://localhost:5000/api/v2/sessions'

# print(requests.post(url).text)


from python_graphql_client import GraphqlClient 

client = GraphqlClient(endpoint='http://localhost:5000/graphql')

query = """
mutation{
  createUser(userName: "wonchul44") {
    done
    verbose
  }
}
"""

variables = {}

data = client.execute(query=query, variables=variables)

print(data)

import asyncio 

data = asyncio.run(client.execute_async(query=query, variables=variables))
print(data)