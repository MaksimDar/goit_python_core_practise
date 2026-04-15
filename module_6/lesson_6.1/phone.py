from item import Item

class Phone(Item):
    pay_rate = 0.5
    def __init__(self, name, price,quantity,broken_phones=0):
        super().__init__(name,price,quantity)
        self.broken_phones = broken_phones
    def info(self):
        return f"Phone(name={self.get_name()}, price={self.get_price()}, quantity={self.quantity} broken_phones={self.broken_phones}"
phone = Phone('Android', 840,2,13)

# print(phone.info())
# phone.apply_discount()
# print(phone.info())


# ##### check load_data_from_csv

# item = Item('Apple',1200,3)

# item.load_data_from_csv()
# print(item.info())
# print(Item.all_info())


# ######### Inheritance from Item
