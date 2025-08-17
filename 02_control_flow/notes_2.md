# CONTROL FLOW - MASTERING CONDITIONAL LOGIC & LOOPS

# Control Flow = The order in which statements are executed in a program

# Allows programs to make decisions and repeat actions based on conditions

# COMPARISON OPERATORS

# Used to compare values and return True or False

# Formula: value1 operator value2 → True/False

```bash
# Equality and inequality
5 == 5          # -> True
5 != 3          # -> True
"hi" == "Hi"     # -> False (case-sensitive)

# Greater / Less (and inclusive versions)
7 > 3           # -> True
7 >= 7          # -> True
2 < 1           # -> False
2 <= 2          # -> True

# Comparing strings: lexicographic (Unicode) order
"apple" < "banana"  # -> True
"Z" < "a"           # -> True (uppercase < lowercase)

# Comparing different types: convert first
"5" == 5        # -> False
int("5") == 5    # -> True

# Chained comparisons (Pythonic range check)
x = 7
0 < x < 10      # -> True (x is between 0 and 10)
```

# CONDITIONAL STATEMENTS (if/elif/else)

# if statement - executes code only if condition is True

# Formula: if condition: do something

```bash
age = 18

if age >= 18:
    print("You are an adult")
# -> "You are an adult"
```

# if/else - choose between two paths

# Formula: if condition: X else: Y

```bash
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# -> "Odd number"
```

# if/elif/else - multiple conditions

# Formula: if cond1: X elif cond2: Y else: Z

```bash
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
# -> "Grade: B"
```

# Nested if statements

# Formula: if cond1: if cond2: X else: Y else: Z

```bash
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("Too young")
# -> "Access granted"
```

# TERNARY OPERATOR (Conditional Expression)

# A one-line shortcut for the if/else statement

# Formula: X if condition else Y

# Prints or assigns one of two values based on the condition

```bash
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)
# -> "Adult"
```

# LOGICAL OPERATORS

# Combine multiple conditions

# Formula: condition1 and/or/not condition2 → True/False

```bash
# and: both must be True
x = 5
y = 10
x > 0 and y > 0   # -> True

# or: at least one must be True
x < 0 or y > 0    # -> True

# not: negates the condition
not(x > 0)        # -> False
```

# Complex logical expressions

```bash
age = 25
has_ticket = True
has_id = False

if (age >= 18 and has_ticket) or has_id:
    print("Entry allowed")
else:
    print("Entry denied")
# -> "Entry allowed"
```

# SHORT-CIRCUIT EVALUATION

# Python stops evaluating as soon as it knows the result

```bash
# 'or' stops if first condition is True
True or print("This will not run")  # -> True

# 'and' stops if first condition is False
False and print("This will not run") # -> False
```

# CHAINING COMPARISON OPERATORS

# Python allows chaining multiple comparisons

# Formula: a < b < c < d

```bash
x = 5
print(0 < x < 10)   # -> True
print(0 < x < 3)    # -> False
```

# FOR LOOPS

# Iterate over sequences (strings, lists, ranges)

# Formula: for variable in sequence: do something

```bash
# Iterate over a range
for i in range(5):
    print(i)
# -> 0 1 2 3 4

# Iterate over a string
for char in "hello":
    print(char)
# -> h e l l o

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# -> apple banana cherry
```

# FOR-ELSE STATEMENT

# else block executes when loop completes normally (no break)

# Formula: for var in sequence: ... else: ...

```bash
for i in range(3):
    print(i)
else:
    print("Loop finished")
# -> 0 1 2  \n "Loop finished"

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop finished")
# -> 0 (else skipped because of break)
```

# NESTED LOOPS

# Loops inside loops

# Formula: for x in seq1: for y in seq2: do something

```bash
for x in range(2):
    for y in range(3):
        print(f"x={x}, y={y}")
# -> x=0,y=0  x=0,y=1  x=0,y=2  x=1,y=0  x=1,y=1  x=1,y=2
```

# WHILE LOOPS

# Repeat code while condition is True

# Formula: while condition: do something

```bash
count = 0
while count < 5:
    print(count)
    count += 1
# -> 0 1 2 3 4
```

# Counter-controlled while loop

```bash
num = 3
while num > 0:
    print("Countdown:", num)
    num -= 1
# -> 3 2 1
```

# INFINITE LOOPS

# Loops that run forever (usually with break to exit)

```bash
while True:
    cmd = input("Type 'exit' to quit: ")
    if cmd == "exit":
        break
```

# BREAK AND CONTINUE

# Control flow within loops

# break = exit loop entirely

# continue = skip to next iteration

```bash
# break example
for i in range(5):
    if i == 3:
        break
    print(i)
# -> 0 1 2

# continue example
for i in range(5):
    if i == 2:
        continue
    print(i)
# -> 0 1 3 4
```

# WHILE-ELSE STATEMENT

# else block executes when while loop completes normally (no break)

# Formula: while condition: ... else: ...

```bash
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished")
# -> 0 1 2  \n "Loop finished"

count = 0
while count < 3:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print("Loop finished")
# -> 0 (else skipped because of break)
```

# KEY CONCEPTS SUMMARY

## Comparison Operators

- `==` - Equal to
- `!=` - Not equal to
- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal to
- `>=` - Greater than or equal to

## Logical Operators

- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `not` - Negates the condition

## Control Flow Structures

- `if/elif/else` - Conditional execution
- `for` - Iterate over sequences
- `while` - Repeat while condition is True
- `break` - Exit loop immediately
- `continue` - Skip to next iteration

## Loop Patterns

- `for-else` - Execute else when loop completes normally
- `while-else` - Execute else when while loop completes normally
- `while True` - Infinite loop with break
- Nested loops - Loops inside loops

## Best Practices

- Use meaningful variable names
- Keep conditions simple and readable
- Use break/continue sparingly
- Avoid infinite loops without exit conditions
- Use chained comparisons for ranges
- Leverage short-circuit evaluation for safety

## Common Patterns

- Input validation loops
- Search patterns with for-else
- Menu systems with while True
- Counter-controlled loops
- Nested loops for grids/tables
