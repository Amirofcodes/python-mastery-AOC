# 05_exceptions · Micro‑drills (Exception Handling)
# Use only concepts from previous sections plus exception handling.

# Drill 1: Basic try/except
# Ask for a number, convert with int(), handle ValueError if invalid input. Print result or error msg.
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Invalid entry")

# Drill 2: Function error handling
# Create safe_divide(a, b) that handles ZeroDivisionError and returns result or error message.


def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Can't divide by 0"


# Drill 3: Multiple exceptions in loops
# Read a list of strings ["42", "hello", "3.14", "world"],
# convert each to int() with try/except. Print converted numbers and error count.
strings = ["42", "hello", "3.14", "world"]
converted = []
error_count = 0
for s in strings:
    try:
        converted.append(int(s))
    except ValueError:
        print("error")
        error_count += 1
print(converted)
print(error_count)


# Drill 4: Complete exception flow
# Use try/except/else/finally to open a file "test.txt",
# read content, and ensure it's always closed.
file = None
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    content = file.read()
    print("File content:", content)
finally:
    if file:
        file.close()
        print("File closed")


# Drill 5: Raising custom exceptions
# Create validate_age(age) that raises ValueError if age < 0 or age > 150.
# Test with valid/invalid ages.
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot be over 150")
    return age


# Test valid age
try:
    print("Valid age:", validate_age(25))
except ValueError as e:
    print("Error:", e)

# Test negative age
try:
    print("Negative age:", validate_age(-5))
except ValueError as e:
    print("Error:", e)

# Test too high age
try:
    print("Too high age:", validate_age(200))
except ValueError as e:
    print("Error:", e)


# Drill 6: Multiple specific exceptions
# Handle multiple exception types: ValueError, TypeError,
# KeyError in a single try block. Test each type.

def risky_operation(operation_type):
    if operation_type == "value_error":
        int("not_a_number")  # Causes ValueError
    elif operation_type == "type_error":
        "string" + 42  # Causes TypeError
    elif operation_type == "key_error":
        {"a": 1}["missing_key"]  # Causes KeyError


# Test ValueError
try:
    risky_operation("value_error")
except ValueError:
    print("Caught ValueError")
except TypeError:
    print("Caught TypeError")
except KeyError:
    print("Caught KeyError")

# Test TypeError
try:
    risky_operation("type_error")
except ValueError:
    print("Caught ValueError")
except TypeError:
    print("Caught TypeError")
except KeyError:
    print("Caught KeyError")

# Test KeyError
try:
    risky_operation("key_error")
except ValueError:
    print("Caught ValueError")
except TypeError:
    print("Caught TypeError")
except KeyError:
    print("Caught KeyError")


# Drill 7: Context managers
# Use 'with open()' to read a file safely. Compare with manual file handling using try/finally.

print("=== Using context manager (with statement) ===")
try:
    with open("test.txt", "r") as file:
        content = file.read()
        print("Content with 'with':", content.strip())
        # File automatically closed when exiting 'with' block
except FileNotFoundError:
    print("File not found using 'with'")

print("=== Manual file handling (try/finally) ===")
file = None
try:
    file = open("test.txt", "r")
    content = file.read()
    print("Content with try/finally:", content.strip())
except FileNotFoundError:
    print("File not found using try/finally")
finally:
    if file:
        file.close()
        print("Manually closed file")

print("=== Context manager with missing file ===")
try:
    with open("missing.txt", "r") as file:
        content = file.read()
        print("Content:", content)
except FileNotFoundError:
    print("Missing file handled gracefully with 'with'")
