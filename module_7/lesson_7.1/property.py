###### classical approach

# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name
    
#     def set_name(self,name):
#         self.__name = name


# person = Person('Oleg', 20)

# print(person.get_name())
# person.set_name('Maksym')
# print(person.get_name())



#alternative through property 1-st

# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name
    
#     def set_name(self,name):
#         self.__name = name
    
#     name = property(get_name,set_name)


# person = Person('Oleg', 20)

# print(person.name)
# person.name = 'Maksym'
# print(person.name)



#alternative through property 2-nd

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age = age



person = Person('Oleg', 20)

print(person.name)
person.name = 'Maksym'
print(person.name)

