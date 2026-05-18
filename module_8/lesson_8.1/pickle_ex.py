# import pickle

# data = {'some_key': 12345678}

# with open('example.bin', 'wb') as file:
#     pickle.dump(data,file)

# data_types = pickle.dumps(data)
# print(data_types)

# with open('example.bin', 'rb') as file:
#     my_dict = pickle.load(file)

# print(my_dict)
# print(pickle.loads(data_types))


####### Second example
import pickle

FILENAME = 'user.dat'
users = [
    ['Tom', 28, True],
    ['Marina', 23, False],
    ['Oleg', 38, True]
]

with open(FILENAME, 'wb') as file:
    pickle.dump(users,file)

with open(FILENAME,'rb') as file:
    users_from_file = pickle.load(file)

    for user in users_from_file:
        print(f"Name {user[0]}\t\tAge {user[1]}\t\tDriving License {user[2]}")
