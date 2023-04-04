import requests

url = "http://localhost:5000/graphql"

body = """
{
  allTrainLogs{
    edges{
      node{
        epoch
        log
        createdAt
        description
        experiment {
          experimentIndex
          project {
            projectName
            authorName
            createdAt
            upatedAt
            description
          }
        }
      }
    }
  }
}
"""

resp = requests.post(url=url, json={"query": body})
print("response status", resp.status_code)
if resp.status_code == 200:
    print(resp.content)
    print(resp.json())
