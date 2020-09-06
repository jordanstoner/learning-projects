import random

# Initialize Variables
number = random.randint(1,100)

guess = int(input("Guess a number between 1 and 100!: "))

while guess != number:
    if guess < number:
        guess = int(input("Higher!: "))
    else:
        guess = int(input("Lower!: "))

print(f"You got it! The number was {number}!")