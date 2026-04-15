from collections import UserList
from random import randint

class ExperimentResults(UserList):

    def positive_results(self):
        return list(filter(lambda x: x >= 0, self.data))
    
    def negative_results(self):
        return list(filter(lambda x: x < 0, self.data))
    
result = ExperimentResults()

for _ in range(20):
    result.append(randint(-10,10))

print(result)
print(result.positive_results())
print(result.negative_results())
print(result.data)
