def square_numbers():
    try:
        while True:
            number = yield
            square = number ** 2
            yield square
    except GeneratorExit:
        print('Generator is being closed')

if __name__ == '__main__':
    gen = square_numbers()
    next(gen)
    result = gen.send(20)
    print(f"Square root of {result}")

    next(gen)
    result = gen.send(15)
    print(f"Square root of {result}")
    gen.close()