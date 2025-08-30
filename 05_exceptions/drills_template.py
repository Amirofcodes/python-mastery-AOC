# 05_exceptions - Comprehensive Error Handling Mastery Drills
#
# Instructions:
# 1. Copy this template to drills.py to start fresh practice
# 2. Complete each drill by typing the solution yourself to build muscle memory
# 3. Learn ALL the different ways to handle errors and write robust code
# 4. Test each drill with both valid and invalid inputs
# 5. Focus on making programs that never crash unexpectedly
#
# Notes: See notes_5.md for detailed explanations of all concepts

# ===== EXCEPTION TYPES - COMPREHENSIVE MASTERY (4 DRILLS) =====

# Drill 1: Common exception types recognition
# Prompt: Create examples that trigger each exception type, then handle them:
# - ValueError (invalid conversion)
# - TypeError (wrong type operation)
# - KeyError (missing dictionary key)
# - IndexError (list index out of range)
# Print the exception type and message for each.
# Core concept: Recognizing all common exception types
# TODO: Create scenarios that trigger each exception type and handle them


# Drill 2: Exception hierarchy understanding
# Prompt: Create a function that can raise ValueError, TypeError, or KeyError.
# Handle them using: specific handlers, parent class handler (Exception),
# and demonstrate the order matters (specific first, general last).
# Core concept: Exception hierarchy and handler order
# TODO: Show specific vs general exception handling order


# Drill 3: Exception information extraction
# Prompt: In exception handlers, extract and display:
# - Exception type name
# - Exception message
# - Exception args
# - Line number where error occurred (use traceback)
# Core concept: Extracting detailed exception information
# TODO: Use type(), str(), args, and traceback to get full error info


# Drill 4: Built-in vs custom exception scenarios
# Prompt: Create scenarios for FileNotFoundError, PermissionError, ZeroDivisionError.
# Handle each appropriately and demonstrate when built-in exceptions occur.
# Also create a custom ValidationError for invalid data.
# Core concept: When to use built-in vs custom exceptions
# TODO: Show scenarios for common built-in exceptions plus custom ones


# ===== EXCEPTION HANDLING PATTERNS - COMPREHENSIVE MASTERY (5 DRILLS) =====

# Drill 5: Basic try/except patterns
# Prompt: Create safe_convert_int(value) function with three approaches:
# - Return None on error
# - Return tuple (result, error_message)
# - Return result with default value parameter
# Test with valid numbers, invalid strings, and None.
# Core concept: Different error handling return patterns
# TODO: Show 3 different ways to handle conversion errors


# Drill 6: Multiple exception handling strategies
# Prompt: Create process_data(data) that handles different errors differently:
# - ValueError: log warning and continue with default
# - TypeError: log error and skip item
# - KeyError: log critical and raise custom DataError
# Process a list with mixed valid/invalid data.
# Core concept: Different strategies for different exception types
# TODO: Handle same operation differently based on exception type


# Drill 7: Complete exception flow mastery
# Prompt: Create file_processor(filename) using try/except/else/finally:
# - try: open and read file
# - except: handle FileNotFoundError and PermissionError
# - else: print "Successfully processed" (only if no exception)
# - finally: print "Cleanup completed" (always runs)
# Test with existing file, missing file, and permission denied.
# Core concept: Complete try/except/else/finally flow
# TODO: Use all four blocks and understand when each executes


# Drill 8: Exception chaining and context
# Prompt: Create high_level_operation() that calls low_level_operation().
# When low_level raises ValueError, catch it and raise BusinessLogicError
# using both chaining approaches: "raise ... from e" and "raise ... from None"
# Show the difference in traceback output.
# Core concept: Exception chaining and context preservation
# TODO: Demonstrate exception chaining with and without context


# Drill 9: Nested exception handling
# Prompt: Create database_operation() with nested try/except blocks:
# - Outer try: handles ConnectionError, DatabaseError
# - Inner try: handles specific SQL errors (ValidationError, ConstraintError)
# - Demonstrate when inner vs outer handlers catch exceptions
# Core concept: Nested exception handling strategies
# TODO: Show how nested handlers work and which catches what


# ===== CUSTOM EXCEPTIONS - COMPREHENSIVE MASTERY (3 DRILLS) =====

# Drill 10: Custom exception classes hierarchy
# Prompt: Create custom exception hierarchy:
# - BaseAppError (inherits from Exception)
# - ValidationError (inherits from BaseAppError)
# - BusinessLogicError (inherits from BaseAppError)
# - DataProcessingError (inherits from BaseAppError)
# Show how catching BaseAppError catches all custom exceptions.
# Core concept: Custom exception hierarchies
# TODO: Create exception hierarchy and demonstrate polymorphic handling


# Drill 11: Exceptions with additional data
# Prompt: Create DatabaseError with extra attributes:
# - error_code (string)
# - query (string that failed)
# - timestamp (when error occurred)
# Override __str__ to include all information in error message.
# Core concept: Exceptions carrying additional context
# TODO: Create exception class with custom attributes and string representation


# Drill 12: Domain-specific exception handling
# Prompt: Create UserRegistrationError for user signup with specific subtypes:
# - DuplicateEmailError
# - WeakPasswordError
# - InvalidAgeError
# Create register_user() function that raises appropriate exceptions.
# Core concept: Domain-specific exception design
# TODO: Design exception hierarchy for specific business domain


# ===== DEFENSIVE PROGRAMMING - COMPREHENSIVE MASTERY (4 DRILLS) =====

# Drill 13: Input validation with exceptions
# Prompt: Create comprehensive input validator with these functions:
# - validate_email(email) - raises ValidationError for invalid format
# - validate_age(age) - raises ValidationError for age < 0 or > 150
# - validate_password(password) - raises ValidationError for weak passwords
# Create user_registration(email, age, password) that uses all validators.
# Core concept: Input validation with custom exceptions
# TODO: Build comprehensive validation system with exceptions


# Drill 14: Safe conversion functions
# Prompt: Create safe conversion functions with error handling:
# - safe_int(value, default=None, min_val=None, max_val=None)
# - safe_float(value, default=None, precision=2)
# - safe_bool(value, default=None)
# Each should handle type errors gracefully and validate ranges.
# Core concept: Safe type conversion with validation
# TODO: Create robust conversion functions with comprehensive error handling


# Drill 15: Resource management patterns
# Prompt: Create DatabaseConnection context manager that:
# - Connects in __enter__, handles ConnectionError
# - Always disconnects in __exit__, handles DisconnectionError
# - Logs all connection events and errors
# Compare with manual connection management using try/finally.
# Core concept: Resource management with context managers
# TODO: Implement context manager for resource management


# Drill 16: Retry patterns with exponential backoff
# Prompt: Create retry_operation(func, max_retries=3) that:
# - Retries on ConnectionError and TimeoutError only
# - Uses exponential backoff (1s, 2s, 4s delays)
# - Logs each retry attempt
# - Raises original exception after max retries
# Test with function that randomly fails.
# Core concept: Retry patterns for transient failures
# TODO: Implement retry logic with exponential backoff


# ===== REAL-WORLD APPLICATIONS - COMPREHENSIVE MASTERY (3 DRILLS) =====

# Drill 17: File processing pipeline with error handling
# Prompt: Create process_files(file_list) that:
# - Processes each file individually
# - Handles FileNotFoundError, PermissionError, UnicodeDecodeError
# - Collects errors but continues processing other files
# - Returns summary: {processed: count, errors: [error_info]}
# - Fails completely only if >50% of files have errors
# Core concept: Batch processing with partial failure handling
# TODO: Build resilient file processing pipeline


# Drill 18: API client with comprehensive error handling
# Prompt: Create APIClient class with error handling for:
# - ConnectionError (network issues)
# - TimeoutError (slow responses)
# - HTTPError (4xx, 5xx responses)
# - JSONDecodeError (invalid response format)
# Implement different retry strategies for different error types.
# Core concept: Network communication error handling
# TODO: Build robust API client with comprehensive error handling


# Drill 19: Data validation pipeline
# Prompt: Create DataProcessor that validates and processes records:
# - Handles ValidationError for individual records (log and skip)
# - Handles DatabaseError for storage (retry with backoff)
# - Handles SystemError for critical failures (stop processing)
# - Provides detailed error reporting and processing statistics
# Core concept: Complex data processing with multi-level error handling
# TODO: Build comprehensive data processing pipeline with error handling


# ===== INTEGRATION CHALLENGE - ADVANCED APPLICATION (1 DRILL) =====

# Drill 20: Complete application with error handling
# Prompt: Create mini user management system that combines everything:
# - Input validation for user data (custom ValidationError)
# - Safe type conversion for user input
# - File I/O for data persistence (handle all file errors)
# - Logging for all operations and errors
# - Graceful degradation (use defaults when external services fail)
# - Resource cleanup (files, connections) using context managers
# System should never crash, always provide useful feedback to users.
# Core concept: Integration of all error handling patterns
# TODO: Build complete application demonstrating all error handling concepts


# ===== END OF COMPREHENSIVE DRILLS =====
#
# After completing these 20 drills, you should be fluent in:
# - Recognizing and handling all common exception types
# - Using all exception handling patterns appropriately
# - Creating custom exceptions for your applications
# - Writing defensive code that validates inputs
# - Managing resources safely with proper cleanup
# - Building resilient applications that handle failures gracefully
# - Debugging and troubleshooting exception scenarios
# - Designing error handling strategies for real applications
#
# This comprehensive error handling foundation makes your code robust,
# maintainable, and production-ready!
