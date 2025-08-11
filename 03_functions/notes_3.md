# FUNCTIONS - MASTERING CODE ORGANIZATION & REUSABILITY

# Functions = Reusable blocks of code that perform specific tasks

# Allow breaking complex problems into smaller, manageable pieces

---

# DEFINING FUNCTIONS

# Basic function definition using 'def' keyword

```python
# Simple function with no parameters
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)  # Output: 5 + 3 = 8
```

# Function naming conventions

```python
# Use snake_case for function names
def calculate_area():
    pass

def get_user_input():
    pass

def process_payment_data():
    pass

# Functions should be verbs (actions)
def validate_email():
    pass

def convert_temperature():
    pass
```

---

# RETURN STATEMENTS

# Functions can return values using 'return' keyword

```python
# Function that returns a value
def add(a, b):
    return a + b

# Use the returned value
result = add(5, 3)
print(result)  # Output: 8

# Function with multiple return statements
def get_grade(score):
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

grade = get_grade(85)
print(f"Your grade is: {grade}")  # Output: Your grade is: B
```

# Return vs Print

```python
# Function that prints (no return value)
def print_sum(a, b):
    print(a + b)

# Function that returns (can be used in expressions)
def calculate_sum(a, b):
    return a + b

# Usage difference
print_sum(5, 3)  # Prints: 8, but returns None
result = calculate_sum(5, 3)  # Returns 8, can be stored
print(result * 2)  # Can use the result in calculations
```

---

# FUNCTION ARGUMENTS

# Positional arguments - order matters

```python
def introduce(name, age, city):
    print(f"Hi, I'm {name}, {age} years old, from {city}")

# Arguments passed by position
introduce("John", 25, "New York")
# Output: Hi, I'm John, 25 years old, from New York

# Order matters!
introduce(25, "John", "New York")  # Wrong!
# Output: Hi, I'm 25, John years old, from New York
```

# Variable number of arguments

```python
# *args - accepts any number of positional arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# **kwargs - accepts any number of keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Boston")
# Output:
# name: Alice
# age: 30
# city: Boston
```

---

# KEYWORD ARGUMENTS

# Named arguments - order doesn't matter

```python
def create_profile(name, age, email, city):
    return f"Profile: {name}, {age}, {email}, {city}"

# Using keyword arguments
profile = create_profile(
    age=25,
    name="Alice",
    city="Boston",
    email="alice@email.com"
)
print(profile)

# Mix positional and keyword arguments
profile2 = create_profile("Bob", age=30, email="bob@email.com", city="Seattle")
```

# Keyword-only arguments

```python
# Arguments after * must be passed as keywords
def calculate_price(base_price, *, discount=0, tax_rate=0.1):
    discounted = base_price * (1 - discount)
    final_price = discounted * (1 + tax_rate)
    return final_price

# Must use keyword arguments for discount and tax_rate
price = calculate_price(100, discount=0.2, tax_rate=0.08)
print(f"Final price: ${price:.2f}")
```

---

# DEFAULT ARGUMENTS

# Parameters with default values

```python
# Function with default parameter
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Uses default: Hello, Alice!
greet("Bob", "Hi")          # Custom greeting: Hi, Bob!
greet("Charlie", "Hey")     # Custom greeting: Hey, Charlie!

# Multiple default parameters
def create_user(username, email, role="user", active=True):
    return {
        "username": username,
        "email": email,
        "role": role,
        "active": active
    }

# Use some defaults
user1 = create_user("alice", "alice@email.com")
print(user1)  # {'username': 'alice', 'email': 'alice@email.com', 'role': 'user', 'active': True}

# Override defaults
user2 = create_user("admin", "admin@email.com", role="admin", active=False)
print(user2)
```

# Default argument gotchas

```python
# AVOID: Mutable default arguments
def add_item(item, items=[]):  # DON'T DO THIS!
    items.append(item)
    return items

# CORRECT: Use None as default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

# FUNCTION SCOPE

# Local vs Global variables

```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {global_var}")  # Can access global
    print(f"Inside function: {local_var}")   # Can access local

my_function()
print(f"Outside function: {global_var}")    # Can access global
# print(local_var)  # ERROR! Can't access local variable outside function
```

# Variable shadowing

```python
name = "Global Alice"

def greet():
    name = "Local Bob"  # Shadows global variable
    print(f"Hello, {name}")

greet()        # Output: Hello, Local Bob
print(name)    # Output: Global Alice (unchanged)
```

# Global keyword

```python
counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify global
    counter += 1
    print(f"Counter: {counter}")

increment()  # Counter: 1
increment()  # Counter: 2
print(f"Final counter: {counter}")  # Final counter: 2
```

---

# NESTED FUNCTIONS

# Functions inside functions

```python
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function(10)

result = outer_function(5)
print(result)  # Output: 15

# Closures - inner function remembers outer variables
def create_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

# Create specialized functions
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

---

# FUNCTION TYPES

# Pure functions - same input always gives same output

```python
# Pure function - no side effects
def calculate_area(length, width):
    return length * width

# Always returns same result for same inputs
area1 = calculate_area(5, 3)  # Always 15
area2 = calculate_area(5, 3)  # Always 15
```

# Functions with side effects

```python
# Function with side effects (prints, modifies global state)
total_calls = 0

def log_and_add(a, b):
    global total_calls
    total_calls += 1
    print(f"Call #{total_calls}: Adding {a} and {b}")
    return a + b

result = log_and_add(2, 3)  # Has side effects: prints and modifies global
```

# Higher-order functions

```python
# Functions that take other functions as parameters
def apply_operation(numbers, operation):
    results = []
    for num in numbers:
        results.append(operation(num))
    return results

def square(x):
    return x * x

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
doubled = apply_operation(numbers, double)

print(f"Squared: {squared}")  # [1, 4, 9, 16, 25]
print(f"Doubled: {doubled}")  # [2, 4, 6, 8, 10]
```

---

# LAMBDA FUNCTIONS

# Anonymous functions for simple operations

```python
# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add(5, 3))        # Output: 8
print(add_lambda(5, 3)) # Output: 8

# Lambda with single parameter
square = lambda x: x * x
print(square(4))  # Output: 16

# Lambda in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Lambda with conditionals
max_val = lambda a, b: a if a > b else b
print(max_val(10, 5))  # Output: 10
```

---

# DEBUGGING FUNCTIONS

# Using print statements for debugging

```python
def calculate_compound_interest(principal, rate, time):
    print(f"DEBUG: principal={principal}, rate={rate}, time={time}")

    amount = principal
    for year in range(time):
        interest = amount * rate
        amount += interest
        print(f"DEBUG: Year {year + 1}, Interest={interest:.2f}, Amount={amount:.2f}")

    return amount

result = calculate_compound_interest(1000, 0.05, 3)
print(f"Final amount: ${result:.2f}")
```

# Using return values for debugging

```python
def validate_input(value):
    if not isinstance(value, (int, float)):
        return False, "Value must be a number"
    if value < 0:
        return False, "Value must be positive"
    return True, "Valid input"

# Check validation results
is_valid, message = validate_input(-5)
if not is_valid:
    print(f"Error: {message}")
else:
    print("Input is valid")
```

---

# RUNNING SCRIPTS SAFELY (THE MAIN GUARD)

# Use a guard to prevent top-level code from running on import

```python
def run_converter():
    print("Running the converter loop...")
    # ... main loop here ...


if __name__ == "__main__":
    # This block runs ONLY when the file is executed directly:
    # python unit_converter_v2.py
    run_converter()
```

# Why this matters

- When Python loads a file, it sets a built-in variable `__name__`.
- If the file is executed directly, `__name__ == "__main__"`.
- If the file is imported from another file, `__name__` becomes the module name, so the guarded block does NOT run.
- This lets you keep reusable functions importable without triggering the script’s CLI logic.

# Quick check

```python
print("Module name:", __name__)

def add(a, b):
    return a + b

if __name__ == "__main__":
    # Runs only when this file is executed directly
    print(add(2, 3))
```

# Mini‑drill

1. Add `print("Module:", __name__)` near the top of a script and run it with `python your_file.py`.
2. Observe it prints `__main__`.
3. Create another file and `import your_file`; observe the printed module name is `your_file` and the guarded block does not run.

---

# COMMON FUNCTION PATTERNS

# Input validation pattern

```python
def safe_divide(a, b):
    if b == 0:
        return None, "Cannot divide by zero"
    return a / b, "Success"

result, message = safe_divide(10, 2)
if result is not None:
    print(f"Result: {result}")
else:
    print(f"Error: {message}")
```

# Configuration pattern

```python
def create_connection(host="localhost", port=5432, database="mydb", timeout=30):
    return {
        "host": host,
        "port": port,
        "database": database,
        "timeout": timeout,
        "status": "connected"
    }

# Use defaults
conn1 = create_connection()

# Override specific settings
conn2 = create_connection(host="production.db", timeout=60)
```

# Factory pattern

```python
def create_calculator(operation):
    if operation == "add":
        return lambda x, y: x + y
    elif operation == "multiply":
        return lambda x, y: x * y
    elif operation == "power":
        return lambda x, y: x ** y
    else:
        return lambda x, y: 0

adder = create_calculator("add")
multiplier = create_calculator("multiply")

print(adder(5, 3))      # Output: 8
print(multiplier(4, 6)) # Output: 24
```

---

# KEY CONCEPTS SUMMARY

## Function Definition

- `def function_name(parameters):` - Define a function
- `return value` - Return a value from function
- Function names should be verbs in snake_case

## Parameters and Arguments

- **Positional arguments** - Order matters
- **Keyword arguments** - Named parameters
- **Default parameters** - Optional with default values
- **\*args** - Variable number of positional arguments
- **\*\*kwargs** - Variable number of keyword arguments

## Scope

- **Local scope** - Variables inside function
- **Global scope** - Variables outside all functions
- **global keyword** - Modify global variables inside functions
- **Variable shadowing** - Local variables hide global ones

## Function Types

- **Pure functions** - No side effects, same input → same output
- **Functions with side effects** - Modify global state or print
- **Higher-order functions** - Take functions as parameters
- **Lambda functions** - Anonymous functions for simple operations

## Best Practices

- Functions should do one thing well
- Use descriptive names for functions and parameters
- Keep functions small and focused
- Use return values rather than printing when possible
- Validate input parameters
- Use default parameters for optional settings
- Avoid mutable default arguments

## Common Patterns

- Input validation with error handling
- Configuration functions with defaults
- Factory functions that create other functions
- Debugging with print statements and return codes
- Pure functions for calculations
- Side-effect functions for I/O operations

## Debugging

- Use print statements to trace execution
- Return error codes and messages
- Test functions with different inputs
- Use meaningful variable names
- Break complex functions into smaller ones
