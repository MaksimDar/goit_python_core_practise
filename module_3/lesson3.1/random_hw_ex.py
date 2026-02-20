from random import randint, sample
min_value = -10
max_value = 10
length = 10

result_array = set()

while len(result_array) != length:
    result_array.add(randint(min_value,max_value))

print(sorted(list(result_array)))

print(sorted(sample(range(min_value, max_value), length)))

