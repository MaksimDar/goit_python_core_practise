class Item:
    pay_rate = 0.8
    all_class_instances = list()

    def __init__(self,name,price, quantity=0):
        assert price >= 0, f"Price {price} can be more or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} can be more or equal to 0"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all_class_instances.append(self)

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        if len(value) < 5:
            raise Exception('Name is too short')
        self.__name = value
    def calculate_total_price(self):
        return self.__price * self.quantity
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    def info(self):
        return f"Item(name={self.get_name()}, price={self.get_price()}, quantity={self.quantity})"
    @classmethod
    def all_info(cls):
        return [item.info() for item in cls.all_class_instances]
    @classmethod
    def load_data_from_csv(cls):
        with open('items.csv', 'r') as file:
            next(file)
            for line in file:
                name,price,quantity = line.strip().split(',')
                ## Item can be replaced by cls as well
                Item(
                    name=name.strip('"'),
                    price=float(price),
                    quantity=int(quantity)
                )


# item_1 = Item('Phone', 150, 3)
# item_2 = Item('Laptop', 1600, 5)
# # print(item_1.calculate_total_price())
# # print(item_2.calculate_total_price())

# # print(item_1.__dict__)
# # print(item_2.__dict__)

# # print(item_1.calculate_total_price())
# # item_1.apply_discount()
# # print(item_1.calculate_total_price())
# print(item_2.info())
# print(Item.all_info())