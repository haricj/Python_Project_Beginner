#
import random

while True:
    choice=str(input("Roll the dice y/n :"))
    if choice.lower()=='y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'({die1},{die2})')
    else:
        print('Pls try againy')
