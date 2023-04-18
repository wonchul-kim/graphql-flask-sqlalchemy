from client import client
import asyncio

def read_all_users(use_async=True, verbose=False, only_users=True):
    query = """
            query
                {
                allUsers {
                    edges {
                        node {
                            id
                            userName
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
        
    edges = response['data']['allUsers']['edges']
    
    if only_users:
        users_list = []
        for edge in edges:
            users_list.append(edge['node']['userName'])
            
        return users_list
    else:
        return edges

def create_user(variables={}, use_async=True, verbose=False, only_done=True):
    query = """
            mutation ($user_name: String!) {
                createUser(userName: $user_name) {
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
        return response['data']['createUser']['done']
    else:
        return response['data']['createUser']
    
def delete_user(variables={}, use_async=True, verbose=False):
    query = """
            mutation ($user_name: String!) {
                deleteUser(userName: $user_name) {
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
    
    return response['data']['deleteUser']

def update_user(variables={}, use_async=True, verbose=False):
    query = """
            mutation ($user_name: String!, $new_user_name: String!) {
                updateUser(userName: $user_name, newUserName: $new_user_name) {
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
    
    return response['data']['updateUser']

def find_user(variables={}, use_async=True, verbose=False):
    query = """
            query ($user_name: String!){
                findUser(userName: $user_name) {
                    id
                    userName
                    description
                }
            }
            """
    
    if use_async:
        response = asyncio.run(client.execute_async(query=query, variables=variables))
    else:
        response = client.execute(query=query, variables=variables)
    
    if verbose:
        print("* response: ", response)
    
    return response['data']['findUser']
                
if __name__ == '__main__':
    users = read_all_users(True, True, True)
    print(users)
    print("-----------------------------------------------------------------------------------------------------")
    variables = {"user_name": "waefsdfasfasfawefawefawefawefaweflkj"}
    ret = create_user(variables, True, True)
    print(ret)
    print("-----------------------------------------------------------------------------------------------------")

    variables = {"user_name": "wonchul2"}
    ret = find_user(variables, True, True)
    print(ret)
    variables = {"user_name": "wonchul1"}
    ret = find_user(variables, True, True)
    print(ret)
    
    print("-----------------------------------------------------------------------------------------------------")
    variables = {"user_name": "wonchul3"}
    ret = delete_user(variables)
    print(ret)
    print("-----------------------------------------------------------------------------------------------------")
    variables = {"user_name": "wonchul44", "new_user_name": "wonchul"}
    ret = update_user(variables)
    print(ret)