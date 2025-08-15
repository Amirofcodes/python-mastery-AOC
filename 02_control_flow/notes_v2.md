# 02 · Control Flow — Beginner Notes (Read Before Drills)

These notes are a short, beginner‑friendly mini‑course. Read them once, type the examples, then solve the drills.

---

## What is Control Flow?

- Control flow is the order in which Python executes statements.
- It lets programs make decisions (if/elif/else) and repeat work (loops) based on conditions.

---

## Comparison Operators (make True/False)

```python
x = 10
y = 12
print(x == y)   # False (equal?)
print(x != y)   # True  (not equal?)
print(x < y)    # True  (less than)
print(x >= 10)  # True  (greater or equal)
```

Why it matters: Comparisons are the inputs to your decisions.

---

## If / Elif / Else (make decisions)

```python
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")
```

Tips:

- Use elif for mutually exclusive branches.
- Use else for the “everything else” case.

---

## Logical Operators (combine conditions)

```python
temp = 22
is_sunny = True

print(temp >= 20 and temp <= 26)  # AND: both must be True
print(is_sunny or temp > 30)      # OR: at least one True
print(not is_sunny)               # NOT: flips True/False
```

Real use:

```python
email = "user@example.com"
looks_ok = ("@" in email) and ("." in email)
```

---

## Short‑circuit Evaluation (skip unsafe work)

Python stops as soon as the result is known.

```python
numerator = 10
denominator = 0

# Safe: second part runs only if denominator != 0
if denominator != 0 and (numerator / denominator) > 2:
    print("> 2")
```

---

## Ternary Operator (tiny if/else)

```python
n = 7
parity = "even" if n % 2 == 0 else "odd"
print(parity)
```

Use for simple choices. Prefer normal if/else for bigger blocks.

---

## Chained Comparisons (clean ranges)

```python
temperature = 24
if 20 <= temperature <= 26:
    print("Comfortable")
```

---

## For Loops (repeat over sequences)

```python
for char in "Python":
    print(char)

for i in range(3):
    print(i)  # 0, 1, 2

for i in range(1, 4):
    print(i)  # 1, 2, 3

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

---

## For‑Else (run else if no break)

```python
numbers = [1, 3, 5]
target = 4

for n in numbers:
    if n == target:
        print("Found!")
        break
else:
    print("Not found")  # runs only if loop never broke
```

---

## While Loops (repeat while condition is True)

```python
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```

Common pattern: menu loops with a break.

```python
while True:
    choice = input("Enter q to quit: ").strip().lower()
    if choice == "q":
        break
```

---

## Break and Continue (control a loop)

```python
for n in range(10):
    if n == 5:
        break      # stop loop entirely
    if n % 2 == 0:
        continue   # skip even numbers
    print(n)
```

---

## Mini Reference

- Comparisons: `== != < <= > >=`
- Logical: `and or not`
- Ranges: `range(stop)`, `range(start, stop, step)`
- Loop helpers: `break`, `continue`, `for‑else`
- Ternary: `a if condition else b`

---

## Try These (warm‑ups)

1. Ask for a number and print "even" or "odd" using a ternary.

2. Loop from 1..10 and print numbers divisible by 3 but not 5.

3. Build a 3×3 multiplication grid using nested `for` loops.

These are small on purpose—solve them quickly to warm up before the drills.
