### method __call__ => first approach

# class Product:
#     def __init__(self,value_one,value_two):
#         self.value_one = value_one
#         self.value_two = value_two

#     def __call__(self):
#         return self.value_one * self.value_two
    
# product = Product(6,6)
# print(product())

### method __call__ => second approach

class Product:

    def __call__(self, value_one, value_two):
        return value_one * value_two
    
product = Product()
print(product(9,6))