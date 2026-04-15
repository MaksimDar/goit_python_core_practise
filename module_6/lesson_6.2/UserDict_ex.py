from collections import UserDict

class DualDict(UserDict):
    def __init__(self,initial=0):
        if initial is None:
            self.from_value = dict()
            self.data = dict()
        else:
            self.data = initial
            self.from_value = {val: key for key, val in initial.items()}

    def __setitem__(self,key,value):
        self.data[key] = value
        if value in self.from_value:
            old = self.from_value[value]
            self.from_value.pop(old)
        self.from_value[value] = key

    def get_by_value(self, value):
        return self.from_value[value]
    
    def set_by_value(self,key,value):
        old_key = self.from_value[value]
        self.data.pop(old_key)
        self.data[key] = value
        self.from_value[value] = key

dual = DualDict({8:12,89:63})

print(dual.data)
# print(dual.get_by_value(2) == 1)

# dual.set_by_value(4,8)

# print(dual)