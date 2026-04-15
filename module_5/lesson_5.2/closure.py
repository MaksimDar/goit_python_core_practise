message = 'Goodbye!'

def outer_func(name):
    message = 'Hello'
    def inner_function(message,name):
        return f'{message} {name}'
    return inner_function(message, name)

print(outer_func('Maksym'))