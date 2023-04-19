from user import create_user
from project import create_project
from train_experiment import create_train_experiment
from train_log import create_train_log
import json

class myDB():
    def __init__(self):
        print("This is DB")
        
    def create_user(self, user_name):
        self.user_name = user_name
        variables = {"user_name": user_name}
        ret = create_user(variables, True, True)
        print(ret)
        
    def create_project(self, project_name):
        self.project_name = project_name
        variables = {"user_name": self.user_name, "project_name": project_name}
        ret = create_project(variables, True, True)
        print(ret)
        
    def create_experiment(self):
        variables = {"user_name": self.user_name, "project_name": self.project_name, \
            "dataset_info": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]}), \
            "parameters": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
        self.experiment_id = create_train_experiment(variables, True, True)
        print(self.experiment_id)
    
    def create_log(self):
        variables = {"experiment_id": self.experiment_id, \
                "log": json.dumps({"a": 1, "b": "c", "c": [1, 2, 3], "d": ["ab", "bc"]})}
        ret = create_train_log(variables, True, True)
        print(ret)