# 03 · Functions — Beginner Notes (Read Before Drills)

Functions let you name a task, reuse it, and test it. Start small and keep them focused.

---

## What is a function?

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ana")
```

- `def` starts a function definition
- parameters go in parentheses
- body is indented

---

## Return values vs printing

```python
def add(a, b):
    return a + b  # returns data to the caller

def print_sum(a, b):
    print(a + b)  # side effect only

result = add(2, 3)
print(result)  # 5
```

Prefer returning values for logic; print in the outer layer (CLI).

---

## Parameters and Arguments

```python
def rectangle_area(length, width):
    return length * width

area = rectangle_area(5, 3)  # arguments
```

---

## Default Parameters

```python
def make_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(make_greeting("Ben"))          # Hello, Ben!
print(make_greeting("Cleo", "Hi"))   # Hi, Cleo!
```

Rules:

- Defaults are used when you don't pass a value
- Keep defaults simple (avoid mutable defaults)

---

## Keyword Arguments

```python
def profile(name, age, city):
    return f"{name} ({age}) from {city}"

print(profile(city="Paris", age=30, name="Ana"))
```

---

## Variable Arguments (`*args`)

```python
def total(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(total(1, 2, 3))  # 6
```

---

## Scope (local vs global)

```python
counter = 0  # global

def increment():
    global counter
    counter += 1
    return counter
```

Use `global` sparingly. Prefer passing values in/out of functions.

---

## Nested Functions and Closures

```python
def multiplier(factor):
    def apply(x):
        return x * factor
    return apply

double = multiplier(2)
print(double(5))  # 10
```

---

## Higher‑order Functions and Lambdas (simple anonymous functions)

```python
def apply_all(numbers, op):
    out = []
    for n in numbers:
        out.append(op(n))
    return out

square = lambda x: x * x
print(apply_all([1, 2, 3], square))
```

Use lambdas for tiny throwaway functions only.

---

## The Main Guard (safe script entry)

```python
def run():
    print("Running...")

if __name__ == "__main__":
    run()
```

Prevents auto‑execution when importing functions from this file.

---

## Mini Reference

- Define: `def name(params): ...`
- Return: `return value`
- Defaults: `def f(x=10): ...`
- Varargs: `def f(*args): ...`
- Keyword args call: `f(name="Ada", age=35)`
- Main guard: `if __name__ == "__main__": ...`
