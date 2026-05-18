import csv

FILENAME = 'users.csv'

# users = [
#   {'name': 'Roman', 'age': 22, 'sex': 'male'},
#   {'name': 'Oksana', 'age': 22, 'sex': 'female'},
#   {'name':'Mike', 'age': 22, 'sex': 'male'},
# ]

# with open(FILENAME, 'w', newline="", encoding='utf-8') as file:
#     field_names = ['name', 'age', 'sex']
#     writer = csv.DictWriter(file,delimiter=",",fieldnames=field_names)
#     writer.writeheader()
#     for row in users:
#         writer.writerow(row)

#### Read full file


# with open(FILENAME,'r',newline="",encoding='utf-8') as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)


#### Read full file and get names


# with open(FILENAME,'r',newline="",encoding='utf-8') as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row.get("name"))