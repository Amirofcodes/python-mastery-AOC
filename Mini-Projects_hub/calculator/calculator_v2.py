# Advanced Calculator CLI — v2.0 (exceptions)
# Scope: primitives, I/O, control flow, functions + robust exception handling
# Features: Bulletproof input validation, memory operations, error logging

# Constants and global state
ERROR_LOG = []  # Track session errors for statistics
MEMORY = 0.0    # Calculator memory storage

# -------------------------------
# Operations (pure math functions)
# -------------------------------


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Enhanced division with proper exception handling."""
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        # Check for overflow/underflow
        if result != result:  # NaN check
            raise ValueError("Division resulted in NaN")
        if result in (float('inf'), float('-inf')):
            raise OverflowError("Division resulted in infinity")
        return result, "Success"
    except ZeroDivisionError as e:
        return None, str(e)
    except (OverflowError, ValueError) as e:
        return None, f"Math error: {e}"
    except Exception as e:
        return None, f"Unexpected calculation error: {e}"


def power(a, b):
    """Calculate a^b with refined overflow protection."""
    try:
        # Prevent extremely large exponents
        if abs(b) > 1000:
            raise ValueError("Exponent too large (limit: ±1000)")
        # Guard against negative base with fractional exponent
        if a < 0 and not float(b).is_integer():
            raise ValueError("Negative base requires an integer exponent")
        # Only block huge base when exponent magnitude > 1 (allows safe cases like 1e120^1)
        if abs(a) > 1e154 and abs(b) > 1:
            raise ValueError("Base too large for exponent > 1")

        result = a ** b

        # Check for overflow/underflow
        if result != result:  # NaN
            raise ValueError("Power calculation resulted in NaN")
        if result in (float('inf'), float('-inf')):
            raise OverflowError("Power calculation resulted in infinity")

        return result, "Success"
    except (ValueError, OverflowError) as e:
        return None, str(e)
    except Exception as e:
        return None, f"Unexpected power error: {e}"


def memory_store(value):
    """Store value in memory."""
    global MEMORY
    try:
        if value != value:  # NaN check
            raise ValueError("Cannot store NaN in memory")
        if value in (float('inf'), float('-inf')):
            raise ValueError("Cannot store infinity in memory")
        MEMORY = value
        return f"Stored {value:.6g} in memory"
    except Exception as e:
        return f"Memory store error: {e}"


def memory_recall():
    """Recall value from memory."""
    return MEMORY


def memory_clear():
    """Clear memory."""
    global MEMORY
    MEMORY = 0.0
    return "Memory cleared"


def _reset_session():
    """Reset session state for unit testing."""
    global ERROR_LOG, MEMORY
    ERROR_LOG.clear()
    MEMORY = 0.0


def _is_finite(x):
    """Check if a number is finite (not NaN or ±infinity)."""
    return not (isinstance(x, float) and (x != x or x in (float('inf'), float('-inf'))))


# --------------
# Safe Input Functions (bulletproof I/O)
# --------------

def log_error(error_type, message):
    """Log errors for session statistics."""
    ERROR_LOG.append({"type": error_type, "message": message})


def safe_get_menu_choice():
    """Get menu choice with comprehensive validation."""
    while True:
        try:
            choice = int(input("Choose an option (1-8): "))
        except ValueError:
            print("❌ Please enter a valid number")
            log_error("ValueError", "Invalid menu choice input")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)
        else:
            if 1 <= choice <= 8:
                return choice
            print("❌ Please choose a number between 1-8")
            log_error("ValueError", "Menu choice out of range")


def safe_get_number(prompt):
    """Get a number with comprehensive validation."""
    while True:
        try:
            raw = input(prompt)
            value = float(raw)

            # Block non-finite numbers
            if value != value:  # NaN
                print("❌ Please enter a valid finite number (NaN not allowed)")
                log_error("ValueError", "NaN input detected")
                continue
            if value in (float('inf'), float('-inf')):
                print("❌ Please enter a finite number (infinity not allowed)")
                log_error("ValueError", "Infinity input detected")
                continue

            # Check for extremely large numbers that might cause issues
            if abs(value) >= 1e308:
                print("❌ Number too large for calculations")
                log_error("ValueError", "Number too large")
                continue

            return value

        except ValueError:
            print("❌ Please enter a valid number")
            log_error("ValueError", "Invalid number input")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)


def display_menu():
    """Display enhanced menu with memory operations."""
    print("\n" + "=" * 55)
    print("🧮 Advanced Calculator v2.0 - Bulletproof Edition 🛡️")
    print("- Main Menu -")
    print("1) Add (+)")
    print("2) Subtract (-)")
    print("3) Multiply (×)")
    print("4) Divide (÷)")
    print("5) Power (^)")
    print("6) Memory Operations")
    print("7) Session Statistics")
    print("8) Quit")
    print("=" * 55)

    return safe_get_menu_choice()


def display_memory_menu():
    """Display memory operations menu."""
    print("\n📱 Memory Operations:")
    print("1) Store result in memory (MS)")
    print("2) Recall from memory (MR)")
    print("3) Clear memory (MC)")
    print("4) Back to main menu")

    while True:
        try:
            choice = int(input("Choose memory operation (1-4): "))
        except ValueError:
            print("❌ Please enter a valid number")
            log_error("ValueError", "Invalid memory menu input")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)
        else:
            if 1 <= choice <= 4:
                return choice
            print("❌ Please choose 1-4")
            log_error("ValueError", "Memory menu choice out of range")


def format_equation(a, operation, b, result, message="Success"):
    """Format output with enhanced error handling and finite result validation."""
    def _nonfinite(x):
        return isinstance(x, float) and (x != x or x in (float('inf'), float('-inf')))

    if result is None or _nonfinite(result):
        if result is not None and _nonfinite(result):
            message = "Non-finite result (overflow/NaN)"
        log_error("CalculationError",
                  f"{operation} operation failed: {message}")
        return f"❌ {a:g} {operation} {b:g} = ERROR ({message})"

    return f"✅ {a:g} {operation} {b:g} = {result:.6g}"


def display_statistics():
    """Display session statistics and error log."""
    print("\n📊 Session Statistics:")
    print(f"Total errors logged: {len(ERROR_LOG)}")
    print(f"Current memory value: {MEMORY:.6g}")

    if ERROR_LOG:
        print("\n🔍 Error Summary:")
        error_types = {}
        for error in ERROR_LOG:
            error_type = error["type"]
            error_types[error_type] = error_types.get(error_type, 0) + 1

        for error_type, count in error_types.items():
            print(f"  {error_type}: {count} occurrence(s)")

        print("\n📝 Recent Errors (last 5):")
        for error in ERROR_LOG[-5:]:
            print(f"  - {error['type']}: {error['message']}")
    else:
        print("🎉 No errors recorded this session!")


# --------------
# Enhanced Orchestrator with Comprehensive Exception Handling
# --------------

def handle_memory_operations(last_result=None):
    """Handle memory operations with error recovery."""
    while True:
        try:
            choice = display_memory_menu()

            if choice == 1:  # Store
                if last_result is not None:
                    msg = memory_store(last_result)
                    print(f"💾 {msg}")
                else:
                    print("❌ No result to store. Perform a calculation first.")
                    log_error("MemoryError", "No result to store")
                break

            elif choice == 2:  # Recall
                value = memory_recall()
                print(f"📤 Memory recall: {value:.6g}")
                break

            elif choice == 3:  # Clear
                msg = memory_clear()
                print(f"🗑️ {msg}")
                break

            elif choice == 4:  # Back
                break

        except Exception as e:
            print(f"❌ Memory operation error: {e}")
            log_error("MemoryError", str(e))


def run_calculator():
    """Main calculator loop with bulletproof exception handling."""
    # Welcome banner
    print("🎉 Welcome to Advanced Calculator v2.0!")
    print("🛡️ Now with bulletproof error handling and memory operations!")
    print("🧪 Try invalid inputs - the calculator won't crash! 🚀")

    operations_count = 0
    last_result = None

    while True:
        try:
            choice = display_menu()

            # Quit
            if choice == 8:
                print("\n👋 Thank you for using Advanced Calculator v2.0!")
                print(f"📊 Total successful operations: {operations_count}")
                if ERROR_LOG:
                    print(
                        f"⚠️ Total errors handled gracefully: {len(ERROR_LOG)}")
                print("🎯 No crashes occurred - bulletproof success! 🛡️")
                break

            # Memory operations
            elif choice == 6:
                handle_memory_operations(last_result)
                continue

            # Session statistics
            elif choice == 7:
                display_statistics()
                continue

            # Mathematical operations (1-5)
            try:
                # Get operands with validation
                a = safe_get_number("Enter first number: ")

                # For power operation, get second operand before showing warning
                if choice == 5:
                    print("⚠️ Power operations have safety limits to prevent overflow")
                    b = safe_get_number("Enter exponent: ")
                else:
                    b = safe_get_number("Enter second number: ")

                # Dispatch operations
                op_done = False
                result = None

                if choice == 1:  # Add
                    try:
                        result = add(a, b)
                        result_msg = format_equation(a, "+", b, result)
                        op_done = _is_finite(result)
                    except Exception as e:
                        result_msg = format_equation(a, "+", b, None, str(e))
                        op_done = False

                elif choice == 2:  # Subtract
                    try:
                        result = subtract(a, b)
                        result_msg = format_equation(a, "-", b, result)
                        op_done = _is_finite(result)
                    except Exception as e:
                        result_msg = format_equation(a, "-", b, None, str(e))
                        op_done = False

                elif choice == 3:  # Multiply
                    try:
                        result = multiply(a, b)
                        result_msg = format_equation(a, "×", b, result)
                        op_done = _is_finite(result)
                    except Exception as e:
                        result_msg = format_equation(a, "×", b, None, str(e))
                        op_done = False

                elif choice == 4:  # Divide
                    result, message = divide(a, b)
                    result_msg = format_equation(a, "÷", b, result, message)
                    op_done = (result is not None) and _is_finite(result)

                elif choice == 5:  # Power
                    result, message = power(a, b)
                    result_msg = format_equation(a, "^", b, result, message)
                    op_done = (result is not None) and _is_finite(result)

                # Display result and update counters
                print(result_msg)
                if op_done:
                    operations_count += 1
                    last_result = result
                    print(f"📈 Successful operations: {operations_count}")

                    # Offer to store result in memory
                    if result is not None:
                        try:
                            store = input(
                                "💾 Store result in memory? (y/n): ").lower().strip()
                            if store in ('y', 'yes'):
                                msg = memory_store(result)
                                print(f"✅ {msg}")
                        except (KeyboardInterrupt, EOFError):
                            print("\n👋 Goodbye!")
                            break
                        except Exception as e:
                            print(f"⚠️ Skipping memory store: {e}")
                            log_error("MemoryPromptError", str(e))

            except (KeyboardInterrupt, EOFError):
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Input error: {e}")
                log_error("InputError", str(e))
                continue

        except Exception as e:
            # Ultimate safety net - should never reach here with proper input validation
            print(f"❌ Unexpected error: {e}")
            print("🔄 Returning to main menu...")
            log_error("UnexpectedError", str(e))
            continue


if __name__ == "__main__":
    run_calculator()
