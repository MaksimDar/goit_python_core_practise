
while True:
    age = input("What is your age? ")
    try:
        age = int(age)
        if age > 18:
            print("Access allowed ")
            break
        else:
            print("Access denied ")
            break
    except ValueError:
        print(f"{age} is not a decimal number. Please, write a decimal number")
    finally:
        print("-" * 30)
    