class User:
    def __init__(self,name,age):
        self.__private_name = None
        self.__private_age = None
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__private_name
    @name.setter
    def name(self, value: str):
        if value.isalpha():
            self.__private_name = value
        else:
            raise Exception('Name can contain only letters')
        
    @property
    def age(self):
        return self.__private_age
    @age.setter
    def age(self, value: str):
        if int(value) >= 18:
            self.__private_age = int(value)
        else:
            raise Exception('You are less than 18')
        
user1 = User('Maksym', '20')
user2 = User('Andrew', '19')
print(user1.name,user2.age)
        

        
    
