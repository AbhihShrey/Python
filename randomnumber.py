# Generate a random number
import random

random_number = random.randint(1, 10)
guess = -1

while guess != random_number:
    guess = int(input("Enter any number from 1 - 10: "))
    if guess != random_number:
        print("Sorry your guess was wrong, try again!")
        if guess > 10:
            print("The number is too big.")
    else:
        # If numbers are same then you win
        print("You win!")
