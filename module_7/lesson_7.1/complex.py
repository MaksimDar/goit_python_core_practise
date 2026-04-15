
###### Difference between __str__ and __repr__

class Complex:
    def __init__(self,real,imagionary):
        self.real = real
        self.imagionary = imagionary

    def __str__(self):
        return f"{self.real} + {self.imagionary}i"
    
    def __repr__(self):
        return f"{self.real} - {self.imagionary}i"
    

number = Complex(10,20)

print(number)
print(str(number))
print(repr(number))