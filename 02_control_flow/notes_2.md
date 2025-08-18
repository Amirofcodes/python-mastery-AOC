# CONTROL FLOW - MASTERING CONDITIONAL LOGIC & LOOPS

# Control Flow = The order in which statements are executed in a program

# Allows programs to make decisions and repeat actions based on conditions

---

# COMPARISON OPERATORS

# Used to compare values and return True or False

```python
# Basic comparison operators
x = 5
y = 10

print(x == y)   # Equal to: False
print(x != y)   # Not equal to: True
print(x < y)    # Less than: True
print(x > y)    # Greater than: False
print(x <= y)   # Less than or equal to: True
print(x >= y)   # Greater than or equal to: False
```

# String comparisons (lexicographical order)

```python
name1 = "Alice"
name2 = "Bob"
print(name1 < name2)  # True (A comes before B)
print(name1 == name2) # False
```

---

# CONDITIONAL STATEMENTS (if/elif/else)

# if statement - executes code only if condition is True

```python
age = 18

if age >= 18:
    print("You are an adult")
    print("You can vote")
```

# if/else statement - executes different code based on condition

```python
age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

# if/elif/else statement - multiple conditions

```python
age = 25

if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")
```

# Nested if statements

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
```

---

# TERNARY OPERATOR (Conditional Expression)

# Shorthand way to write simple if/else statements

```python
age = 20

# Traditional if/else
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator (one-liner)
status = "adult" if age >= 18 else "minor"

print(f"You are an {status}")

# Another example
number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result}")
```

---

# LOGICAL OPERATORS

# Combine multiple conditions

```python
# AND operator - both conditions must be True
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

# OR operator - at least one condition must be True
is_student = True
is_employed = False

if is_student or is_employed:
    print("You have a discount")

# NOT operator - negates the condition
is_weekend = False

if not is_weekend:
    print("It's a weekday")
```

# Complex logical expressions

```python
age = 20
has_license = True
has_car = False

# Can drive if: (18+ AND has license) OR has car
can_drive = (age >= 18 and has_license) or has_car
print(f"Can drive: {can_drive}")
```

---

# SHORT-CIRCUIT EVALUATION

# Python stops evaluating as soon as it knows the result

```python
# AND short-circuit: stops at first False
x = 5
y = 0

# This won't cause division by zero error
if y != 0 and x / y > 2:
    print("Condition met")

# OR short-circuit: stops at first True
name = "John"
age = 25

# This won't cause error if name is empty
if name or age > 18:
    print("Valid user")
```

# Practical example - safe division

```python
numerator = 10
denominator = 0

# Safe division using short-circuit
if denominator != 0 and numerator / denominator > 2:
    print("Result is greater than 2")
else:
    print("Cannot divide or result is not greater than 2")
```

---

# CHAINING COMPARISON OPERATORS

# Python allows chaining multiple comparisons

```python
age = 25

# Traditional way
if age >= 18 and age <= 65:
    print("Working age")

# Chained comparison (more readable)
if 18 <= age <= 65:
    print("Working age")

# Multiple chained comparisons
x = 5
y = 10
z = 15

if x < y < z:
    print("Numbers are in ascending order")

# Temperature range example
temp = 22
if 20 <= temp <= 25:
    print("Comfortable temperature")
```

---

# FOR LOOPS

# Iterate over sequences (strings, lists, ranges)

```python
# Loop through a string
name = "Python"
for letter in name:
    print(letter)

# Loop through a range
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Loop with start and end
for i in range(1, 6):
    print(i)  # Prints 1, 2, 3, 4, 5

# Loop with step
for i in range(0, 10, 2):
    print(i)  # Prints 0, 2, 4, 6, 8
```

# range() function variations

```python
# range(stop) - starts from 0
for i in range(3):
    print(i)  # 0, 1, 2

# range(start, stop) - starts from start
for i in range(2, 5):
    print(i)  # 2, 3, 4

# range(start, stop, step) - with step
for i in range(0, 10, 3):
    print(i)  # 0, 3, 6, 9
```

---

# FOR-ELSE STATEMENT

# else block executes when loop completes normally (no break)

```python
# Search for a number in a list
numbers = [1, 3, 5, 7, 9]
search_for = 4

for num in numbers:
    if num == search_for:
        print(f"Found {search_for}!")
        break
else:
    print(f"{search_for} not found in the list")

# Another example - password validation
password = "secret123"
attempts = ["wrong", "also_wrong", "secret123", "another_wrong"]

for attempt in attempts:
    if attempt == password:
        print("Access granted!")
        break
else:
    print("Access denied - too many wrong attempts")
```

---

# NESTED LOOPS

# Loops inside loops

```python
# Multiplication table (3x3)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each row

# Pattern printing
for i in range(3):
    for j in range(i + 1):
        print("*", end="")
    print()  # New line after each row
```

# Practical example - coordinate grid

```python
# Print coordinates (0,0) to (2,2)
for x in range(3):
    for y in range(3):
        print(f"({x},{y})", end=" ")
    print()  # New line after each row
```

---

# WHILE LOOPS

# Repeat code while condition is True

```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# User input validation
password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Wrong password. {max_attempts - attempts} attempts left")
```

# Counter-controlled while loop

```python
# Count down from 5
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")
```

---

# INFINITE LOOPS

# Loops that run forever (usually with break to exit)

```python
# Game loop example
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    print(f"You entered: {user_input}")

# Menu system
while True:
    print("\n1. Option 1")
    print("2. Option 2")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("You chose option 1")
    elif choice == "2":
        print("You chose option 2")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```

---

# BREAK AND CONTINUE

# Control flow within loops

```python
# break - exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# continue - skip to next iteration
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)  # Prints 1, 3, 5, 7, 9
```

# Practical examples

```python
# Find first negative number
numbers = [1, 3, -2, 5, 7]
for num in numbers:
    if num < 0:
        print(f"First negative number: {num}")
        break

# Skip processing for invalid data
scores = [85, 92, -1, 78, 95, -1, 88]
for score in scores:
    if score == -1:  # Invalid score
        continue
    print(f"Processing score: {score}")
```

---

# ITERABLES

# Objects that can be iterated over in loops

```python
# String iteration
for char in "Hello":
    print(char)

# List iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Tuple iteration
coordinates = (1, 2), (3, 4), (5, 6)
for x, y in coordinates:
    print(f"Point: ({x}, {y})")

# Dictionary iteration
person = {"name": "John", "age": 30, "city": "NYC"}
for key in person:
    print(f"{key}: {person[key]}")

# Dictionary items iteration
for key, value in person.items():
    print(f"{key}: {value}")
```

---

# MEMBERSHIP TESTING

# Check if item exists in iterable

```python
# Using 'in' operator
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("orange" in fruits)  # False

# String membership
text = "Hello World"
print("Hello" in text)  # True
print("Python" in text)  # False

# Practical example - user validation
allowed_users = ["admin", "user1", "user2"]
username = input("Enter username: ")

if username in allowed_users:
    print("Access granted")
else:
    print("Access denied")
```

---

# KEY CONCEPTS SUMMARY

## Comparison Operators

- `==` - Equal to
- `!=` - Not equal to
- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal to
- `>=` - Greater than or equal to

## Logical Operators

- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `not` - Negates the condition

## Control Flow Structures

- `if/elif/else` - Conditional execution
- `for` - Iterate over sequences
- `while` - Repeat while condition is True
- `break` - Exit loop immediately
- `continue` - Skip to next iteration

## Loop Patterns

- `for-else` - Execute else when loop completes normally
- `while True` - Infinite loop with break
- Nested loops - Loops inside loops

## Best Practices

- Use meaningful variable names
- Keep conditions simple and readable
- Use break/continue sparingly
- Avoid infinite loops without exit conditions
- Use chained comparisons for ranges
- Leverage short-circuit evaluation for safety

## Common Patterns

- Input validation loops
- Search patterns with for-else
- Menu systems with while True
- Counter-controlled loops
- Nested loops for grids/tables
