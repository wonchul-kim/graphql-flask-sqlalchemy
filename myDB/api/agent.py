from python_graphql_client import GraphqlClient 
import asyncio
import sys 
import argparse
import json

class myDB():
    def __new__(cls, endpoint_ip="localhost", endpoint_port=5000, verify=False, verbose=False):
        if not hasattr(cls, 'instance'):
            cls.instance = super(myDB, cls).__new__(cls)
        
        return cls.instance

    def __init__(self, endpoint_ip="localhost", endpoint_port=5000, verify=False, verbose=False):
        print(f"myDB instance is defined")
        self.__client = GraphqlClient(endpoint='http://{}:{}/graphql'.format(endpoint_ip, endpoint_port), verify=verify)
        self._var_verbose = verbose
        self._var_config = None
        self._db_info = {}
        
        self.config = argparse.Namespace()
        self.train_experiment_id = None
        
        print(f"client is {self.__client}")

    def init(self, user_name="NONE", project_name="NONE"):
        if user_name == "":
            user_name = "NONE"
        if project_name == "":
            project_name = "NONE"
        self._db_info['user_name'] = user_name
        self._db_info['project_name'] = project_name
        self.save_user_name()
        self.save_project_name()

    def save_train_info(self, parameters={}, dataset_info={}):
        self._db_info['parameters'] = parameters
        self._db_info['dataset_info'] = dataset_info
        self.save_train_experiment()

    def log(self, train_log):
        self._db_info['train_log'] = train_log
        self.save_train_log()

    def execute(self, query, variables, use_async=True, verbose=False):    
        if use_async:
            response = asyncio.run(self.__client.execute_async(query=query, variables=variables))
        else:
            response = self.__client.execute(query=query, variables=variables)
        
        if verbose:
            print("* response: ", response)
        
        if not "errors" in response.keys():
            return response['data']
        else:
            print(f"There is some error: {response}")
            return response
        
    def save_user_name(self, description="NONE"):
        variables = {"user_name": self._db_info['user_name']}
        if description == "":
            variables['description'] = "NONE"
        else:
            variables['description'] = description
            
        query = """
                mutation ($user_name: String!, $description: String!) {
                    createUser(userName: $user_name, description: $description) {
                        done
                        verbose
                    }
                }
                """
        data = self.execute(query, variables)
        if self._var_verbose:
            print(f"[{self.save_user_name.__name__}] - {data} for {self._db_info['user_name']}")
        
        # if not data['createUser']['done']:
        #     sys.exit(0)
            
    def save_project_name(self, description="NONE"):
        variables = {'user_name': self._db_info['user_name'], 'project_name': self._db_info['project_name']}
        if description == "":
            variables['description'] = "NONE"
        else:
            variables['description'] = description
            
        query = """
                mutation ($user_name: String!, $project_name: String!, $description: String!){
                    createProject(userName: $user_name, projectName: $project_name, description: $description){
                        done
                        verbose
                    }
                }
                """
        data = self.execute(query, variables)
        if self._var_verbose:
            print(f"[{self.save_project_name.__name__}] - {data} for {self._db_info['project_name']}")
        
        # if not data['createProject']['done']:
        #     sys.exit(0)
        
    def save_train_experiment(self, description="NONE"):
        variables = {'user_name': self._db_info['user_name'], 'project_name': self._db_info['project_name'], \
                    'parameters': json.dumps(self._db_info['parameters']), "dataset_info": json.dumps(self._db_info['dataset_info'])}
        if description == "":
            variables['description'] = "NONE"
        else:
            variables['description'] = description
        if not "description" in variables.keys() or variables['description'] == "":
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
        
        print(data)
        
        self.train_experiment_id = data['createTrainExperiment']['experimentId']
        if self._var_verbose:
            print(f"[{self.save_train_experiment.__name__}] - {data} for {self.train_experiment_id}")

        # if not data['createTrainExperiment']['done']:
        #     sys.exit(0)

    def save_train_log(self):
        variables = {'user_name': self._db_info['user_name'], 'project_name': self._db_info['project_name'], \
                    'log': json.dumps(self._db_info['train_log'])}

        query = """
                mutation ($user_name: String!, $project_name: String!, $log: JSONString!){
                    createTrainLog(userName: $user_name, projectName: $project_name, log: $log){
                        done
                        verbose
                    }
                }
                """
                
        data = self.execute(query, variables)
        
        print(data)
        
        if self._var_verbose:
            print(f"[{self.save_train_log.__name__}] - {data}")

        # if not data['createTrainExperiment']['done']:
        #     sys.exit(0)



if __name__ == '__main__':
    agent = myDB(endpoint_ip="192.168.11.177", endpoint_port=5000, verify=False, verbose=True)
    agent.init(user_name="wonchul", project_name="interojo")
    agent.save_train_info()
    agent.log({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})