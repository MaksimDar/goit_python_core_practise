def sum(a,b):
    return a+b

def minus(a,b):
    return a-b

def power(a):
    return pow(a,2)

def operation(operator):
    if operator == '+':
        return sum
    if operator == '-':
        return minus
    if operator == '*':
        return power
# new_sum = sum

# print(new_sum(3,5))

# def operation(a,b,func):
#     return func(a,b)

# print(operation(4,6,sum))


####

choose_operator = operation('+')
print(choose_operator(6,5))

choose_operator = operation('-')
print(choose_operator(6,5))

choose_operator = operation('*')
print(choose_operator(6))