# Variable = A container for a value (string, integer, float, boolean) A variable behaves as if it was the value it contains.

# strings

```bash
first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")
```

# integers

```bash
age = 25
quality = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")
```

# float

```bash
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"'You ran{distance}km")
```

# boolean

```bash
is_student = True # or False

print(f"Are you a student?: {is_student}")

if is_student:
print("You are a student")
else:
print("You are NOT a student")
```

# Typecasting = the process of converting a variable from one data type to another str(), int(), float(), bool()

# input() = A function that prompts the user to enter data. Returns the entered data as a string

```bash
name = input("What is your name?: ")
age = input("How old are you?: ")
age = int (age)
age = age + 1

print(f"Hello {name}!")
print ("HAPPY BIRTHDAY!")
print(f"You will be {age} years old next year")
```

# Exercise 1 Rectangle Area Calc

```bash
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length \* width
print(f"The area is: {area}cm²")
```

# Exercise 2 Shopping Cart Program

```bash
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price \* quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: €{total)")
```

---

# ADVANCED STRING METHODS & TECHNIQUES

# String Methods - strip(), replace(), len()

```bash
password = " P@ssw0rd! "
clean_password = password.strip()  # Removes leading/trailing spaces
alt_password = clean_password.replace("@", "a")  # Replaces @ with a
print(f"After cleaning: {alt_password}, length: {len(alt_password)}")
```

# String Slicing & find() method

```bash
# Extract file extension
path = input("Enter file path: ").strip()
dot = path.rfind(".")  # Find last occurrence of .
extension = path[dot:]  # Slice from dot to end
print(f"File extension: {extension}")

# Extract names from "John Doe"
full_name = "John Doe"
space_pos = full_name.find(" ")  # Find position of space
first_name = full_name[:space_pos]  # Slice from start to space
last_name = full_name[space_pos + 1:]  # Slice from after space to end
print(f"First: {first_name}, Last: {last_name}")
```

# String Membership & Boolean Operators

```bash
# Email validation
email = input("Enter email: ").strip()
is_valid = "@" in email and "." in email  # Check both conditions
print(f"Email valid: {is_valid}")

# String length and case conversion
quote = "Talk is cheap. Show me the code."
print(f"Length: {len(quote)}")
print(f"Last word uppercase: {quote[-5:-1].upper()}")
```

# Escape Sequences & Multi-line Strings

```bash
# Using \n for line breaks
sentence = "This spans\nmultiple lines\nwith escape sequences"
print(sentence)

# Using triple quotes for multi-line
multi_line = """This is a multi-line string
that spans several lines
and preserves formatting"""
word_count = len(multi_line.split())  # Count words, not characters
print(f"Total words: {word_count}")
```

---

# NUMBER FORMATTING & ARITHMETIC

# Rounding & Type Conversion

```bash
pi = 3.14159
rounded_pi = round(pi, 2)  # Round to 2 decimal places
integer_pi = int(pi)  # Convert to integer (truncates)
print(f"Rounded: {rounded_pi}, Integer: {integer_pi}")
```

# Formatted Strings with Number Formatting

```bash
big_number = 1234567.89
formatted = f"{big_number:,.2f}"  # Thousands separator + 2 decimals
print(formatted)  # Output: 1,234,567.89

# Temperature conversion with formatting
celsius = float(input("Enter Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")
```

# Compound Interest & Exponentiation

```bash
P = 100  # Principal
r = 0.04  # Rate (4%)
n = 5     # Years
A = P * (1 + r) ** n  # Compound interest formula
print(f"Final amount: €{round(A, 2)}")
```

---

# VARIABLE NAMING CONVENTIONS

# Python prefers snake_case

```bash
# Good (Pythonic)
snake_case_variable = "I follow Python convention"
user_name = "John"
total_price = 99.99

# Works but not Pythonic
camelCaseVariable = "I'm from other languages"
userName = "John"
totalPrice = 99.99

print(snake_case_variable)  # Python prefers this
print(camelCaseVariable)    # Works but not conventional
```

---

# MULTIPLE ASSIGNMENT & SWAPPING

```bash
# Swap variables without temp
a = 10
b = 5
a, b = b, a  # Multiple assignment
print(f"a: {a}, b: {b}")  # a: 5, b: 10

# Multiple variable assignment
x, y, z = 1, 2, 3
print(f"x: {x}, y: {y}, z: {z}")
```

---

# KEY CONCEPTS SUMMARY

## String Manipulation

- `strip()` - Remove leading/trailing whitespace
- `replace(old, new)` - Replace characters/strings
- `find(char)` - Find position of character
- `rfind(char)` - Find last position of character
- `upper()` - Convert to uppercase
- `split()` - Convert string to list of words

## Number Operations

- `round(number, decimals)` - Round to specified decimals
- `int()` - Convert to integer (truncates)
- `float()` - Convert to float
- `**` - Exponentiation operator
- `f"{var:,.2f}"` - Format with thousands separator and 2 decimals

## Boolean Logic

- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `in` - Check if substring exists in string
- `not` - Negate boolean value

## String Slicing

- `string[start:end]` - Slice from start to end (exclusive)
- `string[start:]` - Slice from start to end
- `string[:end]` - Slice from beginning to end
- `string[start:end:step]` - Slice with step

## Type Conversion

- `str()` - Convert to string
- `int()` - Convert to integer
- `float()` - Convert to float
- `bool()` - Convert to boolean

## Best Practices

- Use snake_case for variable names
- Always strip() user input
- Use f-strings for formatted output
- Handle type conversion safely
- Use descriptive variable names
