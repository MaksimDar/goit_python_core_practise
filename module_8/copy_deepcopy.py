import copy

class MyClass:
    def __init__(self,value):
        self.value = value

    def __copy__(self):
        print("Copy called")
        return MyClass(self.value)
    
    def __deepcopy__(self,memo=None):
        print("Deep copy called")
        return MyClass(copy.deepcopy(self.value,memo))
    

obj_1 = MyClass(5)

obj_1_copy = copy.copy(obj_1)
obj_1_copy.value = 10

obj_1_deep = copy.deepcopy(obj_1)
obj_1_deep.value = 20

print(obj_1.value,obj_1_copy.value,obj_1_deep.value)