# 02 · Control Flow - Comprehensive Decision Making & Iteration Guide

Master Python's control structures through complete understanding of **all the different ways** to make decisions, repeat actions, and control program execution flow.

---

## **Mental Model: Program Flow Control**

- **Conditionals**: Make decisions based on conditions (if/elif/else, ternary)
- **Loops**: Repeat actions while conditions are met (for, while, nested)
- **Control Statements**: Modify loop behavior (break, continue, else)
- **Logical Operations**: Combine and manipulate boolean values (and, or, not)
- **Flow Patterns**: Common structures for real-world programming scenarios

---

# **COMPARISON OPERATORS - Foundation of Decision Making**

## **1. Basic Comparison Operators - All Types**

```python
# Numeric comparisons
x = 5
y = 10

# Equality and inequality
equal = (x == y)        # False
not_equal = (x != y)    # True

# Order comparisons
less_than = (x < y)     # True
greater_than = (x > y)  # False
less_equal = (x <= y)   # True
greater_equal = (x >= y) # False

# Identity comparison (same object)
same_object = (x is y)  # False
different_object = (x is not y)  # True
```

## **2. String Comparisons - Lexicographical Order**

```python
# String comparison rules
name1 = "Alice"
name2 = "Bob"
name3 = "alice"  # Different case

# Basic comparisons
print(name1 < name2)   # True (A comes before B)
print(name1 == name2)  # False
print(name1 > name2)   # False

# Case sensitivity matters
print(name1 < name3)   # False (uppercase comes before lowercase)
print(name1.lower() < name3.lower())  # True (case-insensitive)

# Empty string comparisons
empty = ""
print(empty < "a")     # True (empty string is smallest)
print(empty == "")     # True
```

## **3. Advanced Comparison Patterns**

```python
# Multiple value comparisons
a, b, c = 1, 2, 3

# Chained comparisons (Python feature)
in_order = (a < b < c)           # True (equivalent to a < b and b < c)
range_check = (0 <= a <= 10)     # True (a is between 0 and 10)
descending = (c > b > a)          # True (c > b and b > a)

# Type-aware comparisons
mixed = [1, "hello", 3.14]
# print(1 < "hello")  # TypeError: '<' not supported between 'int' and 'str'

# Safe comparison functions
def safe_compare(a, b):
    """Compare values safely, handling different types"""
    try:
        return a < b
    except TypeError:
        # Convert to strings for comparison
        return str(a) < str(b)

print(safe_compare(1, "hello"))  # True ("1" < "hello")
```

---

# **CONDITIONAL STATEMENTS - Decision Making Mastery**

## **1. Basic if Statement - Single Condition**

```python
# Simple if statement
age = 18

if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You can drive")

# Multiple statements in if block
temperature = 25
if temperature > 20:
    print("It's warm")
    print("Wear light clothes")
    print("Stay hydrated")
```

## **2. if/else Statement - Two-Way Decision**

```python
# Basic if/else
age = 16

if age >= 18:
    print("You are an adult")
    print("You can vote")
else:
    print("You are a minor")
    print("You cannot vote")

# Practical example - password validation
password = "secret123"
if len(password) >= 8:
    print("Password is valid")
else:
    print("Password too short - minimum 8 characters")

# Multiple conditions in if/else
score = 85
if score >= 90:
    grade = "A"
    print(f"Excellent! Grade: {grade}")
else:
    grade = "B or lower"
    print(f"Good effort! Grade: {grade}")
```

## **3. if/elif/else Statement - Multiple Conditions**

```python
# Age categorization with multiple conditions
age = 25

if age < 13:
    category = "child"
    print(f"You are a {category}")
    print("Enjoy your childhood!")
elif age < 18:
    category = "teenager"
    print(f"You are a {category}")
    print("Teenage years are exciting!")
elif age < 65:
    category = "adult"
    print(f"You are a {category}")
    print("Welcome to adulthood!")
else:
    category = "senior"
    print(f"You are a {category}")
    print("Wisdom comes with age!")

# Grade calculation with ranges
score = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Practical example - user role assignment
user_type = "premium"
account_age = 2

if user_type == "admin":
    access_level = "full"
elif user_type == "premium" and account_age >= 1:
    access_level = "extended"
elif user_type == "premium":
    access_level = "standard"
else:
    access_level = "basic"

print(f"Access level: {access_level}")
```

## **4. Nested if Statements - Complex Decision Trees**

```python
# Driving eligibility with nested conditions
age = 20
has_license = True
has_car = False
is_weekend = True

if age >= 18:
    if has_license:
        if has_car:
            print("You can drive alone")
        else:
            print("You can drive with a borrowed car")
            if is_weekend:
                print("Weekend driving is allowed")
            else:
                print("Weekday driving restrictions apply")
    else:
        print("You need a license to drive")
        if age >= 16:
            print("You can apply for a learner's permit")
else:
    print("You are too young to drive")
    if age >= 16:
        print("You can start driver's education")

# User authentication with nested validation
username = "alice"
password = "secret123"
is_active = True
login_attempts = 2

if username and password:  # Check if both provided
    if is_active:
        if login_attempts < 3:
            print("Login successful")
        else:
            print("Account temporarily locked")
            print("Too many failed attempts")
    else:
        print("Account is deactivated")
        print("Contact support to reactivate")
else:
    print("Username and password required")
    if not username:
        print("Username is missing")
    if not password:
        print("Password is missing")
```

---

# **TERNARY OPERATOR - Concise Conditional Expressions**

## **1. Basic Ternary Operator - Simple Decisions**

```python
# Traditional if/else vs ternary
age = 20

# Traditional approach
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator (one-liner)
status = "adult" if age >= 18 else "minor"

print(f"You are an {status}")

# Another example - number classification
number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result}")

# String validation
text = "hello"
length_status = "long" if len(text) > 5 else "short"
print(f"Text is {length_status}")
```

## **2. Advanced Ternary Patterns - Complex Conditions**

```python
# Multiple conditions in ternary
age = 25
has_license = True

# Complex ternary with multiple conditions
can_drive = "yes" if (age >= 18 and has_license) else "no"
print(f"Can drive: {can_drive}")

# Nested ternary (use sparingly for readability)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"Grade: {grade}")

# Ternary with function calls
def get_message(age):
    return "Welcome!" if age >= 18 else "Parental consent required"

message = get_message(20)
print(message)

# Ternary for default values
user_input = ""
display_name = user_input if user_input else "Anonymous"
print(f"Hello, {display_name}")

# Ternary with calculations
x = 10
y = 5
max_value = x if x > y else y
min_value = x if x < y else y
print(f"Max: {max_value}, Min: {min_value}")
```

---

# **LOGICAL OPERATORS - Combining Conditions**

## **1. Basic Logical Operators - AND, OR, NOT**

```python
# AND operator - both conditions must be True
age = 25
has_license = True
has_car = False

# Basic AND
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")  # True

# Multiple AND conditions
can_drive_alone = age >= 18 and has_license and has_car
print(f"Can drive alone: {can_drive_alone}")  # False

# OR operator - at least one condition must be True
is_student = True
is_employed = False

# Basic OR
has_discount = is_student or is_employed
print(f"Has discount: {has_discount}")  # True

# Multiple OR conditions
can_access = is_student or is_employed or age >= 65
print(f"Can access: {can_access}")  # True

# NOT operator - negates the condition
is_weekend = False

# Basic NOT
is_weekday = not is_weekend
print(f"Is weekday: {is_weekday}")  # True

# NOT with complex conditions
cannot_drive = not (age >= 18 and has_license)
print(f"Cannot drive: {cannot_drive}")  # False
```

## **2. Complex Logical Expressions - Combining All Operators**

```python
# Complex driving logic
age = 20
has_license = True
has_car = False
is_weekend = True
is_emergency = False

# Complex condition with parentheses for clarity
can_drive = (
    (age >= 18 and has_license) or  # Normal driving
    (age >= 16 and has_license and has_car and is_weekend) or  # Weekend driving
    is_emergency  # Emergency situations
)

print(f"Can drive: {can_drive}")

# User access control
is_admin = False
is_moderator = True
is_premium = False
has_invitation = True

# Access levels with logical operators
can_edit = is_admin or is_moderator
can_delete = is_admin
can_invite = is_admin or is_moderator or (is_premium and has_invitation)

print(f"Can edit: {can_edit}")
print(f"Can delete: {can_delete}")
print(f"Can invite: {can_invite}")

# Data validation with multiple checks
email = "user@example.com"
password = "secret123"
age = 25

# Comprehensive validation
is_valid = (
    "@" in email and  # Has @ symbol
    "." in email.split("@")[1] and  # Has domain with dot
    len(password) >= 8 and  # Password length
    any(c.isdigit() for c in password) and  # Has digit
    any(c.isupper() for c in password) and  # Has uppercase
    age >= 13  # Minimum age
)

print(f"All validations passed: {is_valid}")
```

## **3. Short-Circuit Evaluation - Performance Optimization**

```python
# AND short-circuit - stops at first False
x = 5
y = 0

# This won't cause division by zero error
if y != 0 and x / y > 2:
    print("Condition met")
else:
    print("Safe evaluation - no division by zero")

# OR short-circuit - stops at first True
name = "John"
age = 25

# This won't cause error if name is empty
if name or age > 18:
    print("Valid user")
else:
    print("Invalid user")

# Practical example - safe division
numerator = 10
denominator = 0

# Safe division using short-circuit
if denominator != 0 and numerator / denominator > 2:
    print("Result is greater than 2")
else:
    print("Cannot divide or result is not greater than 2")

# Function call optimization
def expensive_check():
    print("Running expensive check...")
    return False

# Expensive function won't run due to short-circuit
if False and expensive_check():
    print("This will never print")

# List validation with short-circuit
numbers = [1, 2, 3, 4, 5]
index = 3

# Safe list access with short-circuit
if index < len(numbers) and numbers[index] > 0:
    print(f"Valid positive number: {numbers[index]}")
else:
    print("Invalid index or non-positive number")
```

---

# **FOR LOOPS - Iteration Mastery**

## **1. Basic for Loop - Iterating Over Sequences**

```python
# Loop through a string
name = "Python"
for letter in name:
    print(letter)

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop through a tuple
coordinates = (1, 2), (3, 4), (5, 6)
for x, y in coordinates:
    print(f"Point: ({x}, {y})")

# Loop through a dictionary
person = {"name": "John", "age": 30, "city": "NYC"}
for key in person:
    print(f"{key}: {person[key]}")

# Loop through dictionary items
for key, value in person.items():
    print(f"{key}: {value}")
```

## **2. range() Function - Numeric Iteration**

```python
# Basic range - starts from 0
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4

# Range with start and end
for i in range(1, 6):
    print(i)  # Prints: 1, 2, 3, 4, 5

# Range with step
for i in range(0, 10, 2):
    print(i)  # Prints: 0, 2, 4, 6, 8

# Range with negative step (countdown)
for i in range(5, 0, -1):
    print(i)  # Prints: 5, 4, 3, 2, 1

# Range for specific patterns
# Even numbers
for i in range(0, 11, 2):
    print(f"Even: {i}")

# Multiples of 3
for i in range(0, 16, 3):
    print(f"Multiple of 3: {i}")

# Practical example - multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each row
```

## **3. Advanced for Loop Patterns**

```python
# Enumerate - get both index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Enumerate with custom start
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Zip - iterate over multiple sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old from {city}")

# Filter with for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Even numbers: {even_numbers}")

# List comprehension equivalent
even_numbers_comp = [num for num in numbers if num % 2 == 0]
print(f"Even numbers (comprehension): {even_numbers_comp}")

# Dictionary building with for loop
scores = [85, 92, 78, 96, 88]
grade_scale = {}

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"

    grade_scale[score] = grade

print(f"Grade scale: {grade_scale}")
```

---

# **FOR-ELSE STATEMENT - Advanced Loop Control**

## **1. Basic for-else Pattern - Search and Find**

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

# Password validation with attempts
password = "secret123"
attempts = ["wrong", "also_wrong", "secret123", "another_wrong"]

for attempt in attempts:
    if attempt == password:
        print("Access granted!")
        break
else:
    print("Access denied - too many wrong attempts")

# File search example
files = ["document.txt", "image.jpg", "data.csv"]
target_file = "report.pdf"

for file in files:
    if file == target_file:
        print(f"Found {target_file}")
        break
else:
    print(f"{target_file} not found in directory")
```

## **2. Advanced for-else Patterns - Complex Scenarios**

```python
# Prime number checker
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

# Test prime numbers
test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in test_numbers:
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

# Data validation with for-else
def validate_data(data_list):
    required_fields = ["name", "email", "age"]

    for field in required_fields:
        if field not in data_list:
            print(f"Missing required field: {field}")
            break
    else:
        print("All required fields present")
        return True

    return False

# Test validation
test_data1 = {"name": "Alice", "email": "alice@example.com", "age": 25}
test_data2 = {"name": "Bob", "email": "bob@example.com"}

print("Data 1:", validate_data(test_data1))
print("Data 2:", validate_data(test_data2))

# Pattern matching with for-else
def find_pattern(text, pattern):
    text_lower = text.lower()
    pattern_lower = pattern.lower()

    for i in range(len(text_lower) - len(pattern_lower) + 1):
        if text_lower[i:i + len(pattern_lower)] == pattern_lower:
            print(f"Pattern '{pattern}' found at position {i}")
            break
    else:
        print(f"Pattern '{pattern}' not found in text")

# Test pattern matching
text = "Hello World, welcome to Python programming"
find_pattern(text, "world")
find_pattern(text, "java")
```

---

# **NESTED LOOPS - Multi-Dimensional Iteration**

## **1. Basic Nested Loops - Grid Patterns**

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

# Coordinate grid
for x in range(3):
    for y in range(3):
        print(f"({x},{y})", end=" ")
    print()  # New line after each row
```

## **2. Advanced Nested Loop Patterns - Real Applications**

```python
# Matrix operations
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Matrix addition
result = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Matrix addition result:")
for row in result:
    print(row)

# Data processing with nested loops
students = [
    {"name": "Alice", "scores": [85, 92, 78]},
    {"name": "Bob", "scores": [90, 88, 95]},
    {"name": "Charlie", "scores": [76, 85, 80]}
]

# Calculate average scores for each student
for student in students:
    total = 0
    for score in student["scores"]:
        total += score

    average = total / len(student["scores"])
    print(f"{student['name']}: Average = {average:.1f}")

# Game board representation
board_size = 3
for row in range(board_size):
    for col in range(board_size):
        if row == col:  # Diagonal
            print("X", end=" ")
        elif row + col == board_size - 1:  # Anti-diagonal
            print("O", end=" ")
        else:
            print("-", end=" ")
    print()  # New line after each row
```

---

# **WHILE LOOPS - Conditional Iteration**

## **1. Basic while Loop - Simple Repetition**

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

# Counter-controlled while loop
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")
```

## **2. Advanced while Loop Patterns - Complex Scenarios**

```python
# Data processing with while loop
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
sum_values = 0

while index < len(data):
    if data[index] % 2 == 0:  # Only process even numbers
        sum_values += data[index]
    index += 1

print(f"Sum of even numbers: {sum_values}")

# Menu system with while loop
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

# Game loop with state management
game_running = True
player_health = 100
enemy_count = 5

while game_running:
    print(f"\nPlayer Health: {player_health}")
    print(f"Enemies Remaining: {enemy_count}")

    if player_health <= 0:
        print("Game Over - Player defeated!")
        game_running = False
    elif enemy_count <= 0:
        print("Victory - All enemies defeated!")
        game_running = False
    else:
        # Game logic here
        action = input("Choose action (attack/heal/quit): ")
        if action == "quit":
            print("Game ended by player")
            game_running = False
        elif action == "attack":
            enemy_count -= 1
            print("Enemy defeated!")
        elif action == "heal":
            player_health = min(100, player_health + 20)
            print("Health restored!")
        else:
            print("Invalid action")
```

---

# **INFINITE LOOPS - Controlled Endless Execution**

## **1. Game Loop Pattern - Continuous Operation**

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

## **2. Event-Driven Loop Pattern - Responding to Events**

```python
# Event processing loop
events = ["click", "keypress", "scroll", "quit"]
event_index = 0

while True:
    current_event = events[event_index % len(events)]

    if current_event == "quit":
        print("Shutting down...")
        break
    elif current_event == "click":
        print("Processing click event")
    elif current_event == "keypress":
        print("Processing keypress event")
    elif current_event == "scroll":
        print("Processing scroll event")

    event_index += 1

    # Simulate event processing time
    import time
    time.sleep(0.1)
```

---

# **BREAK AND CONTINUE - Loop Control**

## **1. Break Statement - Early Loop Termination**

```python
# Find first negative number
numbers = [1, 3, -2, 5, 7]
for num in numbers:
    if num < 0:
        print(f"First negative number: {num}")
        break

# Search with break
search_term = "Python"
text = "I love Python programming language"

words = text.split()
for word in words:
    if word.lower() == search_term.lower():
        print(f"Found '{search_term}' in text")
        break
else:
    print(f"'{search_term}' not found in text")

# Break in nested loops
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"Breaking at ({i}, {j})")
            break  # Only breaks inner loop
    print(f"Outer loop iteration {i}")
```

## **2. Continue Statement - Skip Current Iteration**

```python
# Skip processing for invalid data
scores = [85, 92, -1, 78, 95, -1, 88]
valid_scores = []

for score in scores:
    if score == -1:  # Invalid score
        continue  # Skip this iteration
    valid_scores.append(score)

print(f"Valid scores: {valid_scores}")

# Process only positive numbers
numbers = [-2, -1, 0, 1, 2, 3, -4, 5]
positive_sum = 0

for num in numbers:
    if num <= 0:
        continue  # Skip non-positive numbers
    positive_sum += num

print(f"Sum of positive numbers: {positive_sum}")

# Continue with nested loops
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:  # Skip diagonal elements
            continue
        print(f"({i}, {j})", end=" ")
    print()  # New line after each row
```

---

# **ITERABLES - Understanding What Can Be Looped**

## **1. Built-in Iterable Types**

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

# Set iteration
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
```

## **2. Custom Iterable Objects**

```python
# Range-like custom iterator
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Use custom iterator
for num in CountDown(5):
    print(num)

# Generator function (simple iterable)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Use generator
for num in fibonacci(10):
    print(num, end=" ")
```

---

# **MEMBERSHIP TESTING - Checking for Existence**

## **1. Using 'in' Operator**

```python
# List membership
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("orange" in fruits)  # False

# String membership
text = "Hello World"
print("Hello" in text)  # True
print("Python" in text)  # False

# Dictionary membership (checks keys)
person = {"name": "John", "age": 30}
print("name" in person)  # True
print("city" in person)  # False

# Set membership
colors = {"red", "green", "blue"}
print("red" in colors)  # True
print("yellow" in colors)  # False

# Tuple membership
coordinates = (1, 2), (3, 4), (5, 6)
print((1, 2) in coordinates)  # True
print((2, 1) in coordinates)  # False
```

## **2. Practical Membership Testing Examples**

```python
# User validation
allowed_users = ["admin", "user1", "user2"]
username = input("Enter username: ")

if username in allowed_users:
    print("Access granted")
else:
    print("Access denied")

# Data filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [2, 4, 6, 8, 10]

# Check if all numbers are even
all_even = all(num in even_numbers for num in numbers)
print(f"All numbers are even: {all_even}")

# Check if any numbers are even
any_even = any(num in even_numbers for num in numbers)
print(f"Any numbers are even: {any_even}")

# Password strength validation
password = "Secret123"
required_chars = "!@#$%^&*"
has_special = any(char in required_chars for char in password)
print(f"Password has special characters: {has_special}")

# File extension validation
allowed_extensions = {".txt", ".pdf", ".doc", ".docx"}
filename = "document.pdf"
file_extension = filename[filename.rfind("."):]

if file_extension in allowed_extensions:
    print(f"File type '{file_extension}' is allowed")
else:
    print(f"File type '{file_extension}' is not allowed")
```

---

# **KEY CONCEPTS SUMMARY**

## **Comparison Operators**

- `==` - Equal to
- `!=` - Not equal to
- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal to
- `>=` - Greater than or equal to
- `is` - Identity comparison (same object)
- `is not` - Identity comparison (different objects)

## **Logical Operators**

- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `not` - Negates the condition
- Short-circuit evaluation for performance

## **Control Flow Structures**

- `if/elif/else` - Conditional execution
- `for` - Iterate over sequences
- `while` - Repeat while condition is True
- `break` - Exit loop immediately
- `continue` - Skip to next iteration
- `for-else` - Execute else when loop completes normally

## **Loop Patterns**

- `while True` - Infinite loop with break
- Nested loops - Loops inside loops
- Enumerate - Get index and value
- Zip - Iterate over multiple sequences
- Range - Numeric iteration with step

## **Best Practices**

- Use meaningful variable names
- Keep conditions simple and readable
- Use break/continue sparingly
- Avoid infinite loops without exit conditions
- Use chained comparisons for ranges
- Leverage short-circuit evaluation for safety
- Prefer for loops over while loops when possible

## **Common Patterns**

- Input validation loops
- Search patterns with for-else
- Menu systems with while True
- Counter-controlled loops
- Nested loops for grids/tables
- Data processing pipelines
- Game loops with state management

---

This comprehensive guide covers **all the different ways** to control program flow in Python. Master these patterns to write clear, efficient, and maintainable code that makes intelligent decisions and repeats actions effectively.
