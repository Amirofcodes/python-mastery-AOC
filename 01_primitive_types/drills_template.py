# 01_primitive_types - Comprehensive Mastery Drills
#
# Instructions:
# 1. Copy this template to drills.py to start fresh practice
# 2. Complete each drill by typing the solution yourself to build muscle memory
# 3. Learn ALL the different ways to work with Python's primitive types
# 4. Test each drill before moving to the next - build that muscle memory!
# 5. Focus on systematic mastery of every method and pattern
#
# Notes: See notes_1.md for detailed explanations of all concepts

# ===== STRINGS - COMPREHENSIVE MASTERY (8 DRILLS) =====

# Drill 1: String creation methods
# Prompt: Create the same text "Hello World" using 5 different methods:
# single quotes, double quotes, string constructor, f-string with variables, triple quotes.
# Print each version to verify they're identical.
# Core concept: All string creation methods
# TODO: Show 5 different ways to create the same string


# Drill 2: String manipulation methods
# Prompt: Given text = "  Python Programming ROCKS!  ":
# Apply these methods and print results: strip(), lower(), upper(), title(), 
# replace("ROCKS", "rocks"), and swapcase().
# Core concept: All string manipulation methods
# TODO: Use 6 different manipulation methods on the same string


# Drill 3: String searching and testing
# Prompt: Given sentence = "Learn Python Programming Today":
# - Find the position of "Python" using find()
# - Count how many times "a" appears (case-insensitive)
# - Test if it starts with "Learn" and ends with "Today"
# - Check if "Programming" is in the sentence
# Core concept: All searching and testing methods
# TODO: Use find(), count(), startswith(), endswith(), and 'in'


# Drill 4: String slicing mastery
# Prompt: Given data = "Python2024Programming":
# Extract and print: first 6 chars, last 11 chars, middle section "2024",
# every 2nd character, and the string reversed.
# Core concept: All slicing patterns
# TODO: Use 5 different slicing patterns to extract parts


# Drill 5: String formatting methods
# Prompt: Given name="Alice", age=25, salary=75000.50:
# Format and print the same message using f-strings, .format(), and % formatting:
# "Alice (age 25) earns $75,000.50"
# Core concept: All formatting methods
# TODO: Use 3 different formatting approaches for same output


# Drill 6: String splitting and joining
# Prompt: Given email = "user.name@company.domain.com":
# - Split by "." to get all parts
# - Split by "@" to get username and domain separately
# - Take the parts and join them with "-" instead
# Core concept: Split and join methods with different separators
# TODO: Use split() with different separators and join() to reassemble


# Drill 7: String validation patterns
# Prompt: Create a function validate_username(username) that checks:
# - Length is between 3-20 characters
# - Contains only letters, numbers, and underscores
# - Doesn't start with a number
# Test with: "user1", "1user", "ab", and "valid_user_123"
# Core concept: String validation using multiple methods
# TODO: Combine isalnum(), isdigit(), and length checks


# Drill 8: Advanced string operations
# Prompt: Given messy_text = "  PyThOn,ProGramming;Is:AwEsome!  ":
# Clean it to produce "Python Programming Is Awesome" by:
# - Stripping whitespace
# - Converting to title case
# - Replacing punctuation (,;:!) with spaces
# - Reducing multiple spaces to single spaces
# Core concept: Chaining multiple string operations
# TODO: Chain strip(), title(), replace(), and join(split())


# ===== NUMBERS - COMPREHENSIVE MASTERY (5 DRILLS) =====

# Drill 9: Number creation methods
# Prompt: Create the number 42 using 4 different methods:
# - Integer literal
# - int() constructor from string
# - int() from float
# - int() from boolean
# Print each result to verify they're all 42.
# Core concept: All number creation methods
# TODO: Show 4 different ways to create the same integer


# Drill 10: Number base conversions
# Prompt: Given decimal number 255:
# - Convert and display in binary, octal, and hexadecimal
# - Create the same number from each base representation
# - Verify all methods produce 255
# Core concept: Number base systems and conversions
# TODO: Use bin(), oct(), hex() and int() with base parameters


# Drill 11: Number arithmetic and operations
# Prompt: Given a=17, b=5:
# Demonstrate all arithmetic operators: +, -, *, /, //, %, **
# Also show augmented assignments (+=, -=, etc.) starting with c=10
# Print each result with clear labels.
# Core concept: All arithmetic operations and assignment operators
# TODO: Show all 7 arithmetic operators and 7 augmented assignments


# Drill 12: Number formatting patterns
# Prompt: Given amount = 1234567.89:
# Format and display as:
# - With thousands separators
# - Rounded to 1 decimal place
# - As currency ($1,234,567.89)
# - In scientific notation
# - As percentage (multiply by 0.0001 first)
# Core concept: All number formatting patterns
# TODO: Use f-strings with different format specifications


# Drill 13: Number conversion and validation
# Prompt: Create safe conversion functions:
# - safe_int(value) - returns (result, error_message)
# - safe_float(value) - returns (result, error_message)
# Test with valid inputs ("42", "3.14") and invalid ("abc", "")
# Core concept: Safe type conversion with error handling
# TODO: Use try/except to handle ValueError in conversions


# ===== BOOLEANS - COMPREHENSIVE MASTERY (3 DRILLS) =====

# Drill 14: Boolean creation and truthiness
# Prompt: Test the truthiness of these values and print results:
# 0, 1, -1, "", "hello", [], [0], {}, None, False, True
# Use if statements to test and print "Truthy" or "Falsy" for each.
# Core concept: Boolean values and truthiness rules
# TODO: Test all falsy values and several truthy examples


# Drill 15: Logical operators and short-circuit evaluation
# Prompt: Given age=20, has_license=True, has_car=False:
# Create expressions using and, or, not to determine:
# - Can drive (age >= 16 AND has_license)
# - Can drive alone (can_drive AND (age >= 18 OR has_car))
# - Cannot drive (NOT can_drive)
# Demonstrate short-circuit with: False and print("This won't print")
# Core concept: All logical operators and short-circuit evaluation
# TODO: Use and, or, not operators and show short-circuit behavior


# Drill 16: Boolean context and patterns
# Prompt: Use boolean context for these patterns:
# - Default values: name = input("Name: ") or "Anonymous"
# - Filtering: numbers = [0, 1, 2, 0, 3]; non_zero = [n for n in numbers if n]
# - Validation: password_ok = len(password) >= 8 and any(c.isdigit() for c in password)
# Core concept: Boolean context usage patterns
# TODO: Show default values, filtering, and validation patterns


# ===== VARIABLES - COMPREHENSIVE MASTERY (3 DRILLS) =====

# Drill 17: Variable assignment patterns
# Prompt: Demonstrate all assignment patterns:
# - Simple: x = 5
# - Multiple: a, b, c = 1, 2, 3
# - Same value: x = y = z = 0
# - Swapping: swap two variables without temp variable
# - Star unpacking: first, *middle, last = [1, 2, 3, 4, 5]
# Core concept: All variable assignment methods
# TODO: Show 5 different assignment patterns


# Drill 18: Variable naming and conventions
# Prompt: Create variables following different naming conventions:
# - snake_case (preferred): user_name, total_amount
# - camelCase (works but not Pythonic): userName, totalAmount
# - Constants: MAX_ATTEMPTS, DEFAULT_TIMEOUT
# - Private convention: _internal_var
# Comment on which style Python prefers and why.
# Core concept: Variable naming conventions
# TODO: Show different naming styles and comment on Python preferences


# Drill 19: Memory references and identity
# Prompt: Demonstrate the difference between == and is:
# - Create two lists with same values: a = [1,2,3], b = [1,2,3]
# - Create reference: c = a
# - Test a == b, a is b, a == c, a is c
# - Use id() function to show memory addresses
# - Modify a and show effect on c but not b
# Core concept: Identity vs equality, references vs copies
# TODO: Show == vs is, demonstrate reference behavior


# ===== INPUT/OUTPUT - COMPREHENSIVE MASTERY (3 DRILLS) =====

# Drill 20: Input validation and conversion
# Prompt: Create get_positive_number() function that:
# - Asks for input until user enters valid positive number
# - Handles ValueError (non-numeric input)
# - Handles negative numbers
# - Returns the validated positive number
# Test it by calling and using the result in a calculation.
# Core concept: Input validation with error handling
# TODO: Use while loop with try/except for robust input


# Drill 21: Output formatting methods
# Prompt: Given data = {"name": "Alice", "age": 30, "balance": 1234.56}:
# Display this information using different output methods:
# - Simple print statements
# - F-string formatting
# - print() with sep and end parameters
# - Formatted as a nice user display
# Core concept: All output formatting approaches
# TODO: Show multiple ways to display the same data


# Drill 22: Comprehensive data processing
# Prompt: Create a mini user registration system:
# - Ask for full name (validate: not empty, contains space for first/last)
# - Ask for age (validate: integer between 13-120)
# - Ask for email (validate: contains @ and .)
# - Display formatted welcome message with all info
# Handle all input validation and provide clear error messages.
# Core concept: Integration of all primitive type skills
# TODO: Combine input, validation, formatting, and output


# ===== END OF COMPREHENSIVE DRILLS =====
#
# After completing these 22 drills, you should be fluent in:
# - All string creation, manipulation, and formatting methods
# - All number types, operations, and formatting options
# - Boolean logic, truthiness, and logical operators  
# - Variable assignment patterns and naming conventions
# - Input validation and output formatting
# - Error handling for type conversions
# - Professional Python coding patterns and idioms
#
# This comprehensive foundation prepares you for control flow, functions,
# and data structures with complete confidence in the basics!
