counter = 0

while counter < 4:
    user_input = input("Enter your value: ")
    counter += 1
    if user_input == "exit":
        break
    else:
        print(f"Your input is {user_input}")
