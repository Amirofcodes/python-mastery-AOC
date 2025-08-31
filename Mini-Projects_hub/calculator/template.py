# Advanced Calculator - Template for Progressive Learning
#
# Instructions:
# 1. Copy this template to calculator_v1.py to start fresh practice
# 2. Complete each section by typing the solution yourself to build muscle memory
# 3. Only use concepts from Primitive Types + Control Flow + Functions (sections 01-03)
# 4. Focus on pure functions, I/O separation, and error handling
# 5. Test each operation thoroughly before moving to the next
#
# Learning Goals: Master function design, pure math operations, and clean architecture
# Real-World Application: Build professional calculation tools with robust error handling
#
# ===== PROJECT OVERVIEW =====
#
# Build a menu-driven calculator with clean function architecture:
# - Basic operations: add, subtract, multiply, divide
# - Safe division with error handling
# - Pure math functions (no I/O inside)
# - I/O helpers for user interaction
# - Operation counter and session tracking
#
# Core Principles:
# - Separation of concerns (math vs I/O)
# - Pure functions return values
# - Error handling via return values
# - No global state mutation
#
# ===== FUNCTION DESIGN PATTERNS =====

# ===== PURE MATH FUNCTIONS (No I/O) =====
# TODO: Implement basic arithmetic operations
# Core concept: Pure functions with clear inputs/outputs

def add(a, b):
    """Add two numbers and return the result."""
    # TODO: Implement addition
    # return a + b
    pass


def subtract(a, b):
    """Subtract b from a and return the result."""
    # TODO: Implement subtraction
    # return a - b
    pass


def multiply(a, b):
    """Multiply two numbers and return the result."""
    # TODO: Implement multiplication
    # return a * b
    pass


def divide(a, b):
    """Divide a by b with safe error handling.

    Returns:
        tuple: (result, message) where result is None on error
    """
    # TODO: Implement safe division with error handling
    # Core concept: Return tuple for error handling without exceptions
    # if b == 0:
    #     return None, "Cannot divide by zero"
    # return a / b, "Success"
    pass


# ===== I/O HELPER FUNCTIONS (Handle User Interaction) =====

def display_menu():
    """Display calculator menu and get user choice."""
    # TODO: Implement menu display and input
    # Core concept: Centralized menu logic
    # print("\n" + "=" * 50)
    # print("🧮 Calculator v1.0")
    # choice = int(
    #     input(
    #         "- Menu -\n"
    #         "1) Add\n"
    #         "2) Subtract\n"
    #         "3) Multiply\n"
    #         "4) Divide\n"
    #         "5) Quit\n"
    #         "Choose an option (1-5): "
    #     )
    # )
    # return choice
    pass


def get_number(prompt):
    """Get a number from user with given prompt."""
    # TODO: Implement number input
    # Core concept: Reusable input helper
    # return float(input(prompt))
    pass


def format_equation(a, operation, b, result, message="Success"):
    """Format calculation result for display.

    Args:
        a: First operand
        operation: Operation symbol (+, -, *, /)
        b: Second operand
        result: Calculation result (None if error)
        message: Status message

    Returns:
        str: Formatted equation string
    """
    # TODO: Implement result formatting
    # Core concept: Consistent output formatting
    # if result is None:
    #     return f"{a:g} {operation} {b:g} = error ({message})"
    # return f"{a:g} {operation} {b:g} = {result:.3f}"
    pass


# ===== MAIN ORCHESTRATOR FUNCTION =====

def run_calculator():
    """Main calculator loop orchestrating all operations."""
    # TODO: Implement main program logic
    # Core concept: Central coordinator using helper functions

    # Initialize session state
    # operations_count = 0

    # while True:
    # TODO: Get menu choice
    # choice = display_menu()

    # TODO: Handle menu validation
    # if choice < 1 or choice > 5:
    #     print("Invalid option. Please choose 1-5.")
    #     continue

    # TODO: Handle quit option
    # if choice == 5:
    #     print("Thank you for using Calculator v1.0!")
    #     print(f"Total operations performed: {operations_count}")
    #     break

    # TODO: Get operands for calculations
    # a = get_number("Enter first number: ")
    # b = get_number("Enter second number: ")

    # TODO: Dispatch operations based on choice
    # op_done = False
    # result = None
    # result_msg = ""

    # if choice == 1:  # Addition
    #     operation = "+"
    #     result = add(a, b)
    #     result_msg = format_equation(a, operation, b, result)
    #     op_done = True

    # elif choice == 2:  # Subtraction
    #     operation = "-"
    #     result = subtract(a, b)
    #     result_msg = format_equation(a, operation, b, result)
    #     op_done = True

    # elif choice == 3:  # Multiplication
    #     operation = "*"
    #     result = multiply(a, b)
    #     result_msg = format_equation(a, operation, b, result)
    #     op_done = True

    # elif choice == 4:  # Division
    #     operation = "/"
    #     result, msg = divide(a, b)
    #     result_msg = format_equation(a, operation, b, result, msg)
    #     op_done = result is not None

    # TODO: Display result and update counter
    # print(result_msg)
    # if op_done:
    #     operations_count += 1
    #     print(f"Operations performed: {operations_count}")

    pass


# ===== PROGRAM ENTRY POINT =====

if __name__ == "__main__":
    # TODO: Call main function
    # run_calculator()
    pass

# ===== TESTING CHECKLIST =====
#
# □ All four basic operations work correctly
# □ Division by zero handled gracefully
# □ Pure functions contain no print/input statements
# □ I/O functions handle user interaction cleanly
# □ Operation counter tracks successful calculations
# □ Menu validation prevents crashes
# □ Results formatted consistently
#
# ===== FUNCTION DESIGN PRINCIPLES =====
#
# 1. Pure Functions (Math):
#    - Take parameters, return values
#    - No side effects (print, input, global variables)
#    - Easy to test and reuse
#    - Predictable behavior
#
# 2. I/O Functions:
#    - Handle user interaction
#    - Keep UI logic separate from business logic
#    - Reusable across different interfaces
#
# 3. Orchestrator:
#    - Coordinates between pure functions and I/O
#    - Manages program flow and state
#    - Single responsibility for main loop
#
# ===== ERROR HANDLING PATTERNS =====
#
# 1. Return Values (Current):
#    - divide() returns (result, message) tuple
#    - None indicates error condition
#    - Message provides user-friendly explanation
#
# 2. Future Enhancements:
#    - Exception handling (Section 05)
#    - Input validation with retry loops
#    - Type checking and conversion
#
# ===== ENHANCEMENT IDEAS (For Later Versions) =====
#
# v2 (Exceptions): Add comprehensive error handling and input validation
# v2.1 (Memory): Add memory operations (store, recall, clear)
# v2.2 (Advanced): Add power, square root, percentage operations
# v3 (Classes): Create Calculator class with state management
# v4 (History): Add calculation history and replay functionality
# v5 (Scientific): Add trigonometric and logarithmic functions
#
# ===== DEBUGGING TIPS =====
#
# 1. Test each function individually with known values
# 2. Verify division by zero handling
# 3. Check that pure functions don't print anything
# 4. Ensure counter only increments on successful operations
# 5. Test menu validation with invalid inputs
# 6. Verify result formatting for various number types
