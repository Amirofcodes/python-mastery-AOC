# 03_functions - Micro-drills for Function Definition, Arguments, and Scope
#
# Instructions:
# 1. Copy this template to drills.py to start fresh practice
# 2. Complete each drill by typing the solution yourself to build muscle memory
# 3. Only use concepts from previous sections (primitive types, control flow) + functions
# 4. Test each drill before moving to the next
#
# Notes: See notes_3.md for detailed explanations of all concepts

# ===== CORE DRILLS (Required) =====

# Drill 1: Basic function definition, return values
# Prompt: Define a function called `calculate_area` that takes length and width as parameters.
# Return the area (length * width). Test it with length=5, width=3.
# Core concept: Function definition · Return values
# TODO: Define the function and test it


# Drill 2: Function with default parameters, string formatting
# Prompt: Create a function `make_greeting` that takes a name and greeting (default="Hello").
# Return a formatted string: "{greeting}, {name}! Welcome!"
# Test with: make_greeting("Alice") and make_greeting("Bob", "Hi")
# Core concept: Default parameters · String formatting
# TODO: Define the function and test it


# Drill 3: Function with conditionals, multiple returns
# Prompt: Write a function `get_grade` that takes a score (0-100).
# Return "A" for 90+, "B" for 80-89, "C" for 70-79, "D" for 60-69, "F" for below 60.
# Test with scores: 95, 82, 77, 65, 45
# Core concept: Multiple returns · Conditionals in functions
# TODO: Define the function and test it


# Drill 4: Function with input validation, return tuple
# Prompt: Create `safe_divide` that takes two numbers.
# If divisor is 0, return (None, "Cannot divide by zero").
# Otherwise, return (result, "Success").
# Test with: (10, 2), (8, 0), (15, 3)
# Core concept: Input validation · Return tuples
# TODO: Define the function and test it


# Drill 5: Function with loops, accumulator pattern
# Prompt: Write `sum_range` that takes start and end parameters.
# Use a for loop to calculate the sum of numbers from start to end (inclusive).
# Return the total. Test with: sum_range(1, 5) should return 15.
# Core concept: Functions with loops · Accumulator pattern
# TODO: Define the function and test it


# Drill 6: Function with user input, while loops
# Prompt: Create `get_positive_number` that asks user for a number.
# Keep asking until they enter a positive number (> 0).
# Return the valid number. Test by calling the function.
# Core concept: Functions with user input · While loops
# TODO: Define the function and test it


# Drill 7: Multiple default parameters, keyword arguments
# Prompt: Write `calculate_interest` with parameters:
# principal, rate=0.05, years=1
# Use formula: result = principal * (1 + rate) ** years
# Test with: calculate_interest(1000), calculate_interest(1000, rate=0.08, years=2)
# Core concept: Multiple default parameters · Keyword arguments
# TODO: Define the function and test it


# Drill 8: String validation, boolean returns
# Prompt: Create `validate_email` that takes an email string.
# Return True if it contains both "@" and "." and has at least 5 characters.
# Return False otherwise. Test with: "user@site.com", "invalid", "a@b.co"
# Core concept: String validation · Boolean returns
# TODO: Define the function and test it


# Drill 9: Function scope, global variables
# Prompt: Create a global variable `call_count = 0`.
# Write function `tracked_add` that takes two numbers, increments call_count,
# and returns both the sum and the current call count as a tuple.
# Test by calling it 3 times with different numbers.
# Core concept: Global variables · Function scope
# TODO: Define global variable, function, and test it


# ===== ADVANCED DRILLS (Optional - Preview) =====
# These preview concepts covered fully in later sections

# Drill 10: Nested functions, closures - PREVIEW
# Note: This previews closures, covered fully in Section 08 (Advanced Functions)
# Prompt: Write `create_multiplier` that takes a factor parameter.
# Inside it, define an inner function `multiply` that takes a number
# and returns number * factor. Return the inner function.
# Test: doubler = create_multiplier(2), then call doubler(5)
# Advanced concept: Nested functions · Closures
# TODO: Research closures and implement (optional challenge)


# Drill 11: Variable arguments (*args) - PREVIEW
# Note: This previews *args, covered fully in Section 08 (Advanced Functions)
# Prompt: Create `find_maximum` that accepts any number of numeric arguments.
# Use a for loop to find and return the largest number.
# Handle the case of no arguments by returning None.
# Test with: find_maximum(1, 5, 3, 9, 2) and find_maximum()
# Advanced concept: Variable arguments (*args)
# TODO: Research *args and implement (optional challenge)


# Drill 12: Lambda functions - PREVIEW
# Note: This previews lambdas, covered fully in Section 09 (Functional Programming)
# Prompt: Create lambda functions for basic math operations:
# add_lambda, subtract_lambda, multiply_lambda, divide_lambda
# Create a function `calculate` that takes two numbers and an operation lambda.
# Return the result of applying the operation to the numbers.
# Test all four operations.
# Advanced concept: Lambda functions · Higher-order functions
# TODO: Research lambdas and implement (optional challenge)


# ===== END OF DRILLS =====
