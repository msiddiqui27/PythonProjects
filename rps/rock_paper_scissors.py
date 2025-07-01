# track how many times computer gets it correct vs how many times user gets it correct

import random

# need two variables

user_wins = 0
comp_wins = 0
options = ["rock", "paper", "scissors"]
# list: collection of elemetns

while True:
    user_input = input("Type Rock/Paper/Scissors. Type Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        # if whatever the user typed in doesnt exists in these three strings:
        print("Invalid input. Please type a valid input: ")
        continue

    randomNumber = random.randint(0,2)

    comp_guess = options[randomNumber]
    print("Computer Picked:", comp_guess)

    if user_input == comp_guess:
        print("No win. Let's go again!: ")
        comp_wins+=0
        user_wins+=0
        continue

    if (user_input == "rock" and comp_guess == "scissors") or\
        (user_input == "scissors" and comp_guess == "paper") or\
        (user_input == "paper" and comp_guess == "rock"):
        print("You win!")
        user_wins += 1

    else:
        print("Computer wins!")
        comp_wins += 1


print("You won", user_wins, "times.")
print("The computer won", comp_wins, "times.")
print("Game over. Goodbye!")
