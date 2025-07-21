# 01_primitive_types - Micro-drills for Variables, Strings, Numbers, Type Conversion
#
# Instructions: Complete each drill by typing the solution yourself.
# Don't copy-paste! The goal is to build muscle memory.

# ===== YOUR COMPLETED DRILLS (1-9) =====
# (Keep your existing solutions here)

city = "Paris"
country = "France"
population = 2.15
print(f"{city}, {country} has {population} million people")

quote = "Talk is cheap. Show me the code."
print(
    f"quote has {len(quote)} Characters, and the last word is {str.upper(quote[-5: -1])} ")

birth_year = int(input("enter your birth year: "))
age_in_months = birth_year * 12
print(f"you are {age_in_months} months old")

password = " P@ssw0rd! "
clean_password = password.strip()
alt_password = clean_password.replace("@", "a")
print(
    f"after stripping we get: {clean_password}, then we replace the @ to get: {alt_password}, with {len(alt_password)} Characters.")

pi = 3.14159
pi1 = int(pi)
pi2 = pi.__round__(2)
print(
    f"pi rounded to 2 decimals is: {pi2}, and type casted to an interger is: {pi1}")

sentence = "this sentence spans \nthree lines \nby the power of the escape sequences"
print(sentence)

a = 10
b = 5
a, b = b, a
print(a)
print(b)

path = input("inter file path: ").strip()
dot = path.rfind(".")
extention = path[dot:]
print(f"your file extention is: {extention}")

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

# Drill 12: Formatted strings, number formatting
# Prompt: Format 1234567.89 with thousands separators and 2 decimal places

# Drill 13: String methods - find(), slicing
# Prompt: Extract first and last name from "John Doe" using string methods (no split)

# Drill 14: Type conversion, arithmetic, f-strings
# Prompt: Convert Celsius to Fahrenheit with formula F = C × 9/5 + 32

# Drill 15: Multi-line strings, string methods
# Prompt: Create multi-line string with triple quotes, count total words
