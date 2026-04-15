# def greeting(variable, args):
#     print(f'Function greeting withn variable {variable}, {args}')


# greeting('Test', 'Passed')

#### alternative code in currying

# def outer_func(variable):
#     def inner_func(args):
#         print(f'Function greeting withn variable {variable}, {args}')
#     return inner_func

# currying = outer_func('Test')
# currying('Passed')
# currying('Failed')


def outer_func(value):
    def inner_func(number):
        return value * number
    return inner_func

multiply_eight = outer_func(8)
print(multiply_eight(5))
print(multiply_eight(25))