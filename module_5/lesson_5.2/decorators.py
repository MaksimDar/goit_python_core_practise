# def greeting(variable):
#     print(f'Function greeting withn variable {variable}')
#     return False


# greeting('Maksym')

# def bot(func):
#     def inner_func(*args,**kwargs):
#         # print(args)
#         # print(kwargs)
#         print('Hello!')
#         result = func(*args,**kwargs)
#         print('Goodbye!')
#         return result

#     return inner_func

# bot_says = bot(greeting)
# print(bot_says(variable='Makar'))


########## decorator without args and kwargs 

def decorator(func):
    def inner_func(arg_1,arg_2):
        print('HELLLLLOOOOO')
        func(arg_1, arg_2)
        print('GOOODDBYEEEE')
    return inner_func

@decorator
def full_name(name, surname):
    print(f'My name is {name} {surname}')

full_name('Maksym', 'Dovhusha')



