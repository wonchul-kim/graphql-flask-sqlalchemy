import time 

class Engine():
    def __init__(self):
        print("This is for training engine")
        
    def set_datasets(self):
        pass 
    
    def set_model(self):
        pass 
    
    def train_one_epoch(self):
        pass 
    
    def validate(self):
        pass 
    
    def end(self):
        pass 
    
    
if __name__ == '__main__':
    engine = Engine()
    
    engine.set_datasets()
    engine.set_model()
    
    for epoch in range(50):
        engine.train_one_epoch()
        engine.validate()
        
        time.sleep(1)
        print("\r{}".format(epoch), end="")