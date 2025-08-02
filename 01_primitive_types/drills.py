# 01_primitive_types - Micro-drills for Variables, Strings, Numbers, and Type Conversion
#
# Instructions:
# Complete each drill by typing the solution yourself to build muscle memory.
# Only use the core concepts listed for each drill.
# No control flow (if/else, loops, etc.) unless the prompt says otherwise.

# ===== DRILLS TO COMPLETE (1-15) =====

# Drill 1: Variables, F-strings
# Prompt: Create variables for city, country, and population (in millions).
# Print: "<city>, <country> has <population> million people." using an f-string.
city = "Casablanca"
country = "Morocco"
population = 8.5

print(f"{city}, {country} has {population} million people.")

# Drill 2: String methods, slicing, len(), upper()
# Prompt: Given quote = "Talk is cheap. Show me the code.",
# print its total number of characters and the last word in uppercase (using slicing).
quote = "Talk is cheap. Show me the code."
print(
    f"The quote length is {len(quote)} and the last word is {quote[-5:-1].upper()}")

# Drill 3: input(), type conversion, arithmetic
# Prompt: Ask the user for their birth year (as input).
# Calculate and print their age in months. (Assume current year is 2025.)
birth_year = int(input("Enter your birth year: "))
print(f"Your age in months: {(2025 - birth_year) * 12}")

# Drill 4: String methods - strip(), replace(), len()
# Prompt: Given password = " P@ssw0rd! ",
# - Strip leading and trailing spaces.
# - Replace '@' with 'a'.
# - Print the cleaned password and its length.
password = " P@ssw0rd! "
clean_pass = password.strip()
correct_pass = clean_pass.replace("@", "a")
print(f"Cleaned password: {correct_pass}")
print(f"Length: {len(correct_pass)}")

# Drill 5: Numbers - round(), int() casting
# Prompt: Given pi = 3.14159,
# - Print pi rounded to 2 decimal places (multiple ways allowed).
# - Print pi converted to an integer.
pi = 3.14159
# Method 1: Using round() function
print(f"Rounded (round): {round(pi, 2)}")
# Method 2: Using f-string formatting
print(f"Rounded (f-string): {pi:.2f}")
# Method 3: Using __round__ method
print(f"Rounded (__round__): {pi.__round__(2)}")
# Convert to integer
print(f"Integer: {int(pi)}")

# Drill 6: Escape sequences
# Prompt: Create a string that spans three lines using \n escape sequences.
# Print the string.
long_quote = "This long quote \ncan be displayed \nin 3 lines"
print(long_quote)

# Drill 7: Multiple assignment, variable names
# Prompt: Initialize a = 10 and b = 5.
# Swap their values using multiple assignment (no temp variable).
# Print both variables after swapping.
a = 10
b = 5
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# Drill 8: String slicing, rfind() method
# Prompt: Ask the user to input a file path (e.g., "picture.png").
# Use rfind() and slicing to extract and print the file extension.
file_path = input("Enter file path: ")
dot = file_path.rfind(".")
print(f"File extension: {file_path[dot:]}")

# Drill 9: Numbers - ** operator, arithmetic
# Prompt: Calculate compound interest: P=100, r=0.04, n=5.
# Use the formula: A = P * (1 + r) ** n.
# Print the final result rounded to 2 decimal places.
P = 100
r = 0.04
n = 5

A = P * (1 + r) ** n
print(f"Compound interest result: {A:.2f}")

# Drill 10: Boolean operators, string membership
# Prompt: Ask the user for an email address.
# Check if it contains both "@" and "." (using boolean operators).
# Print whether it's "Valid" or "Invalid".
email = input("Enter your email: ")
is_valid = "@" in email and "." in email
print(f"Email valid: {is_valid}")

# Drill 11: Variable naming conventions
# Prompt: Create and print variables using both snake_case and camelCase naming styles.
# Note which style is preferred in Python (comment in your code).
snake_case_variable = "I follow Python convention"
camelCaseVariable = "I work but I'm not Pythonic"

print(snake_case_variable)  # Python prefers this style
print(camelCaseVariable)    # Works but not conventional in Python

# Drill 12: Formatted strings, number formatting
# Prompt: Format 1234567.89 with thousands separators and 2 decimal places using an f-string.
# Print the formatted result.
big_number = 1234567.89
print(f"Formatted number: {big_number:,.2f}")

# Drill 13: String methods - find(), slicing
# Prompt: Given full_name = "John Doe",
# - Use find() and slicing to extract the first and last name (no split()).
# - Print them separately.
full_name = "John Doe"
space_pos = full_name.find(" ")
first_name = full_name[:space_pos]
last_name = full_name[space_pos + 1:]
print(f"First name: {first_name}")
print(f"Last name: {last_name}")

# Drill 14: Type conversion, arithmetic, f-strings
# Prompt: Ask the user for a temperature in Celsius (float input).
# Convert it to Fahrenheit using the formula F = C × 9/5 + 32.
# Print the result to 1 decimal place using an f-string.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

# Drill 15: Multi-line strings, string methods
# Prompt: Create a multi-line string using triple quotes.
# Count and print the total number of words (use split() and len()).
# Also print the original multi-line string.
multi_line = """This is a multi-line string
that spans several lines
and demonstrates triple quotes."""
word_count = len(multi_line.split())
print(f"Multi-line string:\n{multi_line}")
print(f"Total words: {word_count}")

# ===== END OF DRILLS =====
