from client import client
import asyncio
import json 

def read_all_train_logs(use_async=True, verbose=False, only_train_logs=True):
    query = """
            query{
                allTrainLogs {
                    edges {
                        node {
                            id
                            log
                            trainExperimentId
                                trainExperiment {
                                    id
                                }
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
        
    edges = response['data']['allTrainLogs']['edges']
    
    if only_train_logs:
        logs_list = []
        for edge in edges:
            logs_list.append(edge['node']['log'])
            
        return logs_list
    else:
        return edges

def create_train_log(variables={}, use_async=True, verbose=False, only_done=True):
    if not "user_name" in variables.keys():
        variables['user_name'] = "NONE"
    if variables['user_name'] == "":
        variables['user_name'] = "NONE"
    if not "project_name" in variables.keys():
        variables['project_name'] = "NONE"
    if variables['project_name'] == "":
        variables['project_name'] = "NONE"
    if len(variables.keys()) == 0:
        return False 
    else:
        query = """
                mutation ($user_name: String!, $project_name: String!, $log: JSONString!){
                    createTrainLog(userName: $user_name, projectName: $project_name, log: $log){
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
            return response['data']['createTrainLog']['done']
        else:
            return response['data']['createTrainLog']
    
               
if __name__ == '__main__':
    variables = {"project_name": "interojo", "user_name": "wonchul1",
                "log": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "interojo", "user_name": "wonchul1",
                "log": json.dumps({"a": 2, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "interojo", "user_name": "wonchul1",
                "log": json.dumps({"a": 3, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "interojo", "user_name": "wonchul1",
                "log": json.dumps({"a": 4, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "interojo", "user_name": "wonchul1",
                "log": json.dumps({"a": 5, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "central", "user_name": "wonchul2",
                "log": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "central", "user_name": "wonchul2",
                "log": json.dumps({"a": 2, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "central", "user_name": "wonchul2",
                "log": json.dumps({"a": 3, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "central", "user_name": "wonchul2",
                "log": json.dumps({"a": 4, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "central", "user_name": "wonchul2",
                "log": json.dumps({"a": 5, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    variables = {"project_name": "central", "user_name": "wonchul2",
                "log": json.dumps({"a": 6, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
    ret = create_train_log(variables, True, True)
    
    print("-----------------------------------------------------------------------------------------------------")
    users = read_all_train_logs(True, True, True)
    print(users)
    print("-----------------------------------------------------------------------------------------------------")

    # variables = {"user_name": "wonchul2"}
    # ret = find_user(variables, True, True)
    # print(ret)
    # variables = {"user_name": "wonchul1"}
    # ret = find_user(variables, True, True)
    # print(ret)