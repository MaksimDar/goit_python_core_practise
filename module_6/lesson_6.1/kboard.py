from item import Item

class Keyboard(Item):
    pay_rate = 0.2
    def __init__(self, name: str, price: float):
        super().__init__(name,price)
    def info(self):
        return f"Phone(name={self.get_name()}, price={self.get_price()}, year={self.year}"
