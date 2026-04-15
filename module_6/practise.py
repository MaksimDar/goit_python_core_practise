# class Player:
#     sport = 'tennis' 
#     age = '25'

# p1 = Player()

# print(p1.sport)
# print(p1.age)

# p2 = Player()
# p2.sport = 'football'
# print(p2.sport)
# print(p2.age)

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active
#         self.__is_admin = is_admin

#     def greeting(self):
#         return f"Hi {self.name}"

#     def is_active(self):
#         return self._is_active

#     def set_active(self, active: bool):
#         self._is_active = active

# p = Person("Boris", 34, True, False)
# print(p._Person__is_admin)


# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age
#     #### works without make_sound as well
#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self) -> str:
#         return "Meow"

# class Dog(Animal):
#     def make_sound(self) -> str:
#         return "Woof"

# class Cow(Animal):  
#     def make_sound(self):
#         return "Moo"

# my_cat = Cat("Simon", 4)
# my_dog = Dog("Rex", 5)
# my_cow = Cow("Bessie", 3)

# print(my_cat.make_sound())  # Виведе "Meow"
# print(my_dog.make_sound())  # Виведе "Woof"
# print(my_cow.make_sound())  # Виведе "Moo"

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# print(D.__mro__)  # Виведе порядок розв'язання методів для класу D

# from typing import Protocol

# class Speaker(Protocol):
#     def peak(self) -> str:
#         pass

# class Dog:
#     def speak(self) -> str:
#         return "Woof"

# class Cat:
#     def speak(self) -> str:
#         return "Meow"

# class Robot:
#     def speak(self) -> str:
#         return "Beep boop"

# def make_it_speak(speaker: Speaker) -> None:
#     print(speaker.speak())

# dog = Dog()
# cat = Cat()
# robot = Robot()

# make_it_speak(dog)  # Виведе: Woof
# make_it_speak(cat)  # Виведе: Meow
# make_it_speak(robot)  # Виведе: Beep boop

# from collections import UserDict

# class MyDictionary(UserDict):
#     def add_key(self,key,value):
#         self.data[key] = value

# my_dict = MyDictionary({'Maksym': 20})
# my_dict.add_key('Makar',12)
# print(my_dict)

# from collections import UserDict

# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     {
#         "name": "Chaim Lewis",
#         "email": "dui.in@egetlacus.ca",
#         "phone": "(294) 840-6685",
#         "favorite": False,
#     },
#     {
#         "name": "Kennedy Lane",
#         "email": "mattis.Cras@nonenimMauris.net",
#         "phone": "(542) 451-7038",
#         "favorite": True,
#     }
# ]

# class Customer(UserDict):
#     def phone_info(self):
#         return f"{self.get('name')}: {self.get('phone')}"

#     def email_info(self):
#         return f"{self.get('name')}: {self.get('email')}"

# if __name__ == "__main__":
#     customers = [Customer(el) for el in contacts]

#     print("---------------------------")

#     for customer in customers:
#         print(customer.phone_info())

#     print("---------------------------")

#     for customer in customers:
#         print(customer.email_info())


# from collections import UserList

# class MyList(UserList):
#     # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
#     def add_if_not_exists(self, item):
#         if item not in self.data:
#             self.data.append(item)

# # Створення екземпляру MyList
# my_list = MyList([1, 2, 3])
# print("Оригінальний список:", my_list)

# # Додавання елементу, якщо він не існує
# my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
# my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
# print("Оновлений список:", my_list)

# from collections import UserString

# # Створення класу, який розширює UserString
# class MyString(UserString):
#     # Додавання методу, який перевіряє, чи рядок є паліндромом
#     def is_palindrome(self):
#         return self.data == self.data[::-1]

# # Створення екземпляру MyString
# my_string = MyString("radar")
# print("Рядок:", my_string)
# print("Чи є паліндромом?", my_string.is_palindrome())

# # Створення іншого екземпляру MyString
# another_string = MyString("hello")
# print("Рядок:", another_string)
# print("Чи є паліндромом?", another_string.is_palindrome())

# from dataclasses import dataclass

# @dataclass
# class Rectangle:
#     width:int
#     height: int

#     def area_rectangle_calculate(self):
#         return self.width*self.height
    
# rectangle_1 = Rectangle(45,3)
# rectangle_2 = Rectangle(23,4)
# rectangle_3 = Rectangle(15,4)

# print(rectangle_1.area_rectangle_calculate())
# print(rectangle_2.area_rectangle_calculate())
# print(rectangle_3.area_rectangle_calculate())

# from enum import Enum

# class Day(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7


# day_from_value = Day(1)
# print(day_from_value)  # Виведе: Day.MONDAY



class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        if self.contacts.get(id):
            return self.contacts[id]
        else:
            return None









