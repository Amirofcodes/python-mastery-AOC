# 03_functions - Micro-drills for Function Definition, Arguments, and Scope
#
# Instructions:
# Complete each drill by typing the solution yourself to build muscle memory.
# Only use concepts from previous sections (primitive types, control flow) + functions.
# No data structures (lists, dicts) or advanced concepts yet.

# ===== DRILLS TO COMPLETE (1-12) =====

# Drill 1: Basic function definition, return values
# Prompt: Define a function called `calculate_area` that takes length and width as parameters.
# Return the area (length * width). Test it with length=5, width=3.
# TODO: Define the function and test it
def calculate_area(length, width):
    return (length * width)


print(calculate_area(5, 3))

# Drill 2: Function with string parameters, f-strings
# Prompt: Create a function `create_greeting` that takes a name and greeting (default="Hello").
# Return a formatted string: "{greeting}, {name}! Welcome!"
# Test with: create_greeting("Alice") and create_greeting("Bob", "Hi")
# TODO: Define the function and test it


def create_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}! Welcome!"


print(create_greeting("Alice"))
print(create_greeting("Bob", "Hi"))

# Drill 3: Function with conditionals, multiple returns
# Prompt: Write a function `get_grade` that takes a score (0-100).
# Return "A" for 90+, "B" for 80-89, "C" for 70-79, "D" for 60-69, "F" for below 60.
# Test with scores: 95, 82, 77, 65, 45
# TODO: Define the function and test it


def get_grade(score):
    if score > 100 or score < 0:
        return "Score must be between 0 and 100"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


for s in [95, 82, 77, 65, 45]:
    print(f"Score: {s} = Grade: {get_grade(s)}")


# Drill 4: Function with input validation, return tuple
# Prompt: Create `safe_divide` that takes two numbers.
# If divisor is 0, return (None, "Cannot divide by zero").
# Otherwise, return (result, "Success").
# Test with: (10, 2), (8, 0), (15, 3)
# TODO: Define the function and test it
def safe_divide(x, y):
    if y == 0:
        return (None, "Cannot divide by zero")
    else:
        result = x / y
        return (result, "Success")


print(safe_divide(10, 2))   # (5.0, "Success")
print(safe_divide(8, 0))    # (None, "Cannot divide by zero")
print(safe_divide(15, 3))   # (5.0, "Success")

# Drill 5: Function with loops, accumulator pattern
# Prompt: Write `sum_range` that takes start and end parameters.
# Use a for loop to calculate the sum of numbers from start to end (inclusive).
# Return the total. Test with: sum_range(1, 5) should return 15.
# TODO: Define the function and test it


def sum_range(start, end):
    total = 0
    for num in range(start, end+1):
        total += num
    return total


print(sum_range(1, 5))

# Drill 6: Function with while loop, user input
# Prompt: Create `get_positive_number` that asks user for a number.
# Keep asking until they enter a positive number (> 0).
# Return the valid number. Test by calling the function.
# TODO: Define the function and test it


def get_positive_number():
    while True:
        num = int(input("Enter number: "))
        if num > 0:
            return num


result = get_positive_number()

print(f"You entered: {result}")

# Drill 7: Function with default parameters, keyword arguments
# Prompt: Write `calculate_compound_interest` with parameters:
# principal, rate=0.05, time=1, compound_frequency=1
# Use formula: A = P(1 + r/n)^(nt) where n is compound_frequency
# Test with: calculate_compound_interest(1000), calculate_compound_interest(1000, rate=0.08, time=2)
# TODO: Define the function and test it


def calculate_compound_interest(principal, rate=0.05, time=1, compound_frequency=1):
    compound_interest = principal * \
        (1 + rate/compound_frequency) ** (compound_frequency * time)
    return compound_interest


print(calculate_compound_interest(1000))
print(calculate_compound_interest(1000, rate=0.08, time=2))

# Drill 8: Function with string operations, validation
# Prompt: Create `validate_email` that takes an email string.
# Return True if it contains both "@" and "." and has at least 5 characters.
# Return False otherwise. Test with: "user@site.com", "invalid", "a@b.co"
# TODO: Define the function and test it


def validate_email(email):
    if "@" in email and "." in email and len(email) >= 5:
        return True
    else:
        return False


print(validate_email("user@site.com"))
print(validate_email("invalid"))
print(validate_email("a@b.co"))


# Drill 9: Function scope, global variables
# Prompt: Create a global variable `call_counter = 0`.
# Write function `tracked_add` that takes two numbers, increments call_counter,
# and returns both the sum and the current call count as a tuple.
# Test by calling it 3 times with different numbers.
# TODO: Define global variable, function, and test it
call_counter = 0


def tracked_add(x, y):
    global call_counter
    result = x + y
    call_counter += 1
    return (result, call_counter)


print(tracked_add(2, 6))
print(tracked_add(5, 9))
print(tracked_add(4, 3))


# Drill 10: Nested function, closure concept
# Prompt: Write `create_multiplier` that takes a factor parameter.
# Inside it, define an inner function `multiply` that takes a number
# and returns number * factor. Return the inner function.
# Test: doubler = create_multiplier(2), then call doubler(5)
# TODO: Define the nested function and test it
def create_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply


doubler = create_multiplier(2)
result = doubler(5)
print(result)


# Drill 11: Function with *args, variable arguments
# Prompt: Create `find_maximum` that accepts any number of numeric arguments.
# Use a for loop to find and return the largest number.
# Handle the case of no arguments by returning None.
# Test with: find_maximum(1, 5, 3, 9, 2) and find_maximum()
# TODO: Define the function and test it

def find_maximum(*args):
    if not args:
        return None

    largest_number = args[0]
    for num in args[1:]:
        if num > largest_number:
            largest_number = num
    return largest_number


# Tests
print(find_maximum(1, 5, 3, 9, 2))  # 9
print(find_maximum())

# Python’s built-in max()


def find_max(*args):
    return max(args) if args else None


# Drill 12: Lambda function, simple calculator
# Prompt: Create lambda functions for basic math operations:
# add_lambda, subtract_lambda, multiply_lambda, divide_lambda
# Create a function `calculate` that takes two numbers and an operation lambda.
# Return the result of applying the operation to the numbers.
# Test all four operations.
# TODO: Define lambdas, calculate function, and test them

def add_lambda(a, b): return a + b
def subtract_lambda(a, b): return a - b
def multiply_lambda(a, b): return a * b
def divide_lambda(a, b): return a / b if b != 0 else None


def calculate(a, b, operation):
    return operation(a, b)


print(calculate(5, 2, add_lambda))
print(calculate(5, 2, subtract_lambda))
print(calculate(5, 2, multiply_lambda))
print(calculate(5, 2, divide_lambda))


# ===== END OF DRILLS =====
