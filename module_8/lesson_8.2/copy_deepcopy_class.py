from collections import UserList
from copy import copy, deepcopy


class CopyList(UserList):
    def __init__(self,*data):
        super().__init__()
        self.data = list(data)

    def __copy__(self):
        cls = self.__class__
        new = cls.__new__(cls)
        new.data = self.data
        return new
    
    def __deepcopy__(self,memodict):
        cls = self.__class__
        result = cls.__new__(cls)
        memodict[id(self)] = result
        for key, value in self.__dict__.items():
            setattr(result, key, deepcopy(value, memodict))
        return result

test_list = CopyList([1,2,3,4,5])

copy_test = copy(test_list)

deep_copy_test = deepcopy(test_list)

print(id(test_list), test_list)
print(id(copy_test), copy_test)
print(id(deep_copy_test), deep_copy_test)

print(id(test_list[0]), test_list[0])
print(id(copy_test[0]), copy_test[0])
print(id(deep_copy_test[0]), deep_copy_test[0])

