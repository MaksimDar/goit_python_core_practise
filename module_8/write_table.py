from csv import DictWriter
import json

file_json = 'users.json'
file_csv = 'users.csv'

def get_users():
    with open(file_json) as file:
        users = json.load(file)
    return users

def write_table():
    users = get_users()
    with open(file_csv,'w',encoding='utf-8',newline="") as file:
        fieldnames = users[0].keys()
        writer = DictWriter(file,delimiter=';',fieldnames=fieldnames)
        writer.writeheader()
        for row in users:
            writer.writerow(row)
        print("CSV table was created")


if __name__ == '__main__':
    write_table()