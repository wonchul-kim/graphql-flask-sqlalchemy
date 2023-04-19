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

def create_train_experiment(variables={}, use_async=True, verbose=False, only_id=True):
    if not "user_name" in variables.keys():
        variables['user_name'] = "NONE"
    if variables['user_name'] == "":
        variables['user_name'] = "NONE"
    if not "project_name" in variables.keys():
        variables['project_name'] = "NONE"
    if variables['project_name'] == "":
        variables['project_name'] = "NONE"
    if not "dataset_info" in variables.keys():
        variables['dataset_info'] = "NONE"
    if variables['dataset_info'] == "":
        variables['dataset_info'] = "NONE"
    if not "parameters" in variables.keys():
        variables['parameters'] = "NONE"
    if variables['parameters'] == "":
        variables['parameters'] = "NONE"
    if not "description" in variables.keys():
        variables['description'] = "NONE"
    if variables['description'] == "":
        variables['description'] = "NONE"

    query = """
            mutation ($user_name: String!, $project_name: String!, $dataset_info: JSONString!, $parameters: JSONString!, $description: String!){
                createTrainExperiment(userName: $user_name, projectName: $project_name, datasetInfo: $dataset_info, parameters: $parameters, description: $description){
                    experimentId
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
    
    if only_id:
        print("response['data']['createTrainExperiment']: ", response['data']['createTrainExperiment'])
        return response['data']['createTrainExperiment']['experimentId']
    else:
        return response['data']['createTrainExperiment']
               
if __name__ == '__main__':
    variables = {"user_name": "wonchul1", "project_name": "interojo", \
                "dataset_info": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]}), \
                "parameters": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_experiment(variables, True, True)
    variables = {"user_name": "wonchul1", "project_name": "interojo", \
                "dataset_info": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]}), \
                "parameters": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_experiment(variables, True, True)
    variables = {"user_name": "wonchul1", "project_name": "interojo", \
                "dataset_info": json.dumps({"a": 2, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]}), \
                "parameters": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_experiment(variables, True, True)
    variables = {"user_name": "wonchul2", "project_name": "central", \
                "dataset_info": json.dumps({"a": 3, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]}), \
                "parameters": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_experiment(variables, True, True)
    variables = {"user_name": "wonchul2", "project_name": "central", \
                "dataset_info": json.dumps({"a": 3, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]}), \
                "parameters": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_experiment(variables, True, True)
    variables = {"user_name": "wonchul2", "project_name": "central", \
                "dataset_info": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]}), \
                "parameters": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_experiment(variables, True, True)
    print("-----------------------------------------------------------------------------------------------------")
    users = read_all_train_experiments(True, True, True)
    print(users)
    print("-----------------------------------------------------------------------------------------------------")

    # variables = {"user_name": "wonchul2"}
    # ret = find_user(variables, True, True)
    # print(ret)
    # variables = {"user_name": "wonchul1"}
    # ret = find_user(variables, True, True)
    # print(ret)
    
    