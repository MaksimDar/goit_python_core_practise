###### Methods getitem and setitem

from collections import UserDict

class PositiveNumber(UserDict):
    def __getitem__(self, index=None):
        if index is None:
            return self.data
        return self.data[index]
    
    def __setitem__(self,key,value):
        if value > 0:
            self.data[key] = value
    
    def __str__(self):
        return f"{self.data}"

numbers = PositiveNumber()

numbers[0] = 5
numbers[1] = -2
numbers[2] = 4
numbers[3] = 1
numbers[4] = 3

print(numbers)


