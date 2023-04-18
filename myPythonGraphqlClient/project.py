from client import client
import asyncio

def read_all_projects(use_async=True, verbose=False, only_projects=True):
    query = """
            query{
                allProjects {
                    edges {
                        node {
                            id
                            projectName
                            description
                        }
                    }
                }
            }
            """

    if use_async:
        response = asyncio.run(client.execute_async(query=query))
    else:
        response = client.execute(query=query)
        
    if verbose:
        print("* response: ", response)
        
    edges = response['data']['allProjects']['edges']
    
    if only_projects:
        projects_list = []
        for edge in edges:
            projects_list.append(edge['node']['projectName'])
            
        return projects_list
    else:
        return edges

def create_project(variables={}, use_async=True, verbose=False, only_done=True):
    query = """
            mutation ($project_name: String!){
                createProject(projectName: $project_name){
                    done
                    verbose
                }
            }
            """
    
    if use_async:
        response = asyncio.run(client.execute_async(query=query, variables=variables))
    else:
        response = client.execute(query=query, variables=variables)
    
    if verbose:
        print("* response: ", response)
    
    if only_done:
        return response['data']['createProject']['done']
    else:
        return response['data']['createProject']
               
if __name__ == '__main__':
    users = read_all_projects(True, True, True)
    print(users)
    print("-----------------------------------------------------------------------------------------------------")
    variables = {"project_name": "central"}
    ret = create_project(variables, True, True)
    print(ret)
    print("-----------------------------------------------------------------------------------------------------")

    # variables = {"user_name": "wonchul2"}
    # ret = find_user(variables, True, True)
    # print(ret)
    # variables = {"user_name": "wonchul1"}
    # ret = find_user(variables, True, True)
    # print(ret)