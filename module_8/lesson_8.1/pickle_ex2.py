from pickle import dumps, loads

class Absolute:
    value = "some data"
    def __init__(self):
        print("Initialization")
        self.data = 'another'


instance = Absolute()

deserialised_instance = dumps(instance)
deserialised_class = dumps(Absolute)

restored_instance = loads(deserialised_instance)
restored_class = loads(deserialised_class)

### show instance
# print(instance.value, instance.data)

# ### show decerialised instance
# print(restored_instance.value, restored_instance.data)

# print(dir(restored_class))

# print(restored_class.__dict__)