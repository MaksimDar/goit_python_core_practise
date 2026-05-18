import csv
from pprint import pprint

FILENAME = 'table.csv'


with open(FILENAME, 'w', newline="") as file:
    writer = csv.writer(file)
    for i in range(1,21):
        writer.writerow([i,pow(i,2),pow(i,3)])

with open(FILENAME,'r') as file:
    reader = csv.reader(file)
    result = list()

    for row in reader:
        result.append(row)

print(result)
pprint(result)