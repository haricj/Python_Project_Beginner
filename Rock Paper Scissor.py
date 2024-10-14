# Assign value to choices
print("rock = 1 , paper = 2 , scissor = 3")

import random

while True:
    # Computer makes a random choice
    comp = random.randint(1, 3)
    user = int(input("Choose your choice (1 for Rock, 2 for Paper, 3 for Scissor): "))

    # Check if user's input is valid
    if user not in [1, 2, 3]:
        print("Invalid input, please enter 1, 2, or 3.")
        continue

    # Display user and computer choices
    choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
    print(f"You chose {choices[user]}, Computer chose {choices[comp]}.")

    # Game logic
    if user == comp:
        print("It's a tie!")
    elif (user == 1 and comp == 3) or (user == 2 and comp == 1) or (user == 3 and comp == 2):
        print("You win!")
    else:
        print("Computer wins!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
