# Advanced Calculator CLI — v1 (functions)
# Scope: primitives, I/O, control flow, functions (no exceptions yet)

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
    """Return (result, message). On divide-by-zero, (None, 'Cannot divide by zero')."""
    if b == 0:
        return None, "Cannot divide by zero"
    return a / b, "Success"


# --------------
# I/O Helpers
# --------------

def display_menu():
    print("\n" + "=" * 50)
    print("🧮 Calculator v1.0")
    choice = int(
        input(
            "- Menu -\n"
            "1) Add\n"
            "2) Subtract\n"
            "3) Multiply\n"
            "4) Divide\n"
            "5) Quit\n"
            "Choose an option (1-5): "
        )
    )
    return choice


def get_number(prompt):
    return float(input(prompt))


def format_equation(a, operation, b, result, message="Success"):
    """Format output. If result is None, show error + message."""
    if result is None:
        return f"{a:g} {operation} {b:g} = error ({message})"
    return f"{a:g} {operation} {b:g} = {result:.3f}"


# --------------
# Orchestrator
# --------------

def run_calculator():
    operations_count = 0

    while True:
        choice = display_menu()

        # Validate menu choice
        if choice < 1 or choice > 5:
            print("Invalid option. Please choose 1-5.")
            continue

        # Quit
        if choice == 5:
            print("Thank you for using Calculator v1.0!")
            print(f"Total operations performed: {operations_count}")
            break

        # Read operands once per loop
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        # Dispatch based on choice
        if choice == 1:
            operation = "+"
            result = add(a, b)
            result_msg = format_equation(a, operation, b, result)
            op_done = True

        elif choice == 2:
            operation = "-"
            result = subtract(a, b)
            result_msg = format_equation(a, operation, b, result)
            op_done = True

        elif choice == 3:
            operation = "*"
            result = multiply(a, b)
            result_msg = format_equation(a, operation, b, result)
            op_done = True

        elif choice == 4:
            operation = "/"
            result, msg = divide(a, b)
            result_msg = format_equation(a, operation, b, result, msg)
            op_done = result is not None

        # Print result + update counter if the op succeeded
        print(result_msg)
        if op_done:
            operations_count += 1
            print(f"Operations performed: {operations_count}")


if __name__ == "__main__":
    run_calculator()
