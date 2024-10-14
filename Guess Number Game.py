
import random

real=random.randint(1,100)

while True:
        guess=input("Guess the number between 1 and 100: ")
        
        try:
                guess=int(guess)

        except ValueError:
                print("Please entera valid number")
                continue

        if real==guess:
                print("Correct answer")
                exit()
        elif real  > guess :
                print("Too Low")
        else:
                print("Too High")