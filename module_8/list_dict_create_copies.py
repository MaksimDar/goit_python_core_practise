# my_dict = {"name": "Maksym", "surname": 'Dovhusha'}
# copy_dict = {**my_dict}

# copy_dict['age'] = 20
# del copy_dict['surname']
# print(my_dict, copy_dict)

import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list[2]["age"] = 30
print(my_list)
print(copy_list)
