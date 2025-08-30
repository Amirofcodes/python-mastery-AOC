# 02_control_flow - Micro-drills for Conditionals, Loops, and Logical Operators
#
# Instructions:
# 1. Copy this template to drills.py to start fresh practice
# 2. Complete each drill by typing the solution yourself to build muscle memory
# 3. Only use primitive types and control flow concepts from notes_2.md
# 4. NO imports allowed yet - time/random will be introduced in later sections
# 5. Test each drill before moving to the next
#
# Notes: See notes_2.md for detailed explanations of all concepts

# ===== CORE DRILLS (Required) =====

# Drill 1: Comparison operators, conditional statements, chaining
# Prompt: Ask user's age, print Teen/Adult/Senior using `if/elif/else` with chained comparison (13 <= age <= 19).
# - Print "Teen" if age is between 13 and 17 (inclusive of 13, exclusive of 18)
# - Print "Adult" if age is between 18 and 50 (inclusive)
# - Print "Senior" if age is greater than 50
# - Otherwise, print "Child"
# Core concept: Comparison operators · Conditional statements · Chaining
# TODO: Use if/elif/else with chained comparisons


# Drill 2: Ternary operator
# Prompt: Ask user to enter a number. Use one-liner ternary to print "even" or "odd".
# Use modulus (%) to determine evenness.
# Core concept: Ternary operator
# TODO: Use "even" if num % 2 == 0 else "odd" syntax


# Drill 3: Logical operators, short-circuit evaluation
# Prompt: Given two numbers, safely divide first by second. If divisor is 0, use `and` short-circuit
# to skip division; print result or "undefined".
# Core concept: Logical operators · Short-circuit evaluation
# TODO: Use divisor != 0 and ... pattern to avoid division by zero


# Drill 4: for loop, break, for-else
# Prompt: Set fixed password "ABC123". Allow user up to 5 attempts to guess it.
# Use for loop. If correct, print "Access granted" and break.
# If all attempts fail, print "Locked out" using for-else.
# Core concept: `for` loop · `break` · `for-else`
# TODO: Use for i in range(5) with break and else


# Drill 5: Nested loops, range() function
# Prompt: Print 5×5 multiplication table (each row one line) using nested `for` loops with `range()`.
# Core concept: Nested loops · `range()` function
# TODO: Use nested for i in range(1,6) and for j in range(1,6)


# Drill 6: for-else, comparisons, break
# Prompt: From numbers [7, 2, 9, 4, 0] find first value ≥ 8. Use `break`;
# `for-else` prints "No match" if not found.
# Core concept: `for-else` · Comparisons · `break`
# TODO: Loop through list, break on first match, else clause for no match


# Drill 7: while loop, infinite loops, break (NO IMPORTS)
# Prompt: Build number-guessing game. Set target = 7 (no random yet).
# User keeps guessing until correct. Count attempts; break on success; print win message.
# Core concept: `while` loop · Infinite loops · `break`
# TODO: Use while True loop with break condition


# Drill 8: Iterables, string iteration, membership
# Prompt: Ask for text and count vowels using `for char in text:` loop with membership testing.
# Check for vowels: a, e, i, o, u (case-insensitive).
# Core concept: Iterables · String iteration · Membership
# TODO: Use for char in text with char.lower() in vowels


# Drill 9: Conditional statements, multiple assignment
# Prompt: Given two numbers a=3, b=8 — swap them only if b is larger using conditional logic.
# Print "Swapped" if swap occurred, otherwise "Not swapped".
# Core concept: Conditional statements · Multiple assignment
# TODO: Use if b > a with tuple unpacking a, b = b, a


# Drill 10: while loop, conditional logic, arithmetic
# Prompt: Start from user-provided number. Print first 10 terms of Collatz sequence:
# if even divide by 2, if odd multiply by 3 and add 1. Use while loop and conditional logic.
# Core concept: `while` loop · Conditional logic · Arithmetic
# TODO: Use counter and while count < 10 with if/else for even/odd


# Drill 11: Chained comparison, ternary operator
# Prompt: Ask for temperature, print "Comfy" if `20 <= temp <= 26`,
# else "Too hot" or "Too cold" using ternary.
# Core concept: Chained comparison · Ternary operator
# TODO: Use chained comparison in ternary expression


# Drill 12: Logical operators, modulus, XOR logic
# Prompt: Loop 1..100, print numbers divisible by 3 or 5 but not both (XOR logic) using modulus.
# Core concept: Logical operators · Modulus · XOR logic
# TODO: Use (x % 3 == 0) != (x % 5 == 0) for exclusive or


# Drill 13: for-else, reverse range
# Prompt: Use `range(10, -1, -1)` for countdown 10 to 0. After loop, print "Blast off!" via `for-else`.
# Core concept: `for-else` · Reverse range
# TODO: Use range with negative step and for-else construct


# ===== END OF DRILLS =====
