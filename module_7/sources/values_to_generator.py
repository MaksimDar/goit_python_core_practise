def generator():
    received = yield 'Ready to work'
    yield f'Hello {received}!'

gen = generator()
print(next(gen))
print(gen.send('Maksym'))
