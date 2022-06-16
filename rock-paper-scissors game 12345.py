import random

user_choices = [1, 2, 3]

while True:
    user_input = input("Enter your choices (1), (2), (3) or q to quit: \n").lower()
    if user_input == "q":
        break
    user_input = int(user_input)
    if user_input not in user_choices:
        continue

    random_number = random.randint(1, 3)
    computer_pick = (random_number)
    print(f"Computer picked {computer_pick}")

    if user_input == 1 and computer_pick == 3:
        print("you win")
    elif user_input == 2 and computer_pick == 1:
        print("you win")
    elif user_input == 3 and computer_pick == 2:
        print("you win")

    else:
        print("you lost !!!!")
if user_input == "q":
        print("Goodbye!!!!!!!")
