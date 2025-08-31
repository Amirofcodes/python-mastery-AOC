# 03 · Functions - Comprehensive Code Organization & Reusability Guide

Master Python functions through complete understanding of **all the different ways** to define, call, and organize code for maximum reusability and maintainability.

---

## **Mental Model: Function Design Philosophy**

- **Functions**: Reusable blocks of code that perform specific tasks
- **Single Responsibility**: Each function should do one thing well
- **Input/Output**: Functions take parameters and return results
- **Scope Management**: Control variable visibility and lifetime
- **Code Organization**: Break complex problems into manageable pieces
- **Reusability**: Write once, use many times across your program

---

# **FUNCTION DEFINITION - Creating Reusable Code Blocks**

## **1. Basic Function Definition - All Patterns**

```python
# Pattern 1: Simple function with no parameters
def greet():
    print("Hello, World!")

# Pattern 2: Function with single parameter
def greet_person(name):
    print(f"Hello, {name}!")

# Pattern 3: Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

# Pattern 4: Function with default parameter
def greet_with_default(name="World"):
    print(f"Hello, {name}!")

# Pattern 5: Function with multiple defaults
def create_profile(name, age=25, city="Unknown"):
    return f"Name: {name}, Age: {age}, City: {city}"

# Pattern 6: Function with variable arguments
def sum_all(*numbers):
    return sum(numbers)

# Pattern 7: Function with keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# Pattern 8: Function with mixed argument types
def complex_function(name, age, *args, city="Unknown", **kwargs):
    print(f"Name: {name}, Age: {age}, City: {city}")
    print(f"Additional args: {args}")
    print(f"Additional kwargs: {kwargs}")
```

## **2. Function Naming Conventions - Best Practices**

```python
# Use snake_case for function names (Python convention)
def calculate_area():
    pass

def get_user_input():
    pass

def process_payment_data():
    pass

def validate_email_address():
    pass

def convert_temperature_celsius_to_fahrenheit():
    pass

# Functions should be verbs (actions)
def validate_email():
    pass

def convert_temperature():
    pass

def calculate_total():
    pass

def process_data():
    pass

def authenticate_user():
    pass

# Descriptive names that explain what the function does
def calculate_monthly_payment(principal, rate, years):
    """Calculate monthly mortgage payment"""
    monthly_rate = rate / 12 / 100
    num_payments = years * 12
    payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    return payment

# Avoid generic names
# def do_something():  # Too vague
# def process():        # Too generic
# def calc():          # Too abbreviated
```

---

# **RETURN STATEMENTS - Output from Functions**

## **1. Basic Return Patterns - All Types**

```python
# Pattern 1: Simple return value
def add(a, b):
    return a + b

# Pattern 2: Multiple return statements (early exit)
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

# Pattern 3: Return with calculation
def calculate_area(length, width):
    area = length * width
    return area

# Pattern 4: Return multiple values (tuple)
def get_name_and_age():
    return "Alice", 25

# Pattern 5: Return with conditional logic
def get_status(age, has_license):
    if age >= 18 and has_license:
        return "Can drive"
    elif age >= 16:
        return "Can learn to drive"
    else:
        return "Too young to drive"

# Pattern 6: Return with default fallback
def get_user_preference(user_id, default="standard"):
    # Try to get user preference
    preference = database.get_preference(user_id)
    return preference if preference else default

# Pattern 7: Return None explicitly
def log_message(message):
    print(f"LOG: {message}")
    return None

# Pattern 8: Return boolean for validation
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]
```

## **2. Return vs Print - Understanding the Difference**

```python
# Function that prints (no return value)
def print_sum(a, b):
    print(a + b)

# Function that returns (can be used in expressions)
def calculate_sum(a, b):
    return a + b

# Usage difference demonstration
print_sum(5, 3)  # Prints: 8, but returns None
result = calculate_sum(5, 3)  # Returns 8, can be stored

# Can use returned value in expressions
double_result = calculate_sum(5, 3) * 2  # 16
print(f"Double the sum: {double_result}")

# Can't use print function in expressions
# double_print = print_sum(5, 3) * 2  # TypeError: NoneType * int

# Practical example - building calculations
def get_tax_rate(income):
    if income < 50000:
        return 0.15
    elif income < 100000:
        return 0.25
    else:
        return 0.35

def calculate_tax(income):
    rate = get_tax_rate(income)
    tax = income * rate
    return tax

# Can chain function calls
total_income = 75000
tax_amount = calculate_tax(total_income)
print(f"Income: ${total_income:,}, Tax: ${tax_amount:,.2f}")

# Can use in conditional statements
if calculate_tax(100000) > 20000:
    print("High tax bracket")
```

---

# **FUNCTION ARGUMENTS - Input to Functions**

## **1. Positional Arguments - Order Matters**

```python
# Basic positional arguments
def introduce(name, age, city):
    print(f"Hi, I'm {name}, {age} years old, from {city}")

# Arguments passed by position
introduce("John", 25, "New York")
# Output: Hi, I'm John, 25 years old, from New York

# Order matters!
introduce(25, "John", "New York")  # Wrong!
# Output: Hi, I'm 25, John years old, from New York

# Multiple positional arguments with calculation
def calculate_distance(x1, y1, x2, y2):
    """Calculate distance between two points"""
    dx = x2 - x1
    dy = y2 - y1
    distance = (dx**2 + dy**2)**0.5
    return distance

# Usage
point1 = (0, 0)
point2 = (3, 4)
distance = calculate_distance(point1[0], point1[1], point2[0], point2[1])
print(f"Distance: {distance}")  # 5.0

# Positional arguments with validation
def validate_coordinates(x, y, z):
    """Validate 3D coordinates are within bounds"""
    if not (-100 <= x <= 100):
        raise ValueError(f"X coordinate {x} out of bounds")
    if not (-100 <= y <= 100):
        raise ValueError(f"Y coordinate {y} out of bounds")
    if not (-100 <= z <= 100):
        raise ValueError(f"Z coordinate {z} out of bounds")
    return True

# Test validation
try:
    validate_coordinates(50, 75, 150)  # Z out of bounds
except ValueError as e:
    print(f"Validation error: {e}")
```

## **2. Keyword Arguments - Named Parameters**

```python
# Using keyword arguments
def create_profile(name, age, email, city):
    return f"Profile: {name}, {age}, {email}, {city}"

# Order doesn't matter with keywords
profile1 = create_profile(
    age=25,
    name="Alice",
    city="Boston",
    email="alice@email.com"
)

profile2 = create_profile(
    name="Bob",
    email="bob@email.com",
    age=30,
    city="Seattle"
)

print(profile1)
print(profile2)

# Mix positional and keyword arguments
# Positional arguments must come first
profile3 = create_profile("Charlie", age=35, email="charlie@email.com", city="LA")

# This would cause an error:
# profile4 = create_profile(name="David", 40, email="david@email.com", city="Chicago")

# Keyword arguments for clarity
def calculate_compound_interest(principal, rate, time, compounds_per_year=12):
    """Calculate compound interest with default monthly compounding"""
    rate_per_period = rate / compounds_per_year / 100
    num_periods = time * compounds_per_year
    amount = principal * (1 + rate_per_period) ** num_periods
    return amount

# Use defaults
monthly_result = calculate_compound_interest(1000, 5, 10)  # Monthly compounding

# Override default
quarterly_result = calculate_compound_interest(1000, 5, 10, compounds_per_year=4)

print(f"Monthly compounding: ${monthly_result:.2f}")
print(f"Quarterly compounding: ${quarterly_result:.2f}")
```

## **3. Default Arguments - Optional Parameters**

```python
# Function with default parameter
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Uses default: Hello, Alice!
greet("Bob", "Hi")          # Custom greeting: Hi, Bob!
greet("Charlie", "Hey")     # Custom greeting: Hey, Charlie!

# Multiple default parameters
def create_user(username, email, role="user", active=True, created_date=None):
    if created_date is None:
        from datetime import datetime
        created_date = datetime.now()

    return {
        "username": username,
        "email": email,
        "role": role,
        "active": active,
        "created_date": created_date
    }

# Use some defaults
user1 = create_user("alice", "alice@email.com")
print(user1)

# Override specific defaults
user2 = create_user("admin", "admin@email.com", role="admin", active=False)
print(user2)

# Override all defaults
user3 = create_user("moderator", "mod@email.com", role="moderator", active=True)
print(user3)

# Default argument gotchas - MUTABLE DEFAULTS
# AVOID: Mutable default arguments
def add_item_bad(item, items=[]):  # DON'T DO THIS!
    items.append(item)
    return items

# This creates problems because all calls share the same list
result1 = add_item_bad("apple")
result2 = add_item_bad("banana")
print(result1)  # ['apple', 'banana'] - unexpected!
print(result2)  # ['apple', 'banana'] - same list!

# CORRECT: Use None as default
def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# Now each call gets a fresh list
result1 = add_item_good("apple")
result2 = add_item_good("banana")
print(result1)  # ['apple']
print(result2)  # ['banana']
```

## **4. Variable Arguments - Flexible Parameter Count**

```python
# *args - accepts any number of positional arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print(sum_all())                # Output: 0

# *args with other parameters
def create_sentence(subject, verb, *objects):
    sentence = f"{subject} {verb}"
    if objects:
        sentence += " " + " ".join(objects)
    sentence += "."
    return sentence

print(create_sentence("I", "love", "Python", "programming"))
print(create_sentence("She", "runs"))
print(create_sentence("They", "eat", "pizza", "every", "Friday"))

# **kwargs - accepts any number of keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Boston")
print_info(title="Manager", department="Engineering", salary=75000)

# Combine *args and **kwargs
def flexible_function(name, *args, **kwargs):
    print(f"Name: {name}")
    if args:
        print(f"Positional arguments: {args}")
    if kwargs:
        print(f"Keyword arguments: {kwargs}")

flexible_function("Alice", 25, "Engineer", city="Boston", experience=5)

# Practical example - configuration function
def configure_database(host, port, **options):
    config = {
        "host": host,
        "port": port
    }
    config.update(options)
    return config

# Basic configuration
basic_config = configure_database("localhost", 5432)

# Advanced configuration
advanced_config = configure_database(
    "production.db",
    5432,
    username="admin",
    password="secret",
    ssl=True,
    timeout=30
)

print("Basic config:", basic_config)
print("Advanced config:", advanced_config)
```

---

# **FUNCTION SCOPE - Variable Visibility and Lifetime**

## **1. Local vs Global Variables - Understanding Scope**

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

# Variable shadowing
name = "Global Alice"

def greet():
    name = "Local Bob"  # Shadows global variable
    print(f"Hello, {name}")

greet()        # Output: Hello, Local Bob
print(name)    # Output: Global Alice (unchanged)

# Global keyword - modify global variables
counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify global
    counter += 1
    print(f"Counter: {counter}")

increment()  # Counter: 1
increment()  # Counter: 2
print(f"Final counter: {counter}")  # Final counter: 2

# Practical example - configuration management
app_config = {
    "debug": False,
    "log_level": "INFO",
    "max_connections": 100
}

def update_config(key, value):
    global app_config
    if key in app_config:
        app_config[key] = value
        print(f"Updated {key} to {value}")
    else:
        print(f"Unknown config key: {key}")

def get_config(key):
    return app_config.get(key, "Not found")

# Test configuration management
print("Initial config:", app_config)
update_config("debug", True)
update_config("max_connections", 200)
print("Updated config:", app_config)
print("Debug mode:", get_config("debug"))
```

## **2. Advanced Scope Patterns - Nested Functions and Closures**

```python
# Nested functions
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

# Practical closure example - rate calculator
def create_rate_calculator(base_rate):
    def calculate_rate(amount, risk_factor=1.0):
        return base_rate * amount * risk_factor
    return calculate_rate

# Create different calculators
mortgage_calculator = create_rate_calculator(0.05)  # 5% base rate
credit_calculator = create_rate_calculator(0.15)   # 15% base rate

# Use calculators
mortgage_payment = mortgage_calculator(200000, 1.2)  # Higher risk
credit_payment = credit_calculator(10000, 0.8)       # Lower risk

print(f"Mortgage payment: ${mortgage_payment:,.2f}")
print(f"Credit payment: ${credit_payment:,.2f}")

# Scope chain example
def outer():
    x = 1

    def inner():
        y = 2

        def innermost():
            z = 3
            print(f"x={x}, y={y}, z={z}")  # Can access all outer variables

        innermost()

    inner()

outer()  # Output: x=1, y=2, z=3
```

---

# **FUNCTION TYPES - Different Kinds of Functions**

## **1. Pure Functions - No Side Effects**

```python
# Pure function - same input always gives same output
def calculate_area(length, width):
    return length * width

# Always returns same result for same inputs
area1 = calculate_area(5, 3)  # Always 15
area2 = calculate_area(5, 3)  # Always 15

# Pure function with multiple calculations
def calculate_compound_interest(principal, rate, time):
    """Calculate compound interest - pure function"""
    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal) ** time
    return amount

# Test purity
result1 = calculate_compound_interest(1000, 5, 10)
result2 = calculate_compound_interest(1000, 5, 10)
print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Results are identical: {result1 == result2}")

# Pure function for data transformation
def format_currency(amount, currency="USD"):
    """Format amount as currency - pure function"""
    if currency == "USD":
        return f"${amount:,.2f}"
    elif currency == "EUR":
        return f"€{amount:,.2f}"
    else:
        return f"{amount:,.2f} {currency}"

# Test formatting
print(format_currency(1234.56))      # $1,234.56
print(format_currency(1234.56, "EUR"))  # €1,234.56
print(format_currency(1234.56, "GBP"))  # 1,234.56 GBP
```

## **2. Functions with Side Effects - Modifying State**

```python
# Function with side effects (prints, modifies global state)
total_calls = 0

def log_and_add(a, b):
    global total_calls
    total_calls += 1
    print(f"Call #{total_calls}: Adding {a} and {b}")
    return a + b

result = log_and_add(2, 3)  # Has side effects: prints and modifies global
print(f"Total calls: {total_calls}")

# Function that modifies input (side effect)
def add_to_list(items, new_item):
    """Add item to list - modifies input"""
    items.append(new_item)
    return len(items)

my_list = [1, 2, 3]
print("Before:", my_list)
new_length = add_to_list(my_list, 4)
print("After:", my_list)
print("New length:", new_length)

# Function with file I/O side effects
def log_to_file(message, filename="app.log"):
    """Write message to log file - side effect"""
    from datetime import datetime
    timestamp = datetime.now().isoformat()
    log_entry = f"{timestamp}: {message}\n"

    with open(filename, "a") as f:
        f.write(log_entry)

    return len(log_entry)

# Test logging
log_length = log_to_file("Application started")
print(f"Logged {log_length} characters")

# Function that modifies database (side effect)
def update_user_status(user_id, status):
    """Update user status in database - side effect"""
    # Simulate database update
    print(f"Updating user {user_id} status to {status}")

    # In real application, this would modify database
    # database.update_user(user_id, {"status": status})

    return True

# Test database update
success = update_user_status(123, "active")
print(f"Update successful: {success}")
```

## **3. Higher-Order Functions - Functions as Parameters**

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

def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
doubled = apply_operation(numbers, double)
cubed = apply_operation(numbers, cube)

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Doubled: {doubled}")
print(f"Cubed: {cubed}")

# Higher-order function with filtering
def filter_numbers(numbers, predicate):
    """Filter numbers based on predicate function"""
    filtered = []
    for num in numbers:
        if predicate(num):
            filtered.append(num)
    return filtered

def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# Test filtering
test_numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter_numbers(test_numbers, is_even)
positive_numbers = filter_numbers(test_numbers, is_positive)
prime_numbers = filter_numbers(test_numbers, is_prime)

print(f"Even numbers: {even_numbers}")
print(f"Positive numbers: {positive_numbers}")
print(f"Prime numbers: {prime_numbers}")

# Higher-order function that returns functions
def create_comparator(operation):
    """Create comparison function based on operation"""
    if operation == "ascending":
        return lambda x, y: x < y
    elif operation == "descending":
        return lambda x, y: x > y
    else:
        return lambda x, y: x == y

# Use returned functions
asc_comp = create_comparator("ascending")
desc_comp = create_comparator("descending")

print(f"5 < 3 (ascending): {asc_comp(5, 3)}")
print(f"5 > 3 (descending): {desc_comp(5, 3)}")
```

---

# **LAMBDA FUNCTIONS - Anonymous Functions**

## **1. Basic Lambda Functions - Simple Operations**

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

# Lambda with no parameters
get_pi = lambda: 3.14159
print(get_pi())  # Output: 3.14159

# Lambda with conditional expression
max_val = lambda a, b: a if a > b else b
print(max_val(10, 5))  # Output: 10

# Lambda for string operations
capitalize = lambda s: s.upper()
reverse = lambda s: s[::-1]

print(capitalize("hello"))  # HELLO
print(reverse("python"))    # nohtyp
```

## **2. Lambda in Higher-Order Functions - Practical Usage**

```python
# Lambda with map function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(f"Squared: {squared}")  # [1, 4, 9, 16, 25]

# Lambda with filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # [2, 4]

# Lambda with sorted function
names = ["Alice", "Bob", "Charlie", "David"]
sorted_by_length = sorted(names, key=lambda name: len(name))
print(f"Sorted by length: {sorted_by_length}")

# Lambda with custom sorting
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade (descending)
sorted_by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print("Sorted by grade:")
for student in sorted_by_grade:
    print(f"{student['name']}: {student['grade']}")

# Lambda with reduce function
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of all numbers: {product}")  # 120

# Lambda for data transformation
data = [("apple", 5), ("banana", 3), ("cherry", 8)]
formatted = list(map(lambda item: f"{item[0]}: {item[1]}", data))
print(f"Formatted: {formatted}")

# Lambda with multiple conditions
def categorize_age(age):
    return (lambda x: "child" if x < 13 else
                   "teen" if x < 18 else
                   "adult" if x < 65 else
                   "senior")(age)

# Test categorization
ages = [10, 15, 25, 70]
categories = [categorize_age(age) for age in ages]
print(f"Ages: {ages}")
print(f"Categories: {categories}")
```

---

# **DEBUGGING FUNCTIONS - Troubleshooting and Testing**

## **1. Using Print Statements for Debugging**

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

# Debug function with multiple return points
def validate_user_data(name, age, email):
    print(f"DEBUG: Validating {name}, age {age}, email {email}")

    if not name or len(name) < 2:
        print("DEBUG: Name validation failed")
        return False, "Name must be at least 2 characters"

    if age < 13 or age > 120:
        print("DEBUG: Age validation failed")
        return False, "Age must be between 13 and 120"

    if "@" not in email or "." not in email.split("@")[1]:
        print("DEBUG: Email validation failed")
        return False, "Invalid email format"

    print("DEBUG: All validations passed")
    return True, "Valid user data"

# Test validation
test_cases = [
    ("A", 25, "valid@email.com"),      # Name too short
    ("Alice", 10, "valid@email.com"),   # Age too young
    ("Alice", 25, "invalid-email"),     # Invalid email
    ("Alice", 25, "valid@email.com")    # All valid
]

for name, age, email in test_cases:
    is_valid, message = validate_user_data(name, age, email)
    print(f"Result: {is_valid}, Message: {message}")
```

## **2. Using Return Values for Debugging**

```python
def safe_divide(a, b):
    """Safe division with error handling"""
    try:
        result = a / b
        return result, None
    except ZeroDivisionError:
        return None, "Division by zero"
    except TypeError:
        return None, "Invalid types for division"

# Test safe division
test_cases = [(10, 2), (10, 0), ("10", 2), (10, "2")]

for a, b in test_cases:
    result, error = safe_divide(a, b)
    if error:
        print(f"Error dividing {a} by {b}: {error}")
    else:
        print(f"{a} / {b} = {result}")

# Function with comprehensive error reporting
def process_data(data_list):
    """Process data with detailed error reporting"""
    results = []
    errors = []

    for i, item in enumerate(data_list):
        try:
            # Process item
            if isinstance(item, (int, float)):
                processed = item * 2
            elif isinstance(item, str):
                processed = item.upper()
            else:
                raise TypeError(f"Unsupported type: {type(item).__name__}")

            results.append(processed)

        except Exception as e:
            error_info = {
                "index": i,
                "item": item,
                "error_type": type(e).__name__,
                "error_message": str(e)
            }
            errors.append(error_info)

    return {
        "successful": results,
        "errors": errors,
        "total_processed": len(data_list),
        "success_rate": len(results) / len(data_list) if data_list else 0
    }

# Test data processing
test_data = [1, 2, "hello", 3.14, None, "world", 5]
result = process_data(test_data)

print("Processing Results:")
print(f"Successful: {result['successful']}")
print(f"Errors: {result['errors']}")
print(f"Success rate: {result['success_rate']:.1%}")
```

---

# **RUNNING SCRIPTS SAFELY - The Main Guard**

## **1. Understanding the Main Guard Pattern**

```python
def run_converter():
    print("Running the converter loop...")
    # ... main loop here ...

if __name__ == "__main__":
    # This block runs ONLY when the file is executed directly:
    # python unit_converter_v2.py
    run_converter()

# Why this matters
# When Python loads a file, it sets a built-in variable `__name__`.
# If the file is executed directly, `__name__ == "__main__"`.
# If the file is imported from another file, `__name__` becomes the module name, so the guarded block does NOT run.
# This lets you keep reusable functions importable without triggering the script's CLI logic.

# Quick check
print("Module name:", __name__)

def add(a, b):
    return a + b

if __name__ == "__main__":
    # Runs only when this file is executed directly
    print(add(2, 3))

# Mini‑drill
# 1. Add `print("Module:", __name__)` near the top of a script and run it with `python your_file.py`.
# 2. Observe it prints `__main__`.
# 3. Create another file and `import your_file`; observe the printed module name is `your_file` and the guarded block does not run.
```

## **2. Practical Main Guard Examples**

```python
# Example 1: Calculator with main guard
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)
    else:
        result = "Invalid choice"

    print(f"Result: {result}")

if __name__ == "__main__":
    main()

# Example 2: Data processor with main guard
def process_file(filename):
    """Process data file"""
    try:
        with open(filename, 'r') as f:
            data = f.read()
        return f"Processed {len(data)} characters from {filename}"
    except FileNotFoundError:
        return f"File {filename} not found"

def analyze_data(data):
    """Analyze data"""
    lines = data.split('\n')
    words = data.split()
    return f"Lines: {len(lines)}, Words: {len(words)}"

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        return

    filename = sys.argv[1]
    result = process_file(filename)
    print(result)

if __name__ == "__main__":
    main()

# Example 3: Module with utility functions
def format_currency(amount, currency="USD"):
    """Format amount as currency"""
    if currency == "USD":
        return f"${amount:,.2f}"
    elif currency == "EUR":
        return f"€{amount:,.2f}"
    else:
        return f"{amount:,.2f} {currency}"

def calculate_tax(income, rate=0.15):
    """Calculate tax on income"""
    return income * rate

# Test functions when run directly
if __name__ == "__main__":
    print("Testing utility functions:")
    print(f"Currency: {format_currency(1234.56)}")
    print(f"Tax: {format_currency(calculate_tax(50000))}")
```

---

# **COMMON FUNCTION PATTERNS - Real-World Applications**

## **1. Input Validation Pattern**

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

# Enhanced validation pattern
def validate_and_process(data, validators):
    """Validate data using multiple validator functions"""
    errors = []

    for validator in validators:
        is_valid, error_msg = validator(data)
        if not is_valid:
            errors.append(error_msg)

    if errors:
        return False, errors

    # Process valid data
    processed = process_data(data)
    return True, processed

# Validator functions
def validate_age(data):
    age = data.get('age')
    if not age or not isinstance(age, int) or age < 0 or age > 150:
        return False, "Age must be integer between 0 and 150"
    return True, None

def validate_email(data):
    email = data.get('email', '')
    if '@' not in email or '.' not in email.split('@')[1]:
        return False, "Invalid email format"
    return True, None

def validate_name(data):
    name = data.get('name', '')
    if len(name.strip()) < 2:
        return False, "Name must be at least 2 characters"
    return True, None

# Test validation
test_data = {
    'name': 'A',  # Too short
    'age': 200,   # Too old
    'email': 'invalid-email'  # Invalid format
}

validators = [validate_name, validate_age, validate_email]
is_valid, result = validate_and_process(test_data, validators)

if is_valid:
    print("Data is valid:", result)
else:
    print("Validation errors:", result)
```

## **2. Configuration Pattern**

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

# Advanced configuration pattern
def create_config(base_config, **overrides):
    """Create configuration with overrides"""
    config = base_config.copy()
    config.update(overrides)
    return config

# Base configuration
base_config = {
    "host": "localhost",
    "port": 5432,
    "database": "mydb",
    "timeout": 30,
    "max_connections": 100,
    "debug": False
}

# Create different configurations
dev_config = create_config(base_config, debug=True, database="dev_db")
prod_config = create_config(base_config, host="prod.db", max_connections=500)

print("Development config:", dev_config)
print("Production config:", prod_config)
```

## **3. Factory Pattern**

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

# Enhanced factory pattern
def create_data_processor(processor_type, **options):
    """Create data processor based on type"""
    if processor_type == "csv":
        return CSVProcessor(**options)
    elif processor_type == "json":
        return JSONProcessor(**options)
    elif processor_type == "xml":
        return XMLProcessor(**options)
    else:
        raise ValueError(f"Unknown processor type: {processor_type}")

# Mock processor classes
class CSVProcessor:
    def __init__(self, delimiter=",", encoding="utf-8"):
        self.delimiter = delimiter
        self.encoding = encoding

    def process(self, data):
        return f"Processing CSV with delimiter '{self.delimiter}' and encoding '{self.encoding}'"

class JSONProcessor:
    def __init__(self, pretty_print=False):
        self.pretty_print = pretty_print

    def process(self, data):
        return f"Processing JSON with pretty_print={self.pretty_print}"

class XMLProcessor:
    def __init__(self, root_element="data"):
        self.root_element = root_element

    def process(self, data):
        return f"Processing XML with root element '{self.root_element}'"

# Test factory
try:
    csv_processor = create_data_processor("csv", delimiter=";", encoding="latin-1")
    json_processor = create_data_processor("json", pretty_print=True)
    xml_processor = create_data_processor("xml", root_element="users")

    print(csv_processor.process("data"))
    print(json_processor.process("data"))
    print(xml_processor.process("data"))

except ValueError as e:
    print(f"Error: {e}")
```

---

# **KEY CONCEPTS SUMMARY**

## **Function Definition**

- `def function_name(parameters):` - Define a function
- `return value` - Return a value from function
- Function names should be verbs in snake_case
- Use descriptive names that explain what the function does

## **Parameters and Arguments**

- **Positional arguments** - Order matters
- **Keyword arguments** - Named parameters, order doesn't matter
- **Default parameters** - Optional with default values
- **\*args** - Variable number of positional arguments
- **\*\*kwargs** - Variable number of keyword arguments
- **Mixed arguments** - Positional first, then keyword

## **Scope**

- **Local scope** - Variables inside function
- **Global scope** - Variables outside all functions
- **global keyword** - Modify global variables inside functions
- **Variable shadowing** - Local variables hide global ones
- **Nested functions** - Functions inside functions
- **Closures** - Inner functions remember outer variables

## **Function Types**

- **Pure functions** - No side effects, same input → same output
- **Functions with side effects** - Modify global state or print
- **Higher-order functions** - Take functions as parameters
- **Lambda functions** - Anonymous functions for simple operations

## **Best Practices**

- Functions should do one thing well
- Use descriptive names for functions and parameters
- Keep functions small and focused
- Use return values rather than printing when possible
- Validate input parameters
- Use default parameters for optional settings
- Avoid mutable default arguments
- Use main guard for script execution

## **Common Patterns**

- Input validation with error handling
- Configuration functions with defaults
- Factory functions that create other functions
- Debugging with print statements and return codes
- Pure functions for calculations
- Side-effect functions for I/O operations

## **Debugging**

- Use print statements to trace execution
- Return error codes and messages
- Test functions with different inputs
- Use meaningful variable names
- Break complex functions into smaller ones
- Use main guard for testing

---

This comprehensive guide covers **all the different ways** to work with Python functions. Master these patterns to write clean, reusable, and maintainable code that organizes your programs effectively and follows Python best practices.
