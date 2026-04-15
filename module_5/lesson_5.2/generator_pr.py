def odd_number(limit):
    for value in range(limit):
        if value % 2:
            yield pow(value,2)

limit = 15
get_value = filter(lambda value: bool(value % 2), map(lambda x: pow(x,2), list(range(limit))))
print(get_value)
for result in zip(get_value, odd_number(limit)):
    print(result[0], result[1])



