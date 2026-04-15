def generator(n) :
    for i in range(n):
        yield i

def sum_profit(num, func):
    return sum(func(num))

print(sum_profit(10, generator))