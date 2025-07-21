# 01_primitive_types - Micro-drills for Variables, Strings, Numbers, Type Conversion
#
# Instructions: Complete each drill by typing the solution yourself.
# Don't copy-paste! The goal is to build muscle memory.

# ===== YOUR COMPLETED DRILLS (1-12) =====

# Drill 1: Variables and F-strings
# Prompt: Create city, country, population variables; print: "Paris, France has 2.15 million people."
city = "Paris"
country = "France"
population = 2.15
print(f"{city}, {country} has {population} million people")

# Drill 2: String methods, slicing, len(), upper()
# Prompt: Given quote = "Talk is cheap. Show me the code.", print its length and last word in UPPERCASE
quote = "Talk is cheap. Show me the code."
print(
    f"quote has {len(quote)} Characters, and the last word is {str.upper(quote[-5: -1])} ")

# Drill 3: input(), type conversion, arithmetic
# Prompt: Ask user's birth year, calculate age in months. Handle string → int conversion
birth_year = int(input("enter your birth year: "))
age_in_months = birth_year * 12
print(f"you are {age_in_months} months old")

# Drill 4: String methods - strip(), replace(), len()
# Prompt: Clean password = " P@ssw0rd! ": strip spaces, replace @ → a, count final characters
password = " P@ssw0rd! "
clean_password = password.strip()
alt_password = clean_password.replace("@", "a")
print(
    f"after stripping we get: {clean_password}, then we replace the @ to get: {alt_password}, with {len(alt_password)} Characters.")

# Drill 5: Numbers - round(), int() casting
# Prompt: For pi = 3.14159, print it rounded to 2 decimals and as an integer
pi = 3.14159
pi1 = int(pi)
pi2 = pi.__round__(2)
print(
    f"pi rounded to 2 decimals is: {pi2}, and type casted to an interger is: {pi1}")

# Drill 6: Escape sequences
# Prompt: Create a sentence spanning 3 lines using \n. Then print it
sentence = "this sentence spans \nthree lines \nby the power of the escape sequences"
print(sentence)

# Drill 7: Multiple assignment, variable names
# Prompt: Swap two numbers without a temp variable using Python's multiple assignment
a = 10
b = 5
a, b = b, a
print(a)
print(b)

# Drill 8: String slicing, rfind() method
# Prompt: Ask for file path, extract and print only the extension (e.g., .png)
path = input("inter file path: ").strip()
dot = path.rfind(".")
extention = path[dot:]
print(f"your file extention is: {extention}")

# Drill 9: Working with numbers - ** operator
# Prompt: Calculate compound interest: €100 at 4% for 5 years using formula A = P(1+r)^n
P = 100
r = 0.04
n = 5

A = P * (1 + r) ** n
print(round(A, 2))

# ===== DRILLS TO COMPLETE (10-15) =====
# TODO: Implement these yourself following the README prompts

# Drill 10: Boolean operators, string membership
# Prompt: Validate email: check if it contains both @ and . using boolean operators

email = input("enter your email: ").strip()
is_valid = "@" in email and "." in email
print(f"you email is valid: {is_valid}")

# Drill 11: Variable names and Python conventions
# Prompt: Create variables using snake_case and camelCase, test which Python prefers
snake_case_variable = "I follow Python convention"
camelCaseVariable = "I work but I'm not Pythonic"

print(snake_case_variable)  # Works fine
print(camelCaseVariable)    # Also works fine

# Drill 12: Formatted strings, number formatting
# Prompt: Format 1234567.89 with thousands separators and 2 decimal places
big_number = 1234567.89456
formatted = f"{big_number:,.2f}"
print(formatted)  # Output: 1,234,567.89

# Drill 13: String methods - find(), slicing
# Prompt: Extract first and last name from "John Doe" using string methods (no split)
full_name = "John Doe"
space_pos = full_name.find(" ")
first_name = full_name[:space_pos]
last_name = full_name[space_pos + 1:]
print(f"First name: {first_name}")
print(f"Last name: {last_name}")

# Drill 14: Type conversion, arithmetic, f-strings
# Prompt: Convert Celsius to Fahrenheit with formula F = C × 9/5 + 32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

# Drill 15: Multi-line strings, string methods
# Prompt: Create multi-line string with triple quotes, count total words
multi_line = """This is a multi-line string
that spans several lines
and demonstrates triple quotes."""
word_count = len(multi_line.split())
print(f"Multi-line string:\n{multi_line}")
print(f"Total words: {word_count}")
