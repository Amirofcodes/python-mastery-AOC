# 01 · Primitive Types - Comprehensive Mastery Guide

Master Python's fundamental building blocks through complete understanding of **all the different ways** to create, manipulate, format, and work with strings, numbers, booleans, and variables.

---

## **Mental Model: Python's Core Data Types**

- **String** `str`: Text data - immutable sequences of characters
- **Integer** `int`: Whole numbers with unlimited precision  
- **Float** `float`: Decimal numbers with floating-point precision
- **Boolean** `bool`: True/False values (subclass of int)
- **Variable**: Name that refers to a value in memory

---

# **STRINGS - Text Data Mastery**

## **1. Creating Strings - All Methods**

```python
# Method 1: Single quotes (most common)
name = 'Alice'
message = 'Hello World'

# Method 2: Double quotes (allows single quotes inside)
greeting = "Hello, it's a beautiful day!"
quote = "She said, 'Hello there!'"

# Method 3: Triple quotes (multi-line strings)
long_text = """This is a multi-line string
that spans several lines
and preserves formatting"""

paragraph = '''You can also use
triple single quotes
for multi-line strings'''

# Method 4: String constructor
from_number = str(42)          # "42"
from_list = str([1, 2, 3])     # "[1, 2, 3]"
empty_string = str()           # ""

# Method 5: Raw strings (escape sequences ignored)
file_path = r"C:\Users\name\Documents\file.txt"
regex_pattern = r"\d+\.\d+"

# Method 6: Formatted strings (f-strings)
age = 25
formatted = f"I am {age} years old"

# Method 7: Bytes to string
byte_data = b"Hello"
decoded = byte_data.decode('utf-8')  # "Hello"
```

## **2. String Manipulation - All Methods**

```python
text = "  Hello, Python World!  "

# Case conversion methods
upper = text.upper()           # "  HELLO, PYTHON WORLD!  "
lower = text.lower()           # "  hello, python world!  "
title = text.title()           # "  Hello, Python World!  "
capitalize = text.capitalize() # "  hello, python world!  "
swapcase = text.swapcase()     # "  hELLO, pYTHON wORLD!  "

# Whitespace methods
stripped = text.strip()        # "Hello, Python World!"
left_strip = text.lstrip()     # "Hello, Python World!  "
right_strip = text.rstrip()    # "  Hello, Python World!"
stripped_chars = text.strip(' !') # "Hello, Python World"

# Replacement methods
replaced = text.replace("Python", "Java")     # Replace all occurrences
replaced_once = text.replace("o", "0", 1)     # Replace first occurrence only
translated = text.translate(str.maketrans("o", "0"))  # Character translation

# Split and join methods
words = text.strip().split()                  # ["Hello,", "Python", "World!"]
split_comma = text.split(",")                 # ["  Hello", " Python World!  "]
split_max = text.split(" ", 2)                # Split max 2 times
joined = " ".join(["Hello", "Python"])        # "Hello Python"
joined_custom = "-".join(["a", "b", "c"])     # "a-b-c"

# Partition methods
partition = text.partition("Python")          # ("  Hello, ", "Python", " World!  ")
rpartition = text.rpartition(" ")            # ("  Hello, Python", " ", "World!  ")
```

## **3. String Searching and Testing - All Methods**

```python
text = "Hello, Python Programming"

# Finding positions
find_pos = text.find("Python")               # 7 (returns -1 if not found)
rfind_pos = text.rfind("o")                  # 18 (last occurrence)
index_pos = text.index("Python")             # 7 (raises ValueError if not found)
rindex_pos = text.rindex("o")                # 18 (raises ValueError if not found)

# Counting occurrences
count_o = text.count("o")                    # 2
count_range = text.count("o", 0, 10)         # 1 (count in range)

# Membership testing
has_python = "Python" in text               # True
no_java = "Java" not in text                # True

# String testing methods
is_alpha = text.isalpha()                   # False (has comma and space)
is_digit = "12345".isdigit()                # True
is_alnum = "Hello123".isalnum()             # True
is_space = "   ".isspace()                  # True
is_upper = "HELLO".isupper()                # True
is_lower = "hello".islower()                # True
is_title = "Hello World".istitle()          # True

# Advanced testing
starts_hello = text.startswith("Hello")     # True
ends_ing = text.endswith("ing")             # True
starts_multiple = text.startswith(("Hi", "Hello"))  # True (tuple of options)
```

## **4. String Slicing - All Patterns**

```python
text = "Python Programming"

# Basic slicing [start:stop:step]
first_char = text[0]           # "P"
last_char = text[-1]           # "g"
first_three = text[:3]         # "Pyt"
last_three = text[-3:]         # "ing"
middle = text[2:8]             # "thon "
every_second = text[::2]       # "Pto rgamn"
reversed_text = text[::-1]     # "gnimmargorP nohtyP"

# Advanced slicing patterns
skip_first_last = text[1:-1]   # "ython Programmin"
every_third = text[::3]        # "Ph rmn"
reverse_slice = text[10:5:-1]  # "amrgr" (reverse slice)

# Negative step slicing
backwards_range = text[15:8:-1] # "mmargro"
```

## **5. String Formatting - All Methods**

```python
name = "Alice"
age = 30
price = 1234.56

# Method 1: f-strings (modern, preferred)
f_string = f"Hello {name}, you are {age} years old"
f_format = f"Price: ${price:,.2f}"           # "Price: $1,234.56"
f_expression = f"Next year: {age + 1}"       # "Next year: 31"

# Method 2: .format() method
format_basic = "Hello {}, you are {}".format(name, age)
format_named = "Hello {name}, age {age}".format(name=name, age=age)
format_positional = "Hello {0}, you are {1}".format(name, age)
format_number = "Price: ${:.2f}".format(price)

# Method 3: % formatting (older style)
percent_basic = "Hello %s, you are %d" % (name, age)
percent_format = "Price: $%.2f" % price

# Advanced formatting
padding = f"{name:>10}"        # Right-align in 10 chars: "     Alice"
left_pad = f"{name:<10}"       # Left-align: "Alice     "
center = f"{name:^10}"         # Center: "  Alice   "
fill_char = f"{name:*^10}"     # Center with *: "**Alice***"

# Number formatting
binary = f"{42:b}"             # "101010"
hex_val = f"{255:x}"           # "ff"
octal = f"{64:o}"              # "100"
scientific = f"{1234.5:e}"     # "1.234500e+03"
percentage = f"{0.15:.2%}"      # "15.00%"
```

## **6. String Validation Patterns**

```python
def validate_email(email):
    """Multiple validation approaches"""
    # Method 1: Simple containment check
    basic_valid = "@" in email and "." in email
    
    # Method 2: More thorough checking
    parts = email.split("@")
    if len(parts) != 2:
        return False
    username, domain = parts
    return bool(username) and "." in domain
    
    # Method 3: Using string methods
    return (email.count("@") == 1 and 
            not email.startswith("@") and 
            not email.endswith("@") and
            "." in email.split("@")[1])

def clean_input(text):
    """All cleaning methods"""
    # Strip whitespace
    cleaned = text.strip()
    
    # Remove extra spaces
    single_spaces = " ".join(cleaned.split())
    
    # Title case for names
    title_case = single_spaces.title()
    
    return title_case

# Usage examples
email_test = "user@example.com"
print(validate_email(email_test))  # True

messy_name = "  jOhN   dOE  "
clean_name = clean_input(messy_name)  # "John Doe"
```

---

# **NUMBERS - Numeric Data Mastery**

## **1. Creating Numbers - All Methods**

```python
# Method 1: Integer literals
positive_int = 42
negative_int = -17
zero = 0
big_int = 123456789012345678901234567890  # Unlimited precision

# Method 2: Different bases
binary = 0b1010        # 10 in decimal
octal = 0o755          # 493 in decimal  
hexadecimal = 0xFF     # 255 in decimal

# Method 3: Float literals
positive_float = 3.14
negative_float = -2.5
scientific = 1.23e4    # 12300.0
small_sci = 5e-3       # 0.005

# Method 4: Constructor functions
from_string = int("42")           # 42
from_float = int(3.9)             # 3 (truncates)
from_bool = int(True)             # 1
base_conversion = int("FF", 16)   # 255 (from hex)
binary_conv = int("1010", 2)      # 10 (from binary)

float_from_str = float("3.14")    # 3.14
float_from_int = float(42)        # 42.0
infinity = float('inf')           # inf
neg_infinity = float('-inf')      # -inf
not_a_number = float('nan')       # nan

# Method 5: Complex numbers
complex_basic = 3 + 4j
complex_func = complex(3, 4)      # (3+4j)
complex_from_str = complex("3+4j") # (3+4j)
```

## **2. Number Operations - All Types**

```python
a = 17
b = 5
x = 3.14
y = 2.5

# Basic arithmetic
addition = a + b        # 22
subtraction = a - b     # 12
multiplication = a * b  # 85
division = a / b        # 3.4 (always returns float)
floor_division = a // b # 3 (integer division)
modulo = a % b          # 2 (remainder)
exponent = a ** b       # 1419857 (17^5)

# Augmented assignment operators
a += 5                  # a = a + 5
a -= 3                  # a = a - 3
a *= 2                  # a = a * 2
a /= 4                  # a = a / 4
a //= 2                 # a = a // 2
a %= 3                  # a = a % 3
a **= 2                 # a = a ** 2

# Comparison operations
equal = (a == b)        # False
not_equal = (a != b)    # True
greater = (a > b)       # True
less = (a < b)          # False
greater_equal = (a >= b) # True
less_equal = (a <= b)   # False

# Built-in math functions
absolute = abs(-42)     # 42
rounded = round(3.7)    # 4
rounded_places = round(3.14159, 2)  # 3.14
minimum = min(1, 5, 3)  # 1
maximum = max(1, 5, 3)  # 5
sum_values = sum([1, 2, 3, 4])  # 10
```

## **3. Number Conversion - All Methods**

```python
# String to number conversion
int_from_str = int("42")
float_from_str = float("3.14")
complex_from_str = complex("1+2j")

# Base conversion
decimal_num = 255
binary_str = bin(decimal_num)     # '0b11111111'
octal_str = oct(decimal_num)      # '0o377'
hex_str = hex(decimal_num)        # '0xff'

# Custom base conversion
def to_base(num, base):
    if num == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num:
        result = digits[num % base] + result
        num //= base
    return result

base_5 = to_base(42, 5)  # "132"

# Number to string conversion
str_from_int = str(42)           # "42"
str_from_float = str(3.14)       # "3.14"

# Type checking and conversion
def safe_int_convert(value):
    """Safe conversion with error handling"""
    try:
        return int(value)
    except ValueError:
        return None
    except TypeError:
        return None

result = safe_int_convert("42")    # 42
result2 = safe_int_convert("abc")  # None
```

## **4. Number Formatting - All Patterns**

```python
number = 1234567.89
small_num = 0.00123
percentage = 0.157

# Basic formatting
two_decimals = f"{number:.2f}"        # "1234567.89"
comma_separator = f"{number:,}"       # "1,234,567.89"
underscore_sep = f"{number:_}"        # "1_234_567.89"

# Padding and alignment
right_aligned = f"{number:>15.2f}"    # "    1234567.89"
left_aligned = f"{number:<15.2f}"     # "1234567.89    "
center_aligned = f"{number:^15.2f}"   # "  1234567.89  "
zero_padded = f"{number:015.2f}"      # "0001234567.89"

# Scientific notation
scientific = f"{number:e}"            # "1.234568e+06"
scientific_2 = f"{number:.2e}"        # "1.23e+06"

# Different number systems
binary = f"{42:b}"                    # "101010"
octal = f"{42:o}"                     # "52"
hex_lower = f"{255:x}"                # "ff"
hex_upper = f"{255:X}"                # "FF"

# Percentage formatting
percent = f"{percentage:.2%}"         # "15.70%"
percent_0 = f"{percentage:.0%}"       # "16%"

# Sign handling
always_sign = f"{42:+}"               # "+42"
space_positive = f"{42: }"            # " 42"
negative_sign = f"{-42:+}"            # "-42"

# Engineering notation (not built-in, custom function)
def engineering_notation(num):
    """Convert to engineering notation (powers of 1000)"""
    if num == 0:
        return "0"
    
    import math
    exponent = int(math.floor(math.log10(abs(num))))
    eng_exponent = 3 * (exponent // 3)
    mantissa = num / (10 ** eng_exponent)
    
    return f"{mantissa:.3f}e{eng_exponent:+03d}"

eng_format = engineering_notation(1234567)  # "1.235e+006"
```

## **5. Advanced Number Operations**

```python
import math

# Math module functions
sqrt_val = math.sqrt(16)          # 4.0
power = math.pow(2, 3)            # 8.0
log_natural = math.log(math.e)    # 1.0
log_base_10 = math.log10(100)     # 2.0
log_base_2 = math.log2(8)         # 3.0

# Trigonometric functions
sin_val = math.sin(math.pi / 2)   # 1.0
cos_val = math.cos(0)             # 1.0
tan_val = math.tan(math.pi / 4)   # 1.0

# Rounding functions
ceil_val = math.ceil(3.2)         # 4
floor_val = math.floor(3.8)       # 3
trunc_val = math.trunc(3.8)       # 3

# Random numbers (preview)
import random
random_int = random.randint(1, 10)      # Random integer 1-10
random_float = random.random()          # Random float 0.0-1.0
random_choice = random.uniform(1.0, 5.0) # Random float 1.0-5.0

# Number validation
def is_number(value):
    """Check if value can be converted to number"""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def is_integer(value):
    """Check if value is integer"""
    try:
        int(value)
        return str(value).isdigit() or (str(value).startswith('-') and str(value)[1:].isdigit())
    except (ValueError, TypeError):
        return False

print(is_number("42"))      # True
print(is_number("3.14"))    # True
print(is_number("abc"))     # False
print(is_integer("42"))     # True
print(is_integer("3.14"))   # False
```

---

# **BOOLEANS - Truth Value Mastery**

## **1. Creating Boolean Values - All Methods**

```python
# Method 1: Literal values
true_val = True
false_val = False

# Method 2: Boolean constructor
bool_from_int = bool(1)        # True (any non-zero)
bool_from_zero = bool(0)       # False
bool_from_string = bool("hi")  # True (any non-empty)
bool_from_empty = bool("")     # False
bool_from_list = bool([1, 2])  # True (any non-empty)
bool_from_none = bool(None)    # False

# Method 3: Comparison operations
is_equal = (5 == 5)           # True
is_greater = (10 > 5)         # True
is_in_list = (3 in [1, 2, 3]) # True

# Method 4: Logical operations
logical_and = True and True    # True
logical_or = False or True     # True
logical_not = not False        # True
```

## **2. Truthiness Rules - All Cases**

```python
# Falsy values (evaluate to False)
falsy_values = [
    False,          # Boolean False
    0,              # Integer zero
    0.0,            # Float zero
    0j,             # Complex zero
    "",             # Empty string
    [],             # Empty list
    (),             # Empty tuple
    {},             # Empty dictionary
    set(),          # Empty set
    None,           # None value
]

# Everything else is truthy
truthy_values = [
    True,           # Boolean True
    1,              # Any non-zero number
    -1,             # Negative numbers
    0.1,            # Any non-zero float
    "hello",        # Any non-empty string
    " ",            # String with space
    [0],            # List with elements (even falsy ones)
    {"key": False}, # Dict with items
    {0, False},     # Set with elements
]

# Testing truthiness
def test_truthiness(value):
    if value:
        return "Truthy"
    else:
        return "Falsy"

for val in falsy_values:
    print(f"{val!r}: {test_truthiness(val)}")
```

## **3. Logical Operations - All Patterns**

```python
# Basic logical operators
a = True
b = False

# AND operations (all must be true)
and_result = a and b          # False
and_chain = a and True and b  # False
and_short = False and (1/0)   # False (short-circuit, no error)

# OR operations (at least one must be true)
or_result = a or b            # True
or_chain = b or False or a    # True
or_short = True or (1/0)      # True (short-circuit, no error)

# NOT operations (negation)
not_a = not a                 # False
not_b = not b                 # True
double_not = not not a        # True (equivalent to bool(a))

# Complex logical expressions
age = 25
has_license = True
has_car = True

can_drive = age >= 16 and has_license
can_drive_alone = can_drive and (age >= 18 or has_car)
cannot_drive = not (can_drive or age < 16)

# Chained comparisons
x = 10
range_check = 1 < x < 20      # True (equivalent to 1 < x and x < 20)
triple_check = 5 <= x <= 15   # True
ascending = 1 < 5 < 10 < 20   # True
```

## **4. Boolean Context Usage**

```python
# In conditional statements
number = 42
if number:                    # Truthy check
    print("Number exists")

text = "hello"
if not text:                  # Falsy check
    print("No text")
else:
    print("Text exists")

# In while loops
countdown = 5
while countdown:              # Loop while truthy
    print(countdown)
    countdown -= 1

# Default value patterns
name = input("Enter name: ") or "Anonymous"  # Use "Anonymous" if empty
age = int(input("Age: ") or "0")             # Use 0 if empty

# Filtering with boolean context
numbers = [0, 1, 2, 0, 3, 0, 4]
non_zero = [n for n in numbers if n]  # [1, 2, 3, 4]

words = ["", "hello", "", "world", ""]
non_empty = [w for w in words if w]   # ["hello", "world"]

# Boolean return values
def is_valid_password(password):
    """Multiple validation checks"""
    return (len(password) >= 8 and 
            any(c.isdigit() for c in password) and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password))

def has_special_chars(text):
    """Check for special characters"""
    special_chars = "!@#$%^&*"
    return any(char in special_chars for char in text)
```

---

# **VARIABLES - Memory and Assignment**

## **1. Variable Assignment - All Patterns**

```python
# Method 1: Simple assignment
name = "Alice"
age = 25
height = 5.6

# Method 2: Multiple assignment (tuple unpacking)
x, y, z = 1, 2, 3
first_name, last_name = "John", "Doe"

# Method 3: Same value to multiple variables
a = b = c = 0
default_score = initial_lives = max_attempts = 3

# Method 4: Swapping variables
a = 10
b = 20
a, b = b, a  # Now a=20, b=10

# Method 5: Unpacking sequences
coordinates = (3, 4)
x, y = coordinates

point_3d = [1, 2, 3]
x, y, z = point_3d

# Method 6: Star unpacking
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers  # first=1, middle=[2,3,4], last=5
head, *tail = numbers           # head=1, tail=[2,3,4,5]
*init, last = numbers           # init=[1,2,3,4], last=5

# Method 7: Walrus operator (Python 3.8+)
# if (n := len(input("Enter text: "))) > 5:
#     print(f"Text is {n} characters long")
```

## **2. Variable Naming - All Conventions**

```python
# Valid variable names
user_name = "John"           # snake_case (preferred)
userName = "John"            # camelCase (works but not Pythonic)
user_name_2 = "Jane"         # numbers allowed
_private_var = "secret"      # leading underscore (internal use)
__dunder_var = "special"     # double underscore (name mangling)

# Python conventions (PEP 8)
# Constants (uppercase with underscores)
MAX_ATTEMPTS = 3
PI = 3.14159
DEFAULT_TIMEOUT = 30

# Class names (PascalCase) - preview
# class UserAccount:
#     pass

# Function names (snake_case)
def calculate_tax():
    pass

def get_user_input():
    pass

# Invalid variable names (will cause SyntaxError)
# 2variable = "invalid"      # Cannot start with number
# my-variable = "invalid"    # Cannot contain hyphens
# for = "invalid"            # Cannot use keywords
# my variable = "invalid"    # Cannot contain spaces

# Keywords that cannot be used as variable names
import keyword
print("Python keywords:", keyword.kwlist)

# Check if name is valid identifier
def is_valid_name(name):
    return name.isidentifier() and not keyword.iskeyword(name)

print(is_valid_name("user_name"))    # True
print(is_valid_name("2user"))        # False
print(is_valid_name("for"))          # False
```

## **3. Memory and References**

```python
# Understanding variable references
a = [1, 2, 3]
b = a                        # b refers to same object as a
c = a.copy()                 # c refers to new object with same values

a.append(4)
print(a)                     # [1, 2, 3, 4]
print(b)                     # [1, 2, 3, 4] (same object)
print(c)                     # [1, 2, 3] (different object)

# Identity vs equality
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)                # True (same values)
print(x is y)                # False (different objects)
print(x is z)                # True (same object)

# id() function shows memory address
print(id(x))                 # Memory address of x
print(id(y))                 # Different address
print(id(z))                 # Same as x

# Immutable vs mutable types
# Immutable: int, float, str, tuple, bool
name = "Alice"
name_ref = name
name = "Bob"                 # Creates new string object
print(name_ref)              # Still "Alice"

# Mutable: list, dict, set
data = {"name": "Alice"}
data_ref = data
data["name"] = "Bob"         # Modifies existing object
print(data_ref)              # {"name": "Bob"}
```

## **4. Type Checking and Validation**

```python
# Type checking functions
value = 42

# Built-in type() function
print(type(value))           # <class 'int'>
print(type(value).__name__)  # 'int'

# isinstance() function (preferred)
print(isinstance(value, int))           # True
print(isinstance(value, (int, float)))  # True (multiple types)
print(isinstance("hello", str))         # True

# Comprehensive type checker
def analyze_variable(var, name="variable"):
    """Complete variable analysis"""
    print(f"\n--- Analysis of {name} ---")
    print(f"Value: {var!r}")
    print(f"Type: {type(var).__name__}")
    print(f"ID: {id(var)}")
    print(f"Size in bytes: {var.__sizeof__()}")
    
    # Type-specific analysis
    if isinstance(var, str):
        print(f"Length: {len(var)}")
        print(f"Is empty: {not bool(var)}")
        print(f"Is numeric: {var.isdigit() if var else False}")
    elif isinstance(var, (int, float)):
        print(f"Is zero: {var == 0}")
        print(f"Is positive: {var > 0}")
        print(f"Absolute value: {abs(var)}")
    elif isinstance(var, bool):
        print(f"Truthiness: {bool(var)}")
    elif isinstance(var, (list, tuple, dict, set)):
        print(f"Length: {len(var)}")
        print(f"Is empty: {not bool(var)}")

# Usage examples
analyze_variable(42, "number")
analyze_variable("Hello", "greeting")
analyze_variable([1, 2, 3], "numbers_list")
analyze_variable(True, "flag")
```

---

# **INPUT AND OUTPUT MASTERY**

## **1. Input Methods - All Approaches**

```python
# Basic input (always returns string)
name = input("Enter your name: ")
age_str = input("Enter your age: ")

# Input with type conversion
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# Safe input conversion
def safe_int_input(prompt):
    """Safe integer input with validation"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def safe_float_input(prompt):
    """Safe float input with validation"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Input validation patterns
def get_yes_no(prompt):
    """Get yes/no input"""
    while True:
        response = input(prompt + " (y/n): ").lower().strip()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'.")

def get_choice(prompt, choices):
    """Get choice from list of options"""
    while True:
        print(prompt)
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")
        
        try:
            selection = int(input("Enter choice number: ")) - 1
            if 0 <= selection < len(choices):
                return choices[selection]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

# Usage examples
# age = safe_int_input("Enter your age: ")
# continue_game = get_yes_no("Continue playing?")
# color = get_choice("Choose a color:", ["Red", "Green", "Blue"])
```

## **2. Output Formatting - All Methods**

```python
# Basic print statements
print("Hello, World!")
print("Value:", 42)
print("Multiple", "values", "here")

# Print with separators and endings
print("A", "B", "C", sep="-")           # "A-B-C"
print("Loading", end="...")             # "Loading..." (no newline)
print("Done!")                          # "Done!" (continues on same line)

# Print to different outputs
import sys
print("Error message", file=sys.stderr)
print("Regular output", file=sys.stdout)

# String formatting for display
name = "Alice"
age = 30
balance = 1234.56

# F-string formatting (modern)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Balance: ${balance:,.2f}")

# Format method
print("Name: {}".format(name))
print("Balance: ${:.2f}".format(balance))

# Old-style % formatting
print("Name: %s" % name)
print("Balance: $%.2f" % balance)

# Pretty printing for complex data
data = {
    "name": "Alice",
    "age": 30,
    "scores": [85, 92, 78, 94],
    "active": True
}

import pprint
pprint.pprint(data, indent=2, width=40)

# Custom formatting function
def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

def format_percentage(decimal):
    """Format decimal as percentage"""
    return f"{decimal:.1%}"

def format_large_number(num):
    """Format large numbers with suffixes"""
    if abs(num) >= 1_000_000_000:
        return f"{num/1_000_000_000:.1f}B"
    elif abs(num) >= 1_000_000:
        return f"{num/1_000_000:.1f}M"
    elif abs(num) >= 1_000:
        return f"{num/1_000:.1f}K"
    else:
        return str(num)

print(format_currency(1234.56))      # "$1,234.56"
print(format_percentage(0.157))      # "15.7%"
print(format_large_number(1500000))  # "1.5M"
```

---

# **ERROR HANDLING AND VALIDATION**

## **1. Common Conversion Errors**

```python
# Handling ValueError in conversions
def safe_convert_int(value):
    """Safe integer conversion"""
    try:
        return int(value), None
    except ValueError as e:
        return None, f"Cannot convert '{value}' to integer: {e}"

def safe_convert_float(value):
    """Safe float conversion"""
    try:
        return float(value), None
    except ValueError as e:
        return None, f"Cannot convert '{value}' to float: {e}"

# Usage examples
result, error = safe_convert_int("42")
if error:
    print(f"Error: {error}")
else:
    print(f"Converted: {result}")

result, error = safe_convert_int("hello")
if error:
    print(f"Error: {error}")  # Error will be displayed

# Validation functions
def validate_integer_range(value, min_val=None, max_val=None):
    """Validate integer within range"""
    try:
        num = int(value)
        if min_val is not None and num < min_val:
            return False, f"Value must be at least {min_val}"
        if max_val is not None and num > max_val:
            return False, f"Value must be at most {max_val}"
        return True, num
    except ValueError:
        return False, f"'{value}' is not a valid integer"

# Comprehensive input validator
def get_validated_input(prompt, validator_func):
    """Get input with custom validation"""
    while True:
        user_input = input(prompt).strip()
        is_valid, result = validator_func(user_input)
        if is_valid:
            return result
        else:
            print(f"Invalid input: {result}")

# Example usage
def age_validator(value):
    return validate_integer_range(value, 0, 150)

# age = get_validated_input("Enter your age: ", age_validator)
```

---

# **PRACTICAL PATTERNS AND IDIOMS**

## **1. Common Programming Patterns**

```python
# Pattern 1: Default values
name = input("Enter name: ") or "Anonymous"
age = int(input("Enter age: ") or "0")

# Pattern 2: Conditional assignment
status = "adult" if age >= 18 else "minor"
greeting = f"Good {'morning' if hour < 12 else 'afternoon'}"

# Pattern 3: Multiple conditions
def categorize_age(age):
    if age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    elif age < 65:
        return "adult"
    else:
        return "senior"

# Pattern 4: String cleaning pipeline
def clean_text(text):
    """Multi-step text cleaning"""
    return text.strip().lower().replace("  ", " ")

# Pattern 5: Number validation and formatting
def format_price(amount):
    """Format and validate price"""
    try:
        price = float(amount)
        if price < 0:
            raise ValueError("Price cannot be negative")
        return f"${price:.2f}"
    except ValueError as e:
        return f"Invalid price: {e}"

# Pattern 6: Data collection
def collect_user_data():
    """Collect and validate user information"""
    data = {}
    
    # Name validation
    while True:
        name = input("Enter full name: ").strip()
        if len(name) >= 2 and " " in name:
            data['name'] = name.title()
            break
        print("Please enter your full name (first and last)")
    
    # Age validation
    while True:
        try:
            age = int(input("Enter age (0-150): "))
            if 0 <= age <= 150:
                data['age'] = age
                break
            else:
                print("Age must be between 0 and 150")
        except ValueError:
            print("Please enter a valid age")
    
    # Email validation
    while True:
        email = input("Enter email: ").strip().lower()
        if "@" in email and "." in email.split("@")[1]:
            data['email'] = email
            break
        print("Please enter a valid email address")
    
    return data

# Usage
# user_info = collect_user_data()
# print(f"Welcome, {user_info['name']}!")
```

## **2. Performance and Memory Considerations**

```python
# String concatenation performance
# Inefficient (creates new string each time)
def inefficient_join(words):
    result = ""
    for word in words:
        result += word + " "
    return result.strip()

# Efficient (joins at the end)
def efficient_join(words):
    return " ".join(words)

# Memory usage with large strings
def memory_efficient_processing(text):
    """Process text without creating many intermediate strings"""
    # Instead of multiple .replace() calls
    # replacements = [("old1", "new1"), ("old2", "new2")]
    # for old, new in replacements:
    #     text = text.replace(old, new)
    
    # Use translate for multiple character replacements
    translation_table = str.maketrans("aeiou", "AEIOU")
    return text.translate(translation_table)

# Number precision considerations
def safe_float_comparison(a, b, tolerance=1e-9):
    """Compare floats safely"""
    return abs(a - b) < tolerance

# Avoid: 0.1 + 0.2 == 0.3  # False due to floating point precision
# Use: safe_float_comparison(0.1 + 0.2, 0.3)  # True

# Integer performance (Python handles arbitrarily large integers)
large_number = 2 ** 1000  # No problem in Python
print(f"2^1000 has {len(str(large_number))} digits")
```

---

# **KEY CONCEPTS SUMMARY**

## **Strings**
- **Creation**: Single quotes, double quotes, triple quotes, raw strings, f-strings
- **Manipulation**: Case methods, strip methods, replace, split, join
- **Search**: find, rfind, index, count, startswith, endswith
- **Testing**: isalpha, isdigit, isspace, etc.
- **Formatting**: f-strings (preferred), .format(), % formatting

## **Numbers** 
- **Types**: int (unlimited precision), float (64-bit), complex
- **Creation**: Literals, constructors, different bases
- **Operations**: Arithmetic, comparison, built-in functions
- **Conversion**: Between types and bases, safe conversion patterns
- **Formatting**: Decimal places, thousands separators, scientific notation

## **Booleans**
- **Values**: True, False (capital T and F)
- **Truthiness**: Empty containers and None are falsy, everything else truthy
- **Operations**: and, or, not with short-circuit evaluation
- **Usage**: Conditionals, loops, default values

## **Variables**
- **Assignment**: Single, multiple, unpacking, swapping
- **Naming**: snake_case preferred, follow PEP 8 conventions
- **References**: Understand identity vs equality, mutable vs immutable
- **Validation**: Type checking, range validation, safe conversion

## **Best Practices**
- Use descriptive variable names
- Prefer f-strings for formatting
- Always validate user input
- Handle conversion errors gracefully
- Use isinstance() over type() for type checking
- Follow PEP 8 naming conventions
- Understand truthiness rules for clean conditionals

---

This comprehensive guide covers **all the different ways** to work with Python's primitive types. Master these fundamentals - they're the building blocks for everything that follows in your Python journey!
