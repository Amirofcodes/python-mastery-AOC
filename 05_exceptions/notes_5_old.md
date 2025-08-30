# EXCEPTIONS - MASTERING ERROR HANDLING

# Exceptions = runtime errors that interrupt the normal flow of a program.

# Instead of crashing, we can "handle" them with try/except blocks.

---

## Basic try/except

**Formula:**

```python
try:
    # code that might fail
except SomeError:
    # code that runs if error happens
```

**Example:**

```python
x = int("123")
print(x)

try:
    y = int("hello")  # this will raise ValueError
except ValueError:
    print("Invalid number!")
```

**Output:**

```
123
Invalid number!
```

---

## Handling Multiple Exceptions

**Formula:**

```python
try:
    risky_code()
except ValueError:
    handle_value_error()
except ZeroDivisionError:
    handle_zero_division()
```

**Example:**

```python
nums = [10, 0, "a"]

for n in nums:
    try:
        print(10 / int(n))
    except ValueError:
        print("Not a number!")
    except ZeroDivisionError:
        print("Can't divide by zero!")
```

**Output:**

```
1.0
Can't divide by zero!
Not a number!
```

---

## else and finally

- `else` runs if no exception was raised.
- `finally` always runs (good for cleanup).

**Formula:**

```python
try:
    code
except SomeError:
    handle
else:
    run_if_no_error
finally:
    always_run_this
```

**Example:**

```python
try:
    num = int("42")
except ValueError:
    print("Bad input")
else:
    print("Converted successfully!", num)
finally:
    print("Done!")
```

**Output:**

```
Converted successfully! 42
Done!
```

---

## Raising Exceptions

We can trigger errors ourselves with `raise`.

**Formula:**

```python
raise SomeError("message")
```

**Example:**

```python
def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b

print(safe_divide(10, 2))
print(safe_divide(5, 0))
```

**Output:**

```
5.0
Traceback (most recent call last):
  ...
ZeroDivisionError: b must not be zero
```

---

## The with Statement (Context Managers)

Many resources (files, network connections) need to be cleaned up.
`with` ensures cleanup automatically.

**Formula:**

```python
with resource as var:
    use(var)
```

**Example:**

```python
with open("test.txt", "w") as f:
    f.write("Hello!")

# file is closed automatically
```

---

# KEY CONCEPTS SUMMARY

## try/except basics

- `try/except` prevents crashes by catching exceptions.
- `except TypeError:` handles only that error.

## else/finally

- `else` runs only if no error happened.
- `finally` runs no matter what.

## Raising exceptions

- `raise ValueError("msg")` to signal an error.

## Multiple exceptions

- Catch specific errors in separate `except` blocks.

## with statement

- Ensures cleanup (file closed, lock released, etc.).

## Best Practices

- Catch specific exceptions, not `except:` alone.
- Use `finally` for cleanup tasks.
- Raise exceptions to enforce rules.
- Use `with` for files/resources to avoid leaks.
