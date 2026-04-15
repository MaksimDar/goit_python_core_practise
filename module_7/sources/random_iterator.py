from random import randint

class RandIter():
    def __init__(self,start,end,quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        number = randint(self.start,self.end)
        return number
    
if __name__ == '__main__':
    random_list = RandIter(2,18,6)

    for ran_num in random_list:
        print(ran_num)