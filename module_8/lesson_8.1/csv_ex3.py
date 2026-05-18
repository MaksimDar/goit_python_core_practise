import csv

FILENAME = 'countries.csv'
countries_code = {}

with open(FILENAME, 'r') as file:
    reader = csv.reader(file)

    for country in reader:
        countries_code[country[0]] = country[1]
    countries_code.pop("Code")

print(countries_code['AD'])
print(countries_code.get('UA'))
print(countries_code.get('ES'))