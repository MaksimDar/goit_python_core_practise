def get_numbers(x):
    numbers = []

    for i in range(x):
        num = i ** 2
        if num % 2:
            numbers.append(num)
    print(numbers)

def get_numbers_short(x):
    numbers = [i** 2 for i in range(x) if not i % 2 == 0]
    print(numbers)
    



get_numbers(8)
get_numbers_short(8)
