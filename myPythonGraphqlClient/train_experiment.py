from client import client
import asyncio
import json 

def read_all_train_experiments(use_async=True, verbose=False, only_train_projects=True):
    query = """
            query {
                allTrainExperiments {
                    edges {
                        node {
                            id
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
        
    edges = response['data']['allTrainExperiments']['edges']
    
    if only_train_projects:
        experiments_list = []
        for edge in edges:
            experiments_list.append(edge['node']['id'])
            
        return experiments_list
    else:
        return edges

def create_train_experiment(variables={}, use_async=True, verbose=False, only_done=True):

    query = """
            mutation ($user_name: String!, $project_name: String!, $dataset_info: JSONString!, $parameters: JSONString!){
                createTrainExperiment(userName: $user_name, projectName: $project_name, datasetInfo: $dataset_info, parameters: $parameters){
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
        return response['data']['createTrainExperiment']['done']
    else:
        return response['data']['createTrainExperiment']
               
if __name__ == '__main__':
    users = read_all_train_experiments(True, True, True)
    print(users)
    print("-----------------------------------------------------------------------------------------------------")
    variables = {"user_name": "wonchul2", "project_name": "interojo", \
                "dataset_info": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]}), \
                "parameters": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_experiment(variables, True, True)
    print(ret)
    print("-----------------------------------------------------------------------------------------------------")

    # variables = {"user_name": "wonchul2"}
    # ret = find_user(variables, True, True)
    # print(ret)
    # variables = {"user_name": "wonchul1"}
    # ret = find_user(variables, True, True)
    # print(ret)