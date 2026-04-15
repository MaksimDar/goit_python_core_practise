# def greeting(mode):
#     if mode == 'm':
#         return hello_male
#     elif mode == 'f':
#         return hello_female

# def hello_male(name):
#     print(f"Mr. {name}")

# def hello_female(name):
#     print(f"Mrs. {name}")

# def main():
#     greetina_male = greeting('m')
#     greetina_female = greeting('f')

#     greetina_male('Maksym')
#     greetina_female('Tetiana')


# if __name__ == '__main__':
#     main()

########=========>>> more readable alternative 
def hello_male(name):
    print(f"Mr. {name}")

def hello_female(name):
    print(f"Mrs. {name}")

def hello_dear(name):
    print(f"DEAR {name}")

MODES = {
    'm': hello_male,
    'f': hello_female,
    'd': hello_dear
}


def greeting(mode):
    return MODES[mode]

def main():
    greetina_male = greeting('m')
    greetina_female = greeting('f')
    greeting_dear = greeting('d')

    greetina_male('Maksym')
    greetina_female('Tetiana')
    greeting_dear('Stepan')


if __name__ == '__main__':
    main()