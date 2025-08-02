# 02_control_flow - Micro-drills for Conditionals, Loops, and Logical Operators
#
# Instructions: Complete each drill by typing the solution yourself.
# Only use primitive types and control flow concepts listed for each drill.
# No functions or advanced structures unless otherwise noted.

# ===== DRILLS TO COMPLETE (1-13) =====

# Drill 1: Comparison operators, conditional statements, chaining
# Prompt: Ask the user for their age. Use if/elif/else and chained comparison operators to classify their age group:
# - Print "Teen" if age is between 13 and 17 (inclusive of 13, exclusive of 18)
# - Print "Adult" if age is between 18 and 50 (inclusive)
# - Print "Senior" if age is greater than 50
# - Otherwise, print "Child"

import time
import random
user_age = int(input("Enter your age: "))

if 13 <= user_age < 18:
    print("Teen")
elif 18 <= user_age <= 50:
    print("Adult")
elif user_age > 50:
    print("Senior")
else:
    print("Child")

# Drill 2: Ternary operator
# Prompt: Ask the user to enter a number.
# Use a one-line if/else (ternary) to print "even" if the number is even, otherwise print "odd".
# Use modulus (%) to determine evenness.
num = int(input("Enter a number: "))
print("even" if num % 2 == 0 else "odd")

# Drill 3: Logical operators, short-circuit evaluation
# Prompt: Given two numbers, print the result of dividing the first by the second.
# If the divisor is zero, print "undefined" instead of crashing.
# Use logical operators (like "and") to short-circuit and avoid a division by zero error.
num_1 = 10
divisor = 0

if divisor != 0 and num_1 / divisor:
    result = num_1 / divisor
    print(result)
else:
    print("undefined")

# Drill 4: for loop, break, for-else
# Prompt: Set a fixed password (e.g., "ABC123"). Allow the user up to 5 attempts to guess it.
# Use a for loop. If the user enters the correct password, print "Access granted" and exit the loop.
# If all attempts fail, print "Locked out" after the loop (using for-else).
password = "ABC123"

for x in range(5):
    attempt = input("Enter password: ")
    if attempt == password:
        print("Access granted")
        break
    else:
        print("locked out")

# Drill 5: Nested loops, range() function
# Prompt: Use nested for loops to print a 5 by 5 multiplication table.
# Each row should be on its own line; use the range() function for both loops.
for x in range(1, 6):
    for y in range(1, 6):
        print(x * y, end=" ")
    print()


# Drill 6: for-else, comparisons, break
# Prompt: Given a list of numbers, loop through and find the first value greater than or equal to 8.
# If such a number is found, print it and stop the loop.
# If not found, print "No match" after the loop using for-else.
numbers = [7, 2, 9, 4, 0]

for number in numbers:
    if number >= 8:
        print(f"first value found: {number}")
        break
else:
    print("No match")

# Drill 7: while loop, infinite loops, break
# Prompt: Build a number-guessing game where the computer randomly picks a number between 1 and 10.
# The user keeps guessing until they get it right.
# Count the number of attempts. After a correct guess, print a congratulatory message with the attempt count.

# Drill 7.1: Standard approach
# Prompt: Same as Drill 7, but after each guess, print a hint ("Too high" or "Too low") to guide the user.
target = random.randint(1, 10)  # Random number 1-10
attempts = 0

print("Guess the number (1-10):")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == target:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
    elif guess < target:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# Drill 7.2: Alternative approach
# Prompt: Given a predefined list of numbers, prompt the user to guess a number until they pick one from the list.
# Count and print the number of incorrect guesses before a correct one.
numbers = [11, 234, 387, 46, 53, 61, 79, 83, 39, 710]
attempts = 0

print("******* Welcome to the number-guessing game *******")

while True:
    guess_number = int(input("Enter a number: "))
    if guess_number not in numbers:
        attempts += 1
    else:
        print(f"{guess_number} is a good guess")
        print(f"Number of incorrect attempts: {attempts}")
        break


# Drill 8: Iterables, string iteration, membership
# Prompt: Ask the user to enter a line of text.
# Loop through the text and count how many vowels it contains (a, e, i, o, u, y).
# Print the total vowel count.
vowels = ('a', 'e', 'i', 'o', 'u', 'y')
count = 0

text = input("Enter a text: ").strip()

for x in text:
    if x not in vowels:
        continue
    else:
        count += 1
print(f"You have {count} vowels in your text")


# Drill 9: Conditional statements, multiple assignment
# Prompt: Given two numbers a and b, swap their values only if b is greater than a.
# Print "Swapped" if a swap occurred, otherwise print "Not swapped".

# Drill 9.1: Standard approach
# Prompt: Same as above, but use a while loop that swaps and immediately breaks if b > a; otherwise print "Not swapped".
a = 3
b = 8

if b > a:
    a, b = b, a
    print("Swapped")
else:
    print("Not swapped")

# Drill 9.2: Alternative approach
# Prompt: Same as above, but use a while loop that swaps and immediately breaks if b > a; otherwise print "Not swapped".
a = 39
b = 8

while b > a:
    a, b = b, a
    print("Swapped")
    break
else:
    print("Not swapped")


# Drill 10: while loop, conditional logic, arithmetic
# Prompt: Start from a number provided by the user.
# Print the first 10 terms of the Collatz sequence (if even, divide by 2; if odd, multiply by 3 and add 1).
# Use a while loop and conditional logic to implement the rule.
n = int(input("Enter a number: "))

count = 0

while count < 10:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    count += 1


# Drill 11: Chained comparison, ternary operator
# Prompt: Ask the user to enter the room temperature as an integer.
# Print "Comfy" if the temperature is between 20 and 26 (inclusive).
# Otherwise, print "Too cold" if less than 20, or "Too hot" if greater than 26.
# Use a chained comparison and a one-line ternary for the output.
temp = int(input("Enter temperature: "))

print("Comfy" if 20 <= temp <= 26 else "Too cold" if temp < 20 else "Too hot")


# Drill 12: Logical operators, modulus, XOR logic
# Prompt: Loop through numbers from 1 to 100 (inclusive).
# For each number, print it only if it is divisible by 3 or by 5, but not both at the same time.
# Use modulus (%) to test divisibility and logical operators to enforce the condition (exclusive or logic).
for x in range(1, 101):
    if (x % 3 == 0) != (x % 5 == 0):
        print(x)

# Drill 13: for-else, reverse range
# Prompt: Use a for loop and range(10, -1, -1) to print a countdown from 10 to 0 (one number per line).
# After the loop finishes, print "Blast off!" using the for-else construct.

for x in range(10, -1, -1):
    print(x)
    time.sleep(1)  # Pause for 1 second
else:
    print("Blast off!")
