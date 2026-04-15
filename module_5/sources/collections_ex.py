# from collections import namedtuple

# # person_1 = ('Maksym', 30, 'Kyiv')

# # print(f'Name: {person_1[0]}, age: {person_1[1]}, city: {person_1[2]}')
# #########
# Person = namedtuple('Person', ['name', 'age', 'city'])
# person1 = Person('Maksym', 20, 'Kyiv')

# print(f'Name: {person1.name}, age: {person1.age}, city: {person1.city}')

############# Counter

# text = """Hello my dear friend! Welcome to sources folder. I wish you good luck"""

# def count_char(text):
#     count_dict = {}
#     for item in text:
#         num = count_dict.get(item)
#         if num:
#             count_dict[item] =  num + 1
#         else:
#             count_dict[item] = 1
#     print(count_dict)

# count_char(text)

#########=============>>>>>> analogy 

# from collections import Counter
# text = """Hello my dear friend! Welcome to sources folder. I wish you good luck"""
# counter = Counter(text)
# # print(counter)

# # print(counter.most_common(4))

# print(sorted(counter))