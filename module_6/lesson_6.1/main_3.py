from kboard import Keyboard
from phone import Phone

item1 = Phone('Apple', 500,2)
item1.apply_discount()

print(item1.get_price())


item2 = Keyboard('Nokia', 1000)
item2.apply_discount()

print(item2.get_price())


# item = Item('MyName', 560,3)

# print(item.info())

# item.name = 'OtherName'

# print(item.name)

# print(item.__dict__)



