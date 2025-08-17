# FUNCTIONS - MASTERING CODE ORGANIZATION & REUSABILITY

# Functions = Reusable blocks of code that perform specific tasks

# Allow breaking complex problems into smaller, manageable pieces

```bash
# Function formula
# def function_name(parameters):
#     """optional docstring"""
#     code block
#     return value (optional)
```

# Example

```bash
def greet():
    print("Hello, world!")

greet()  # -> "Hello, world!"
```

# RETURN STATEMENTS

# Functions can return values using 'return' keyword

# Formula: return expression

```bash
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
# -> 7
```

# Return vs Print

```bash
def square(x):
    return x * x

print(square(5))  # -> 25
# return gives a value back; print only displays text
```

# FUNCTION ARGUMENTS

# Positional arguments - order matters

# Formula: function(arg1, arg2, ...)

```bash
def divide(a, b):
    return a / b

print(divide(10, 2))  # -> 5.0
```

# Variable number of arguments

# Formula: \*args → tuple of extra arguments

```bash
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))  # -> 10
```

# KEYWORD ARGUMENTS

# Named arguments - order doesn't matter

# Formula: function(param=value)

```bash
def greet(name, message):
    print(f"{message}, {name}!")

greet(name="Amiro", message="Welcome")
# -> "Welcome, Amiro!"
```

# Keyword-only arguments (after \*)

```bash
def configure(*, debug=False):
    print("Debug mode:", debug)

configure(debug=True)  # -> Debug mode: True
```

# DEFAULT ARGUMENTS

# Parameters with default values

# Formula: def func(param=value)

```bash
def greet(name="Guest"):
    print("Hello", name)

greet()           # -> Hello Guest
greet("Amiro")     # -> Hello Amiro
```

# Default argument gotchas

```bash
def append_item(item, items=[]):
    items.append(item)
    return items

print(append_item(1))  # -> [1]
print(append_item(2))  # -> [1, 2]  (list reused!)
```

# FUNCTION SCOPE

# Variable shadowing

```bash
x = 10

def func():
    x = 5  # local variable shadows global
    print(x)

func()  # -> 5
print(x)  # -> 10
```

# Global keyword

```bash
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # -> 1
```

# Local vs Global variables

```bash
global_var = "I am global"

def test_scope():
    local_var = "I am local"
    print(global_var)
    print(local_var)

test_scope()
# -> "I am global"
# -> "I am local"
```

# NESTED FUNCTIONS

# Functions inside functions

# Formula: def outer(): def inner(): ...

```bash
def outer():
    def inner():
        return "Hello from inner"
    return inner()

print(outer())  # -> Hello from inner
```

# FUNCTION TYPES

# Pure functions - same input always gives same output

```bash
def pure_add(a, b):
    return a + b
```

# Functions with side effects

```bash
state = []
def add_item(x):
    state.append(x)  # modifies external variable
```

# Higher-order functions - take or return other functions

```bash
def apply(func, value):
    return func(value)

print(apply(lambda x: x**2, 3))  # -> 9
```

# LAMBDA FUNCTIONS

# Anonymous functions for simple operations

# Formula: lambda parameters: expression

```bash
square = lambda x: x * x
print(square(4))  # -> 16
```

# RUNNING SCRIPTS SAFELY (THE MAIN GUARD)

# Why this matters

# - When Python loads a file, it sets a built-in variable **name**.

# - If the file is executed directly, **name** == "**main**".

# - If imported, **name** is the module name, so the guarded block does NOT run.

# - This lets you keep reusable functions importable without triggering CLI logic.

```bash
# Formula:
if __name__ == "__main__":
    # code runs only when executed directly
    main()
```

# COMMON FUNCTION PATTERNS

# Input validation pattern

```bash
def get_age():
    while True:
        age = input("Enter age: ")
        if age.isdigit():
            return int(age)
        print("Invalid input, try again.")
```

# Configuration pattern

```bash
def setup(debug=False):
    if debug:
        print("Debug mode on")
    else:
        print("Normal mode")
```

# Factory pattern

```bash
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(5))  # -> 10
```

# Use a guard to prevent top-level code from running on import

```bash
def main():
    print("Program running")

if __name__ == "__main__":
    main()
```

# KEY CONCEPTS SUMMARY

## Function Definition

- `def function_name(parameters):` - Define a function
- `return value` - Return a value from function
- Function names should be verbs in snake_case

## Parameters and Arguments

- **Positional arguments** - Order matters
- **Keyword arguments** - Named parameters
- **Default parameters** - Optional with default values
- **\*args** - Variable number of positional arguments
- **\*\*kwargs** - Variable number of keyword arguments

## Scope

- **Local scope** - Variables inside function
- **Global scope** - Variables outside all functions
- **global keyword** - Modify global variables inside functions
- **Variable shadowing** - Local variables hide global ones

## Function Types

- **Pure functions** - No side effects, same input → same output
- **Functions with side effects** - Modify global state or print
- **Higher-order functions** - Take functions as parameters
- **Lambda functions** - Anonymous functions for simple operations

## Best Practices

- Functions should do one thing well
- Use descriptive names for functions and parameters
- Keep functions small and focused
- Use return values rather than printing when possible
- Validate input parameters
- Use default parameters for optional settings
- Avoid mutable default arguments

## Common Patterns

- Input validation with error handling
- Configuration functions with defaults
- Factory functions that create other functions
- Debugging with print statements and return codes
- Pure functions for calculations
- Side-effect functions for I/O operations

## Debugging

- Use print statements to trace execution
- Return error codes and messages
- Test functions with different inputs
- Use meaningful variable names
- Break complex functions into smaller ones

---

# TYPE HINTS (PREVIEW)

- What: optional annotations that describe parameter and return types. Example: `def add(a: float, b: float) -> float:`
- Why: improves readability, editor help, and static analysis. Python ignores hints at runtime (no behavior change).
- When: keep v1 solutions without hints if you prefer; we’ll start using hints more after Exceptions and Data Structures.
