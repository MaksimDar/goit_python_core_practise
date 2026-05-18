# import json
# contacts = {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }

# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'w', encoding="utf-8") as file:
#         dictionary = {"contacts": contacts}
#         json.dump(dictionary,file, indent=2)
        
    
        


# def read_contacts_from_file(filename):
#     with open(filename, 'r') as file:
#         read = json.load(file)
#         list = read.values()
#         return read, list
    
# write_contacts_to_file('contacts.json', contacts)
# print(read_contacts_from_file("contacts.json"))

# import csv

# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False
#     },
#     {
#         "name": "Chaim Lewis",
#         "email": "dui.in@egetlacus.ca",
#         "phone": "(294) 840-6685",
#         "favorite": False
#     },
#     {
#         "name": "Kennedy Lane",
#         "email": "mattis.Cras@nonenimMauris.net",
#         "phone": "(542) 451-7038",
#         "favorite": True
#     },
#     {
#         "name": "Wylie Pope",
#         "email": "est@utquamvel.net",
#         "phone": "(692) 802-2949",
#         "favorite": False
#     },
#     {
#         "name": "Cyrus Jackson",
#         "email": "nibh@semsempererat.com",
#         "phone": "(501) 472-5218",
#         "favorite": True
#     }
# ]

# def write_contacts_to_file(filename, contacts):
#     with open(filename,'w') as file:
#         fieldnames = ['name', 'email', 'phone','favorite']
#         writer = csv.DictWriter(file,fieldnames)
#         writer.writeheader()
#         writer.writerows(contacts)

        


# def read_contacts_from_file(filename):
#     with open(filename, 'r') as file:
#         reader = csv.DictReader(file)
#         contacts = []
#         for row in reader:
#             contacts.append({"name": row['name'], "email": row['email'], 'phone': row['phone'], 'favorite': True if row['favorite'] == 'True' else False})
            
#         return contacts


# write_contacts_to_file('contacts.csv',contacts)
# print(read_contacts_from_file('contacts.csv'))

# import pickle


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite 

# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         self.filename = filename
#         if contacts is None:
#             contacts = []
#         self.contacts = contacts
        

#     def save_to_file(self):
#         with open(self.filename, 'wb') as file:
#             pickle.dump(self,file)
        
            

#     def read_from_file(self):
#         with open(self.filename, 'rb') as file:
#             obj = pickle.load(file)
#             return obj

# contacts = [
#     Person(
#         "Allen Raymond",
#         "nulla.ante@vestibul.co.uk",
#         "(992) 914-3792",
#         False,
#     ),
#     Person(
#         "Chaim Lewis",
#         "dui.in@egetlacus.ca",
#         "(294) 840-6685",
#         False,
#     ),
# ]

# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# person_from_file = persons.read_from_file()
# print(persons == person_from_file)  # False
# print(persons.contacts[0] == person_from_file.contacts[0])  # False
# print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
# print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
# print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    shallow_copy = copy.copy(person)
    return shallow_copy

person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

print(copy_person == person)  # False
print(copy_person.name == person.name) 