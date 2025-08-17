# Variable = A container for a value (string, integer, float, boolean) A variable behaves as if it was the value it contains.

# strings

```bash
first_name = "Bro"
food = "pizza"
```

# integers

```bash
age = 25
quality = 3
num_of_students = 30
```

# float

```bash
price = 10.99
gpa = 3.2
distance = 5.5
```

# boolean

```bash
is_student = True  # or False
```

# Typecasting = the process of converting a variable from one data type to another str(), int(), float(), bool()

# input() = A function that prompts the user to enter data. Returns the entered data as a string

# ADVANCED STRING METHODS & TECHNIQUES

# String Methods - strip(), replace(), len(), find(), rfind(), upper(), lower(), capitalize(), title(), startswith(), endswith(), count(), index()

```bash
# strip(): Removes leading/trailing whitespace (or specified characters)
password = " P@ssw0rd! "
clean_password = password.strip()                # -> "P@ssw0rd!"
custom_strip = "---hello---".strip("-")         # -> "hello"

# replace(old, new[, count]): Returns a copy with replacements; optional count limits how many
alt_password = clean_password.replace("@", "a")  # -> "Passw0rd!"
masked = "banana".replace("a", "*")             # -> "b*n*n*"
limited = "ha ha ha".replace("ha", "ho", 1)     # -> "ho ha ha"

# len(obj): Built-in function that returns number of items/characters
msg = "hello"
length = len(msg)                                 # -> 5

# find(substring): Returns the lowest index where substring is found, -1 if not found
quote = "knowledge is power"
position = quote.find("is")    # -> 10
missing = quote.find("hello")  # -> -1

# rfind(substring): Returns the highest index where substring is found, -1 if not found
text = "banana"
last_pos = text.rfind("a")     # -> 5

# upper(): Converts all characters to uppercase
word = "python"
shout = word.upper()             # -> "PYTHON"

# lower(): Converts all characters to lowercase
shout.lower()                    # -> "python"

# capitalize(): Makes first character uppercase, rest lowercase
greeting = "hELLO"
fixed = greeting.capitalize()    # -> "Hello"

# title(): Capitalizes first letter of each word
sentence = "learn python fast"
titled = sentence.title()        # -> "Learn Python Fast"

# startswith(prefix): Checks if string starts with given prefix
url = "https://openai.com"
url.startswith("https")          # -> True

# endswith(suffix): Checks if string ends with given suffix
filename = "report.pdf"
filename.endswith(".pdf")       # -> True

# count(substring): Returns the number of non-overlapping occurrences
phrase = "ha ha ha"
laughs = phrase.count("ha")      # -> 3

# index(substring): Like find() but raises an error if not found
word = "banana"
idx = word.index("n")            # -> 2
```

# String Slicing

```bash
# String slicing: Access parts of a string using [start:end:step]
name = "amirofcodes"
part1 = name[0:5]       # -> "amiro" (from index 0 up to, but not including, 5)
part2 = name[5:]        # -> "fcodes" (from index 5 to the end)
part3 = name[:4]        # -> "amir" (from beginning up to index 4)
part4 = name[::2]       # -> "aiooe" (every 2nd character)
reversed_name = name[::-1]  # -> "sedocforima" (reverses string)
```

# String Membership & Boolean Operators

```bash
# Membership operators: 'in' and 'not in'
text = "Python is fun"
"Python" in text        # -> True
"java" in text          # -> False
"java" not in text      # -> True

# Boolean operators: and, or, not
x = True
y = False

result1 = x and y       # -> False (both must be True)
result2 = x or y        # -> True  (at least one must be True)
result3 = not x         # -> False (negates the value)

# Combined usage
username = "amirofcodes"
valid = ("amiro" in username) and (len(username) > 5)   # -> True
```

# Escape Sequences & Multi-line Strings

```bash
# Escape sequences: special characters inside strings
newline = "Hello\nWorld"     # -> "Hello" (new line) "World"
tabbed = "1\t2\t3"          # -> "1    2    3"
quote = "She said, \"hi!\""  # -> She said, "hi!"

# Multi-line strings: triple quotes
poem = """Roses are red,
Violets are blue,
Python is fun,
And so are you."""
```

# NUMBER FORMATTING & ARITHMETIC

```bash
# Basic arithmetic: +, -, *, /, // (floor division), % (modulus), ** (exponent)
a = 10
b = 3
add = a + b     # -> 13
sub = a - b     # -> 7
mul = a * b     # -> 30
div = a / b     # -> 3.333...
floor = a // b  # -> 3
mod = a % b     # -> 1
exp = a ** b    # -> 1000

# Number formatting with f-strings
price = 1234.5678
formatted = f"${price:,.2f}"   # -> "1,234.57"
```

# Rounding & Type Conversion

```bash
# round(number, ndigits): round to decimals
pi = 3.14159
rounded = round(pi, 2)   # -> 3.14

# int(): convert to integer (truncates)
int(3.9)   # -> 3

# float(): convert to float
float(5)   # -> 5.0
```

# Formatted Strings with Number Formatting

```bash
# f-strings allow embedding expressions with formatting
name = "Amiro"
balance = 9876.54321
msg = f"Hello {name}, your balance is ${balance:,.2f}"
# -> "Hello Amiro, your balance is $9,876.54"
```

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
