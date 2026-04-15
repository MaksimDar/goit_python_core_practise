from collections import UserList, UserDict

class Phones(UserList):
    def set_phone(self,phone):
        if len(phone) == 12:
            new_phone = '+' + phone
        elif len(phone) < 12:
            new_phone = '+38' + phone
        self.data.append(new_phone)

    def see_phone(self):
        return self.data
    
# phone = Phones()
# phone.set_phone('38096157201')
# phone.set_phone('38096155601')
# phone.set_phone('0961572019')

# print(phone.see_phone())

class User(UserDict):
    def set_name(self,name):
        self.data['name'] = name

    def get_name(self):
        return self.data.get('name')
    
    def set_phone(self,phone):
        phone_list = self.data.get('phones', Phones())
        phone_list.data.append(phone)
        self.data['phones'] = phone_list
    
    def get_phones(self):
        return self.data.get('phones')


user1 = User()
user1.set_name('Maksym')
user1.set_phone('+380960157201')
user1.set_phone('+632611261')
print(user1.get_name(),user1.get_phones())
    