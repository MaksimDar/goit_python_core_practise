class Car:
    def __init__(self,name,year,price):
        self.name = name
        self.year = year
        self.price = price
    
    def __lt__(self,other):
        return self.price < other.price
    
    def __gt__(self,other):
        return self.price > other.price
    
    def __le__(self,other):
        return self.price <= other.price
    
    def __ge__(self,other):
        return self.price >= other.price
    
    def __eq__(self,other):
        return self.price == other.price
    

car_one = Car('Toyota', 2018,57000)
car_two = Car('Audi', 2016,75000)

print(car_one > car_two)