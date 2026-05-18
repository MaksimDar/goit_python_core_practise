##### using __getstate__ and __setstate__ for serialisation management 
import pickle 

class Robot:
    def __init__(self,name,battery_life):
        self.name = name
        self.battery_life = battery_life
        self.status = False

    def __getstate__(self):
        print('Get and prepare state for serialization')
        state = self.__dict__
        del state['status']
        return state

    def __setstate__(self, state):
        print('Reinnovate state')
        self.__dict__.update(state)
        self.status = True

robot_1 = Robot("Maksym", 100)

serialized_robot = pickle.dumps(robot_1)

deserialized_robot = pickle.loads(serialized_robot)

print(deserialized_robot.__dict__)