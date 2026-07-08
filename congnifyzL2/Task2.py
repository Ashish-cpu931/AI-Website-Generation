# Number Guesser

import random

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
secret_number = random.randint(lower, upper)

print(f"\nI have selected a number between {lower} and {upper}.")
print("Try to guess it!")

attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
        break