# Scope: primitives, control flow, strings (+ import random)
# No try/except, no comprehensions, no classes no fuctions.
import random

print("******* Welcome to the number-guessing game *******")
num = random.randint(1, 20)
attempts = 0
while attempts < 6:
    guess = int(input("Enter your guess (1 to 20): "))
    if guess <= 0 or guess > 20:
        print("guess must be between 1 and 20")
    elif guess < num:
        attempts += 1
        print("Higher")
    elif guess > num:
        attempts += 1
        print("Lower")
    else:
        attempts += 1
        print(
            f"very good!!! {guess} is the correct guess. You used {attempts} attempts.")
        break
else:
    print("You've reach the max Allowed number of guesses")
