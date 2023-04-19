
from my_db import myDB
import time


class Agent():
    def __init__(self):
        print("This is agent instance")

        self.db = myDB()
        
    def set(self):
        self.db.create_user(user_name="wonchul")
        
    def set_datsets(self):
        self.db.create_project(project_name='abcsdfawefawefawefa')
        


if __name__ == '__main__':
    agent = Agent()
    
    agent.set()
    agent.set_datsets()