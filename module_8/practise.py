# expenses = {'hotel': 150,'breakfast': 20,'lunch': 29,'dinner': 41}

# file_expenses = 'expenses.txt'

# with open(file_expenses, 'w') as fh:
#     for key,item in expenses.items():
#         fh.write(f"{key} || {item}\n")
import pickle
import json

keys = {1:'key', 2:'go', '3': 'Hello man', '4': [1,2,3,4]}


##### pickle 


# to_bytes = pickle.dumps(keys)

# print(to_bytes)

# to_object = pickle.loads(to_bytes)

# print(to_object)

# with open('data.pickle', 'wb') as file:
#     cerialised = pickle.dump(keys,file)

# with open('data.pickle', 'rb') as file:
#     decerialised = pickle.load(file)

# print(decerialised)

#### json


# json_pack = json.dumps(keys)
# print(json_pack)
# unpack_json = json.loads(json_pack)
# print(unpack_json)

# with open('data.json', 'w') as file:
#     json.dump(keys,file)

# with open('data.json', 'r', encoding='utf-8') as file:
#     deserialised = json.load(file)
#     print(deserialised)


### csv

import csv

# Дані для запису
rows = [
    ["name", "age", "specialty"],
    ["Василь Гупало", 30, "Математика"],
    ["Марія Петренко", 22, "Фізика"],
    ["Олександр Коваленко", 20, "Інформатика"],
]

with open('data.csv',"w",newline="" ) as csvfile:

    writer = csv.writer(rows,delimiter=",")

    writer.writerows(rows)

