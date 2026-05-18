import csv

character_banana = {'first_name': 'Baked', 'last_name': 'Banana'}
character_octopus = {'first_name': 'Lovely', 'last_name': 'Octopus'}
character_novelist = {'first_name': 'Sad', 'last_name': 'Novelist'}

with open('names.csv', 'w', newline='\n') as csv_file:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(csv_file,fieldnames=field_names)
    writer.writeheader()
    writer.writerow(character_banana)
    writer.writerow(character_octopus)
    writer.writerow(character_novelist)

with open('names.csv', 'r') as csv_file:
    read_file = csv_file.read()
    print(read_file)