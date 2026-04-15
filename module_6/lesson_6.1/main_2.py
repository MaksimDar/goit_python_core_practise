#### __init__ extension

class Item:
    def __init__(self,name,price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
item_1 = Item('Phone', 150, 3)
item_2 = Item('Laptop', 1600, 5)
print(item_1.calculate_total_price())
print(item_2.calculate_total_price())