import pickle
from time import sleep
from datetime import datetime

class RememberAll:
    def __init__(self,*args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self):
        state = self.__dict__.copy()
        state['saved'] = datetime.now()
        return state
    
    def __setstate__(self,state):
        self.__dict__.update(state)
        self.restored = datetime.now()

list_data = RememberAll(1,2,3,4,5)
print(list_data.data)

saved_data = pickle.dumps(list_data)
sleep(4)
restored_data = pickle.loads(saved_data)
print(restored_data.saved)
print(restored_data.restored)
