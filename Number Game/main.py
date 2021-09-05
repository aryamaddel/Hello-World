import random

while True:
    random_number = random.randint(0, 10)
    for i in range(3):
        usr_choice = int(input("Enter your choice"))
        if i != 2:
            if usr_choice == random_number:
                print("You Won")
                exit()
            else:
                print("Try again")
        elif i == 2:
            if usr_choice == random_number:
                print("You Won")
                exit()
            else:
                print("You Lost")
    if input("to exit type 'exit'") == "exit":
        exit()
