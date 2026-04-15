###lambda map
# names = ['maksym', 'makar', 'stepan', 'sasha']
# normal_name = list(map(str.title, names))
# print(normal_name)

# def number_square(value):
#     return pow(value,2)

# square_numbers = list(map(number_square, [i for i in range(10)]))
# print(square_numbers)

#### lambda filter 

numbers = [100,-3,0,-9,19,29]

positive_numbers = list(filter(lambda ele: ele > 0, numbers))
print(positive_numbers)