# 05_exceptions - Micro-drills for Exception Handling
#
# Instructions:
# 1. Copy this template to drills.py to start fresh practice
# 2. Complete each drill by typing the solution yourself to build muscle memory
# 3. Only use concepts from previous sections + exception handling from notes_5.md
# 4. Focus on making programs robust and crash-resistant
# 5. Test each drill with both valid and invalid inputs
#
# Notes: See notes_5.md for detailed explanations of all concepts

# ===== CORE DRILLS (All Required) =====

# Drill 1: Basic try/except
# Prompt: Ask for a number, convert with int(), handle ValueError if invalid input.
# Print result or error message.
# Core concept: Basic try/except · ValueError
# TODO: Use try/except around int(input()) conversion


# Drill 2: Function error handling
# Prompt: Create safe_divide(a, b) that handles ZeroDivisionError and returns result or error message.
# Return a tuple: (result, message) or (None, error_message).
# Core concept: Function error handling · ZeroDivisionError
# TODO: Use try/except in function with tuple return


# Drill 3: Multiple exceptions in loops
# Prompt: Read a list of strings ["42", "hello", "3.14", "world"],
# convert each to int() with try/except. Print converted numbers and error count.
# Core concept: Multiple exceptions in loops
# TODO: Loop through list, count successful conversions and errors


# Drill 4: Complete exception flow
# Prompt: Use try/except/else/finally to open a file "test.txt",
# read content, and ensure it's always closed.
# Core concept: Complete exception flow · finally cleanup
# TODO: Use all four blocks: try, except, else, finally


# Drill 5: Raising custom exceptions
# Prompt: Create validate_age(age) that raises ValueError if age < 0 or age > 150.
# Test with valid/invalid ages.
# Core concept: Raising custom exceptions
# TODO: Use raise ValueError() with descriptive messages


# Drill 6: Multiple specific exceptions
# Prompt: Handle multiple exception types: ValueError, TypeError, KeyError in a single try block.
# Create a function that can trigger each type and test all three.
# Core concept: Multiple specific exceptions
# TODO: Use multiple except blocks for different exception types


# Drill 7: Context managers
# Prompt: Use 'with open()' to read a file safely. Compare with manual file handling using try/finally.
# Show both approaches and explain the difference.
# Core concept: Context managers · Resource management
# TODO: Demonstrate both manual and automatic resource management


# ===== END OF DRILLS =====
