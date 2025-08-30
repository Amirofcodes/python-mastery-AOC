# 05 · Exception Handling - Comprehensive Error Management Guide

Master robust Python programming through complete understanding of **all the different ways** to handle errors, validate inputs, debug issues, and write defensive code that never crashes unexpectedly.

---

## **Mental Model: Python's Error Handling Philosophy**

- **Exceptions**: Interruptions in normal program flow when something goes wrong
- **EAFP**: "Easier to Ask for Forgiveness than Permission" - Python's preferred approach
- **Defensive Programming**: Anticipate what can go wrong and handle it gracefully
- **Fail Fast**: Detect errors early and handle them appropriately
- **Graceful Degradation**: Continue operation when possible, fail safely when necessary

---

# **EXCEPTION TYPES - Know Every Important Error**

## **1. Common Built-in Exceptions - When They Occur**

```python
# ValueError - Invalid value for correct type
try:
    number = int("hello")           # ValueError: invalid literal
    import math
    math.sqrt(-1)                   # ValueError: negative number
    float("not_a_number")           # ValueError: invalid float
except ValueError as e:
    print(f"ValueError: {e}")

# TypeError - Wrong type entirely
try:
    len(42)                         # TypeError: object has no len()
    "hello" + 5                     # TypeError: can't concatenate
    list[0]                         # TypeError: 'type' object not subscriptable
except TypeError as e:
    print(f"TypeError: {e}")

# KeyError - Dictionary key doesn't exist
try:
    data = {"name": "Alice"}
    value = data["age"]             # KeyError: 'age'
except KeyError as e:
    print(f"KeyError: {e}")

# IndexError - List/tuple index out of range
try:
    numbers = [1, 2, 3]
    value = numbers[10]             # IndexError: list index out of range
except IndexError as e:
    print(f"IndexError: {e}")

# AttributeError - Object doesn't have that attribute/method
try:
    text = "hello"
    text.append("world")            # AttributeError: 'str' has no 'append'
except AttributeError as e:
    print(f"AttributeError: {e}")

# FileNotFoundError - File doesn't exist
try:
    with open("nonexistent.txt") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# ZeroDivisionError - Division by zero
try:
    result = 10 / 0                 # ZeroDivisionError: division by zero
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# NameError - Variable not defined
try:
    print(undefined_variable)       # NameError: name 'undefined_variable' not defined
except NameError as e:
    print(f"NameError: {e}")

# ImportError/ModuleNotFoundError - Import issues
try:
    import nonexistent_module       # ModuleNotFoundError
except ImportError as e:
    print(f"ImportError: {e}")

# PermissionError - Insufficient permissions
try:
    with open("/etc/passwd", "w") as f:
        f.write("hack attempt")
except PermissionError as e:
    print(f"PermissionError: {e}")
```

## **2. Exception Hierarchy - Understanding Inheritance**

```python
# Exception hierarchy (simplified)
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- ArithmeticError
#       |    +-- ZeroDivisionError
#       |    +-- OverflowError
#       +-- AttributeError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- NameError
#       +-- OSError
#       |    +-- FileNotFoundError
#       |    +-- PermissionError
#       +-- RuntimeError
#       +-- TypeError
#       +-- ValueError

# Catching parent exceptions catches all children
try:
    risky_operation()
except LookupError:              # Catches both IndexError and KeyError
    print("Lookup failed")
except ArithmeticError:          # Catches ZeroDivisionError, OverflowError, etc.
    print("Math error")
except Exception:                # Catches almost everything (but not SystemExit)
    print("Something went wrong")

# Best practice: catch specific exceptions first, then general ones
try:
    risky_operation()
except KeyError:
    print("Key not found")       # Most specific
except LookupError:
    print("Lookup failed")      # More general
except Exception:
    print("Unknown error")      # Most general
```

---

# **TRY/EXCEPT PATTERNS - All Combinations**

## **1. Basic Exception Handling - All Structures**

```python
# Pattern 1: Simple try/except
def safe_divide_basic(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Pattern 2: Multiple specific exceptions
def convert_and_access(data, key, target_type):
    try:
        value = data[key]           # Might raise KeyError
        return target_type(value)   # Might raise ValueError/TypeError
    except KeyError:
        return f"Key '{key}' not found"
    except ValueError:
        return f"Cannot convert to {target_type.__name__}"
    except TypeError:
        return f"Invalid type conversion"

# Pattern 3: Multiple exceptions, same handler
def safe_numeric_operation(a, b, operation):
    try:
        if operation == "divide":
            return a / b
        elif operation == "power":
            return a ** b
    except (ZeroDivisionError, OverflowError, ValueError) as e:
        return f"Numeric error: {e}"

# Pattern 4: Catch all exceptions
def robust_operation(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Error in {func.__name__}: {type(e).__name__}: {e}")
        return None

# Pattern 5: Re-raising exceptions
def validate_and_process(data):
    try:
        # Pre-processing validation
        if not isinstance(data, dict):
            raise TypeError("Data must be dictionary")
        result = process_data(data)
        return result
    except (KeyError, ValueError):
        print("Data validation failed")
        raise  # Re-raise the same exception
```

## **2. try/except/else/finally - Complete Structures**

```python
# Pattern 1: try/except/else
def safe_file_read(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    else:
        # Runs only if no exception occurred
        try:
            content = file.read()
            return content
        finally:
            file.close()

# Pattern 2: try/except/else/finally
def complete_error_handling():
    print("Starting operation...")
    try:
        # Risky operation
        result = complex_operation()
    except ValueError as e:
        print(f"Value error: {e}")
        result = None
    except Exception as e:
        print(f"Unexpected error: {e}")
        result = None
    else:
        # Only runs if no exception
        print("Operation completed successfully")
        log_success(result)
    finally:
        # Always runs - cleanup code
        print("Cleaning up resources...")
        cleanup_resources()

    return result

# Pattern 3: Nested try/except for different phases
def multi_phase_operation():
    try:
        # Phase 1: Setup
        try:
            connection = setup_connection()
        except ConnectionError:
            print("Setup failed")
            return False

        # Phase 2: Main operation
        try:
            result = perform_operation(connection)
        except OperationError as e:
            print(f"Operation failed: {e}")
            return False
        else:
            print("Operation successful")
            return True
        finally:
            # Phase 3: Always cleanup
            cleanup_connection(connection)
    except Exception as e:
        print(f"Unexpected error in operation: {e}")
        return False

# Pattern 4: Context-specific exception handling
def process_user_input():
    while True:
        try:
            # Get input
            user_input = input("Enter a number (or 'quit'): ")

            # Check for exit condition
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break

            # Convert and validate
            number = float(user_input)
            if number < 0:
                raise ValueError("Number must be positive")

            # Process
            result = math.sqrt(number)
            print(f"Square root of {number} is {result:.2f}")

        except ValueError as e:
            if "could not convert" in str(e):
                print("Please enter a valid number")
            else:
                print(f"Invalid value: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
```

## **3. Exception Information and Debugging**

```python
import traceback
import sys

# Pattern 1: Detailed exception information
def detailed_error_handling():
    try:
        risky_operation()
    except Exception as e:
        # Basic exception info
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception value: {e}")
        print(f"Exception args: {e.args}")

        # Traceback information
        print("\nFull traceback:")
        traceback.print_exc()

        # Custom error logging
        error_info = {
            'type': type(e).__name__,
            'message': str(e),
            'file': traceback.extract_tb(e.__traceback__)[-1].filename,
            'line': traceback.extract_tb(e.__traceback__)[-1].lineno
        }
        log_error(error_info)

# Pattern 2: Exception chaining
def operation_with_context():
    try:
        low_level_operation()
    except ValueError as e:
        # Chain exceptions to preserve context
        raise RuntimeError("High-level operation failed") from e

# Pattern 3: Suppressing exception chaining
def operation_without_context():
    try:
        low_level_operation()
    except ValueError:
        # Suppress the chaining
        raise RuntimeError("High-level operation failed") from None

# Pattern 4: Custom exception with context
class ValidationError(Exception):
    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value

    def __str__(self):
        base = super().__str__()
        if self.field:
            return f"{base} (field: {self.field}, value: {self.value})"
        return base

def validate_user_data(data):
    try:
        if not data.get('name'):
            raise ValidationError("Name is required", field='name', value=data.get('name'))
        if not isinstance(data.get('age'), int) or data['age'] < 0:
            raise ValidationError("Age must be positive integer", field='age', value=data.get('age'))
    except ValidationError as e:
        print(f"Validation failed: {e}")
        print(f"Field: {e.field}, Value: {e.value}")
        raise

# Pattern 5: Exception logging and monitoring
def monitored_operation():
    import logging

    logger = logging.getLogger(__name__)

    try:
        result = complex_operation()
        logger.info("Operation completed successfully")
        return result
    except Exception as e:
        # Log with full context
        logger.error(
            "Operation failed: %s",
            str(e),
            exc_info=True,  # Include full traceback
            extra={
                'operation': 'complex_operation',
                'user_id': get_current_user_id(),
                'timestamp': datetime.now().isoformat()
            }
        )
        raise  # Re-raise for caller to handle
```

---

# **CUSTOM EXCEPTIONS - Building Your Own**

## **1. Creating Custom Exception Classes**

```python
# Pattern 1: Simple custom exception
class CustomError(Exception):
    """Base class for application-specific errors"""
    pass

class ValidationError(CustomError):
    """Raised when data validation fails"""
    pass

class BusinessLogicError(CustomError):
    """Raised when business rules are violated"""
    pass

# Pattern 2: Exception with additional data
class DatabaseError(Exception):
    def __init__(self, message, error_code=None, query=None):
        super().__init__(message)
        self.error_code = error_code
        self.query = query
        self.timestamp = datetime.now()

    def __str__(self):
        base = super().__str__()
        if self.error_code:
            return f"{base} (Error code: {self.error_code})"
        return base

# Pattern 3: Exception hierarchy for different scenarios
class APIError(Exception):
    """Base class for API-related errors"""
    pass

class AuthenticationError(APIError):
    """Authentication failed"""
    pass

class AuthorizationError(APIError):
    """User not authorized for this operation"""
    pass

class RateLimitError(APIError):
    """API rate limit exceeded"""
    def __init__(self, message, retry_after=None):
        super().__init__(message)
        self.retry_after = retry_after

class APIUnavailableError(APIError):
    """External API is unavailable"""
    pass

# Pattern 4: Exception with recovery suggestions
class ConfigurationError(Exception):
    def __init__(self, message, config_key=None, suggestion=None):
        super().__init__(message)
        self.config_key = config_key
        self.suggestion = suggestion

    def get_help_message(self):
        msg = str(self)
        if self.config_key:
            msg += f"\nConfiguration key: {self.config_key}"
        if self.suggestion:
            msg += f"\nSuggestion: {self.suggestion}"
        return msg

# Usage examples
try:
    validate_user_age(-5)
except ValidationError:
    print("Age validation failed")

try:
    connect_to_database()
except DatabaseError as e:
    print(f"Database error: {e}")
    if e.error_code:
        handle_specific_db_error(e.error_code)

try:
    call_external_api()
except RateLimitError as e:
    if e.retry_after:
        print(f"Rate limited. Retry after {e.retry_after} seconds")
        time.sleep(e.retry_after)
        call_external_api()
```

## **2. Exception Handling Patterns by Domain**

```python
# Web API Error Handling
class APIHandler:
    def handle_request(self, request):
        try:
            return self.process_request(request)
        except ValidationError as e:
            return {"error": "Bad Request", "details": str(e)}, 400
        except AuthenticationError:
            return {"error": "Unauthorized"}, 401
        except AuthorizationError:
            return {"error": "Forbidden"}, 403
        except Exception as e:
            logger.error("Unexpected error in API", exc_info=True)
            return {"error": "Internal Server Error"}, 500

# File Processing Error Handling
class FileProcessor:
    def process_file(self, filepath):
        try:
            with open(filepath, 'r') as f:
                data = f.read()
            return self.parse_and_validate(data)
        except FileNotFoundError:
            raise FileProcessingError(f"File not found: {filepath}")
        except PermissionError:
            raise FileProcessingError(f"Permission denied: {filepath}")
        except UnicodeDecodeError:
            raise FileProcessingError(f"File encoding error: {filepath}")
        except ValidationError as e:
            raise FileProcessingError(f"Invalid file content: {e}")

# Data Processing Error Handling
class DataProcessor:
    def process_dataset(self, data):
        errors = []
        processed_items = []

        for i, item in enumerate(data):
            try:
                processed_item = self.process_item(item)
                processed_items.append(processed_item)
            except ValidationError as e:
                errors.append(f"Item {i}: {e}")
                continue  # Skip this item, continue with others
            except Exception as e:
                errors.append(f"Item {i}: Unexpected error - {e}")
                continue

        if errors:
            # Decide whether to raise or just warn
            if len(errors) > len(data) * 0.5:  # More than 50% failed
                raise ProcessingError(f"Too many errors: {errors}")
            else:
                logger.warning(f"Some items failed: {errors}")

        return processed_items
```

---

# **DEFENSIVE PROGRAMMING PATTERNS**

## **1. Input Validation Strategies**

```python
# Pattern 1: Validation decorators
def validate_input(validator_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                validator_func(*args, **kwargs)
                return func(*args, **kwargs)
            except ValueError as e:
                raise ValidationError(f"Input validation failed: {e}")
        return wrapper
    return decorator

def validate_positive_number(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Must be a number")
    if x <= 0:
        raise ValueError("Must be positive")

@validate_input(validate_positive_number)
def calculate_square_root(x):
    return math.sqrt(x)

# Pattern 2: Safe conversion functions
def safe_int(value, default=None, min_val=None, max_val=None):
    """Safely convert to integer with validation"""
    try:
        result = int(value)
        if min_val is not None and result < min_val:
            raise ValueError(f"Value {result} below minimum {min_val}")
        if max_val is not None and result > max_val:
            raise ValueError(f"Value {result} above maximum {max_val}")
        return result
    except (ValueError, TypeError):
        if default is not None:
            return default
        raise

def safe_dict_access(dictionary, key, default=None, required_type=None):
    """Safely access dictionary with validation"""
    try:
        value = dictionary[key]
        if required_type and not isinstance(value, required_type):
            raise TypeError(f"Expected {required_type.__name__}, got {type(value).__name__}")
        return value
    except KeyError:
        if default is not None:
            return default
        raise

# Pattern 3: Comprehensive input validation
class InputValidator:
    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            raise ValidationError("Email must be string")
        if "@" not in email:
            raise ValidationError("Email must contain @")
        if "." not in email.split("@")[1]:
            raise ValidationError("Email domain must contain .")
        return email.lower().strip()

    @staticmethod
    def validate_age(age):
        try:
            age_int = int(age)
        except (ValueError, TypeError):
            raise ValidationError("Age must be a number")

        if age_int < 0:
            raise ValidationError("Age cannot be negative")
        if age_int > 150:
            raise ValidationError("Age seems unrealistic")

        return age_int

    @staticmethod
    def validate_password(password):
        if not isinstance(password, str):
            raise ValidationError("Password must be string")
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters")
        if not any(c.isdigit() for c in password):
            raise ValidationError("Password must contain at least one digit")
        if not any(c.isupper() for c in password):
            raise ValidationError("Password must contain at least one uppercase letter")

        return password

# Pattern 4: Graceful degradation
def get_user_preferences(user_id, default_prefs=None):
    """Get user preferences with fallback to defaults"""
    if default_prefs is None:
        default_prefs = {"theme": "light", "language": "en"}

    try:
        # Try to get from database
        prefs = database.get_user_preferences(user_id)
        if not prefs:
            raise ValueError("No preferences found")
        return prefs
    except DatabaseError:
        logger.warning(f"Database error getting preferences for user {user_id}")
        try:
            # Try cache as fallback
            return cache.get_user_preferences(user_id)
        except CacheError:
            logger.warning(f"Cache error getting preferences for user {user_id}")
            # Use defaults as last resort
            return default_prefs
    except Exception as e:
        logger.error(f"Unexpected error getting preferences: {e}")
        return default_prefs
```

## **2. Resource Management Patterns**

```python
# Pattern 1: Context managers for automatic cleanup
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def __enter__(self):
        try:
            self.connection = connect_to_database(self.connection_string)
            return self.connection
        except Exception as e:
            raise ConnectionError(f"Failed to connect to database: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            try:
                self.connection.close()
            except Exception as e:
                logger.warning(f"Error closing database connection: {e}")

        # Don't suppress exceptions unless specifically handling them
        if exc_type is DatabaseError:
            logger.error(f"Database error occurred: {exc_val}")
            return True  # Suppress the exception
        return False  # Don't suppress other exceptions

# Usage
try:
    with DatabaseConnection("postgresql://localhost/mydb") as conn:
        result = conn.execute("SELECT * FROM users")
        return result
except ConnectionError as e:
    print(f"Could not connect to database: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

# Pattern 2: Multiple resource management
def process_files_safely(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            data = infile.read()
            processed_data = process_data(data)
            outfile.write(processed_data)
    except FileNotFoundError as e:
        raise ProcessingError(f"File not found: {e}")
    except PermissionError as e:
        raise ProcessingError(f"Permission denied: {e}")
    except Exception as e:
        raise ProcessingError(f"Processing failed: {e}")

# Pattern 3: Retry patterns with exponential backoff
import time
import random

def retry_with_backoff(func, max_retries=3, base_delay=1, max_delay=60):
    """Retry function with exponential backoff"""
    for attempt in range(max_retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            if attempt == max_retries - 1:  # Last attempt
                raise

            # Calculate delay with jitter
            delay = min(base_delay * (2 ** attempt), max_delay)
            jitter = random.uniform(0, delay * 0.1)
            total_delay = delay + jitter

            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {total_delay:.1f} seconds")
            time.sleep(total_delay)

    raise RuntimeError("All retry attempts exhausted")

# Usage
try:
    result = retry_with_backoff(lambda: call_external_api())
except RuntimeError:
    print("API call failed after all retries")
```

---

# **TESTING AND DEBUGGING EXCEPTION HANDLING**

## **1. Testing Exception Scenarios**

```python
import pytest
import unittest

# Pattern 1: Testing that exceptions are raised
def test_validation_errors():
    with pytest.raises(ValidationError):
        validate_email("invalid-email")

    with pytest.raises(ValidationError, match="Age cannot be negative"):
        validate_age(-5)

    # Test specific exception attributes
    with pytest.raises(DatabaseError) as exc_info:
        connect_to_database("invalid://connection")

    assert exc_info.value.error_code == "CONNECTION_FAILED"

# Pattern 2: Testing exception handling
def test_error_handling():
    # Test graceful error handling
    result = safe_divide(10, 0)
    assert result == "Cannot divide by zero"

    # Test successful operation
    result = safe_divide(10, 2)
    assert result == 5.0

    # Test exception information is preserved
    try:
        risky_operation()
        assert False, "Should have raised exception"
    except CustomError as e:
        assert "expected error message" in str(e)
        assert e.error_code == "EXPECTED_CODE"

# Pattern 3: Mocking to test exception scenarios
from unittest.mock import patch, Mock

def test_database_error_handling():
    with patch('mymodule.database') as mock_db:
        # Mock database to raise exception
        mock_db.get_user.side_effect = DatabaseError("Connection failed")

        # Test that our function handles it gracefully
        result = get_user_safely(123)
        assert result is None  # or whatever the expected fallback is

        # Verify error was logged
        assert "Database error" in captured_logs

# Pattern 4: Integration testing with real errors
def test_file_processing_errors(tmp_path):
    # Test with non-existent file
    with pytest.raises(FileNotFoundError):
        process_file("/path/that/does/not/exist")

    # Test with invalid content
    invalid_file = tmp_path / "invalid.txt"
    invalid_file.write_text("invalid content format")

    with pytest.raises(ValidationError):
        process_file(str(invalid_file))

    # Test with valid content
    valid_file = tmp_path / "valid.txt"
    valid_file.write_text("valid content format")

    result = process_file(str(valid_file))
    assert result is not None
```

## **2. Debugging Exception Patterns**

```python
import pdb
import traceback
import sys

# Pattern 1: Debug exception information
def debug_exception():
    try:
        problematic_function()
    except Exception as e:
        # Print detailed information
        print(f"Exception: {type(e).__name__}: {e}")
        print(f"Arguments: {e.args}")

        # Print traceback
        print("\nTraceback:")
        traceback.print_exc()

        # Get traceback as string for logging
        tb_str = traceback.format_exc()
        logger.error(f"Exception occurred:\n{tb_str}")

        # Debug interactively (use with caution in production)
        # pdb.post_mortem()

# Pattern 2: Enhanced error reporting
class ErrorReporter:
    @staticmethod
    def report_exception(e, context=None):
        """Report exception with full context"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "exception_type": type(e).__name__,
            "exception_message": str(e),
            "traceback": traceback.format_exc(),
            "context": context or {},
            "system_info": {
                "python_version": sys.version,
                "platform": sys.platform
            }
        }

        # Log to file
        logger.error("Exception report", extra=report)

        # Send to monitoring service (in production)
        # send_to_monitoring_service(report)

        return report

# Pattern 3: Exception context preservation
def enhanced_error_handling():
    context = {
        "user_id": get_current_user_id(),
        "operation": "data_processing",
        "input_size": len(input_data)
    }

    try:
        process_data(input_data)
    except Exception as e:
        # Add context to exception
        error_msg = f"Operation failed in context: {context}"

        # Create new exception with context
        enhanced_error = ProcessingError(error_msg)
        enhanced_error.original_exception = e
        enhanced_error.context = context

        raise enhanced_error from e

# Pattern 4: Performance monitoring for exceptions
class PerformanceMonitor:
    def __init__(self):
        self.exception_counts = {}
        self.performance_data = {}

    def monitor_function(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                self.performance_data[func.__name__] = execution_time
                return result
            except Exception as e:
                execution_time = time.time() - start_time
                exception_type = type(e).__name__

                # Track exception frequency
                self.exception_counts[exception_type] = self.exception_counts.get(exception_type, 0) + 1

                # Log performance data even for failures
                logger.warning(f"Function {func.__name__} failed after {execution_time:.3f}s with {exception_type}")

                raise
        return wrapper

    def get_stats(self):
        return {
            "exception_counts": self.exception_counts,
            "performance_data": self.performance_data
        }
```

---

# **REAL-WORLD APPLICATION PATTERNS**

## **1. Web Application Error Handling**

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Global error handlers
@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({"error": "Validation failed", "details": str(e)}), 400

@app.errorhandler(AuthenticationError)
def handle_auth_error(e):
    return jsonify({"error": "Authentication required"}), 401

@app.errorhandler(Exception)
def handle_general_error(e):
    logger.error(f"Unexpected error: {e}", exc_info=True)
    return jsonify({"error": "Internal server error"}), 500

# Route with comprehensive error handling
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    try:
        # Validate input
        if user_id <= 0:
            raise ValidationError("User ID must be positive")

        # Authenticate request
        auth_token = request.headers.get('Authorization')
        if not auth_token:
            raise AuthenticationError("Authorization header required")

        # Get user from database
        user = database.get_user(user_id)
        if not user:
            raise NotFoundError(f"User {user_id} not found")

        return jsonify(user.to_dict())

    except ValidationError:
        raise  # Let global handler deal with it
    except AuthenticationError:
        raise  # Let global handler deal with it
    except NotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except DatabaseError as e:
        logger.error(f"Database error getting user {user_id}: {e}")
        return jsonify({"error": "Service temporarily unavailable"}), 503
```

## **2. Data Pipeline Error Handling**

```python
class DataPipeline:
    def __init__(self):
        self.error_threshold = 0.1  # 10% error rate threshold
        self.logger = logging.getLogger(__name__)

    def process_batch(self, data_batch):
        """Process batch with comprehensive error handling"""
        results = []
        errors = []

        for i, item in enumerate(data_batch):
            try:
                # Validate item
                validated_item = self.validate_item(item)

                # Transform item
                transformed_item = self.transform_item(validated_item)

                # Save item
                saved_item = self.save_item(transformed_item)

                results.append(saved_item)

            except ValidationError as e:
                error_info = {
                    "index": i,
                    "item_id": item.get('id', 'unknown'),
                    "error_type": "validation",
                    "error_message": str(e),
                    "item_data": item
                }
                errors.append(error_info)
                self.logger.warning(f"Validation error for item {i}: {e}")

            except TransformationError as e:
                error_info = {
                    "index": i,
                    "item_id": item.get('id', 'unknown'),
                    "error_type": "transformation",
                    "error_message": str(e)
                }
                errors.append(error_info)
                self.logger.error(f"Transformation error for item {i}: {e}")

            except Exception as e:
                error_info = {
                    "index": i,
                    "item_id": item.get('id', 'unknown'),
                    "error_type": "unexpected",
                    "error_message": str(e)
                }
                errors.append(error_info)
                self.logger.error(f"Unexpected error for item {i}: {e}", exc_info=True)

        # Check if error rate is acceptable
        error_rate = len(errors) / len(data_batch)
        if error_rate > self.error_threshold:
            raise BatchProcessingError(
                f"Error rate {error_rate:.1%} exceeds threshold {self.error_threshold:.1%}",
                errors=errors,
                successful_items=len(results),
                total_items=len(data_batch)
            )

        return {
            "successful_items": results,
            "errors": errors,
            "summary": {
                "total_processed": len(data_batch),
                "successful": len(results),
                "failed": len(errors),
                "error_rate": error_rate
            }
        }
```

## **3. Configuration and Environment Error Handling**

```python
import os
from typing import Optional, Any

class ConfigurationManager:
    def __init__(self, config_file: str = None):
        self.config_file = config_file
        self.config = {}
        self.load_config()

    def load_config(self):
        """Load configuration with multiple fallbacks"""
        try:
            # Try to load from file first
            if self.config_file and os.path.exists(self.config_file):
                self.config.update(self._load_from_file(self.config_file))
        except Exception as e:
            logger.warning(f"Could not load config file {self.config_file}: {e}")

        # Load from environment variables
        self.config.update(self._load_from_environment())

        # Apply defaults
        self.config.update(self._get_defaults())

        # Validate required settings
        self._validate_required_config()

    def get(self, key: str, default: Any = None, required: bool = False) -> Any:
        """Get configuration value with error handling"""
        try:
            if key in self.config:
                return self.config[key]

            if required:
                raise ConfigurationError(
                    f"Required configuration key '{key}' not found",
                    config_key=key,
                    suggestion=f"Set environment variable {key.upper()} or add to config file"
                )

            return default

        except Exception as e:
            if required:
                raise
            logger.warning(f"Error getting config key '{key}': {e}")
            return default

    def get_int(self, key: str, default: int = None, required: bool = False) -> int:
        """Get integer configuration with validation"""
        value = self.get(key, default, required)
        if value is None:
            return None

        try:
            return int(value)
        except (ValueError, TypeError):
            if required:
                raise ConfigurationError(
                    f"Configuration key '{key}' must be an integer, got: {value}",
                    config_key=key,
                    suggestion="Ensure the value is a valid integer"
                )
            return default

    def _validate_required_config(self):
        """Validate that all required configuration is present"""
        required_keys = ['DATABASE_URL', 'SECRET_KEY']
        missing_keys = []

        for key in required_keys:
            if not self.config.get(key):
                missing_keys.append(key)

        if missing_keys:
            raise ConfigurationError(
                f"Missing required configuration keys: {missing_keys}",
                suggestion="Check your environment variables or configuration file"
            )
```

---

# **BEST PRACTICES SUMMARY**

## **Exception Handling Principles**

1. **Catch Specific Exceptions**: Always catch the most specific exception type possible
2. **Don't Ignore Exceptions**: Either handle them properly or let them propagate
3. **Use try/except/else/finally Appropriately**: Each block has a specific purpose
4. **Preserve Exception Context**: Use exception chaining with `raise ... from ...`
5. **Log Exceptions Properly**: Include context and traceback information
6. **Fail Fast**: Detect errors early and handle them appropriately
7. **Graceful Degradation**: Provide fallbacks when possible

## **Common Anti-Patterns to Avoid**

```python
# DON'T: Catch and ignore all exceptions
try:
    risky_operation()
except:  # Too broad, hides bugs
    pass  # Silently ignoring errors

# DON'T: Catch Exception without specific handling
try:
    risky_operation()
except Exception:  # Too general
    print("Something went wrong")  # Not helpful

# DON'T: Use exceptions for control flow
try:
    value = dictionary["key"]
except KeyError:
    value = "default"  # Use dict.get() instead

# DO: Specific, helpful exception handling
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Specific operation failed: {e}")
    return default_fallback_result()
except Exception as e:
    logger.error(f"Unexpected error in risky_operation: {e}", exc_info=True)
    raise  # Re-raise unexpected errors
```

## **Performance Considerations**

- Exception handling has overhead - don't use for normal control flow
- try/except is cheap when no exception occurs
- Raising and catching exceptions is expensive
- Use validation to prevent exceptions when possible
- Cache validation results for repeated checks

---

This comprehensive guide covers **all the different ways** to handle errors in Python. Master these patterns to write robust, maintainable code that handles the unexpected gracefully and provides excellent debugging information when things go wrong.
