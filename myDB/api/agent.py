from python_graphql_client import GraphqlClient 
import asyncio
import sys 

class myDB():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(myDB, cls).__new__(cls)
        return cls.instance

    def __init__(self, endpoint_ip="localhost", endpoint_port=5000):
        self.__client = GraphqlClient(endpoint='http://{}:{}/graphql'.format(endpoint_ip, endpoint_port))
        self._config = None 
        
    def execute(self, query, variables, use_async=True, verbose=False):    
        if use_async:
            response = asyncio.run(self.__client.execute_async(query=query, variables=variables))
        else:
            response = self.__client.execute(query=query, variables=variables)
        
        if verbose:
            print("* response: ", response)
        
        return response['data']
                
    def init(self, user_name="NONE", project_name="NONE"):
        self._user_name = user_name 
        self._project_name = project_name 
        self.set_user_name()
        self.set_project_name()
        self.set_train_experiment()
                
    def save_user_name(self):
        variables = {"user_name": self._user_name}
        if variables['user_name'] == "":
            variables['user_name'] = "NONE"
        if not "description" in variables.keys():
            variables['description'] = "NONE"
        if variables['description'] == "":
            variables['description'] = "NONE"
        query = """
                mutation ($user_name: String!, $description: String!) {
                    createUser(userName: $user_name, description: $description) {
                        done
                        verbose
                    }
                }
                """
        data = self.execute(query, variables)
        print(data['createUser'])
        
        if not data['createUser']['done']:
            sys.exit(0)
            
    def save_project_name(self):
        variables = {"project_name": self._project_name}
        if variables['user_name'] == "":
            variables['user_name'] = "NONE"
        if variables['project_name'] == "":
            variables['project_name'] = "NONE"
        if not "description" in variables.keys():
            variables['description'] = "NONE"
        if variables['description'] == "":
            variables['description'] = "NONE"
        query = """
                mutation ($user_name: String!, $project_name: String!, $description: String!){
                    createProject(userName: $user_name, projectName: $project_name, description: $description){
                        done
                        verbose
                    }
                }
                """
        data = self.execute(query, variables)
        print(data['createProject'])
        
        if not data['createProject']['done']:
            sys.exit(0)
        
    def save_train_experiment(self):
        variables = {'user_name': self._user_name, 'project_name': self._project_name}
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
                
        data = self.execute(query, variables)
        self._train_experiment_id = data['createTrainExperiment']['experimentId']
        print(data['createTrainExperiment'])

        if not data['createTrainExperiment']['done']:
            sys.exit(0)

            
            