# DATA STRUCTURES - MASTERING COLLECTIONS

# collection = single "variable" used to store multiple values

# List = \[] ordered and changeable. Duplicates OK

# Set = {} unordered and mutable (but no duplicates)

# Tuple = () ordered and unchangeable. Duplicates OK, faster

# Dict = {key: value} unordered mapping, keys must be unique and immutable

```bash
# List example
fruits = ["apple", "banana", "cherry"]

# Set example
unique_numbers = {1, 2, 3}

# Tuple example
coordinates = (10, 20)

# Dict example
person = {"name": "Ada", "age": 35}
```

---

## Lists (mutable, ordered)

- Create: `letters = ["a", "b", "c"]`
- Length: `len(letters)`
- Indexing/Slicing: `letters[0]`, `letters[-1]`, `letters[1:3]`, `letters[:2]`, `letters[::2]`
- Add/Remove: `append(x)`, `insert(i, x)`, `pop(i)`, `remove(x)`, `clear()`
- Search: `x in letters`, `letters.index(x)` (raises `ValueError` if not found)
- Copy vs reference: `list(a)` / `a.copy()` vs `b = a`
- Sort: `letters.sort()` in-place; `sorted(letters, key=..., reverse=True)` returns new list

### Examples

```bash
letters = ["a", "b", "c"]
letters.append("d")   # -> ["a", "b", "c", "d"]
letters[1] = "B"      # -> ["a", "B", "c", "d"]
print(len(letters))   # -> 4
```

### enumerate

Use when you need index + value in loops.

```bash
for idx, name in enumerate(["Ana", "Ben", "Cleo"], start=0):
    print(idx, name)
```

---

## Unpacking

```bash
x, y, z = [3, 7, 9]           # x=3, y=7, z=9
a, *middle, b = [1, 2, 3, 4]  # a=1, middle=[2,3], b=4
```

Unpacking is powerful when splitting collections into parts.

---

## map, filter, comprehensions

- `map(func, iterable)` transforms each item
- `filter(func, iterable)` keeps items where func(item) is True
- **List comprehension formula:** `[expression for item in iterable if condition]`
- **Dict comprehension formula:** `{key: value for item in iterable if condition}`
- **Set comprehension formula:** `{expression for item in iterable if condition}`

Examples:

```bash
prices_eur = [10, 20, 30]
prices_usd = list(map(lambda p: p * 1.1, prices_eur))

nums = range(1, 11)
evens = [n for n in nums if n % 2 == 0]  # -> [2, 4, 6, 8, 10]

words = ["apple", "banana"]
lengths = {w: len(w) for w in words}     # dict comprehension
unique_lengths = {len(w) for w in words} # set comprehension
```

---

## zip

Combine corresponding items from multiple iterables.

```bash
ids = [1, 2, 3]
names = ["A", "B", "C"]
pairs = list(zip(ids, names))  # -> [(1, "A"), (2, "B"), (3, "C")]
```

---

## Stacks and Queues

- **Stack (LIFO)**: use a list → `append()` to push, `pop()` to pop, `stack[-1]` to peek
- **Queue (FIFO)**: use `collections.deque` → `append()` to enqueue, `popleft()` to dequeue

```bash
# Stack
tasks = []
tasks.append("task1")
tasks.append("task2")
tasks.pop()   # -> "task2"

# Queue
from collections import deque
queue = deque(["a", "b"])
queue.append("c")
first = queue.popleft()   # -> "a"
```

---

## Tuples (immutable, ordered)

```bash
color = (255, 160, 64)
r, g, b = color
# color[0] = 128  # ❌ TypeError (tuples cannot be modified)
```

Tuples are used for:

- Fixed records (like coordinates)
- Dictionary keys (must be immutable)
- Safe multi-value returns from functions

---

## Arrays (typed, memory-efficient)

```bash
from array import array
ints = array('i', [1, 2, 3])
ints.append(4)
# ints.append(2.5)  # ❌ TypeError (only ints allowed)
```

Prefer lists unless you need millions of numeric values and tighter memory.

---

## Sets (unique, unordered)

- Create: `unique = {1, 2, 3}` or `set(iterable)`
- Add/Remove: `add(x)`, `discard(x)` (safe), `remove(x)` (errors if missing)
- Membership: `x in unique`
- Operations: union `a | b`, intersection `a & b`, difference `a - b`

```bash
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # -> {1, 2, 3, 4, 5}
print(A & B)  # -> {3}
print(A - B)  # -> {1, 2}
```

---

## Dictionaries (key → value mapping)

- Create: `d = {"key": "value"}` or `dict(key=value)`
- Access: `d[key]` (errors if missing), `d.get(key, default)` (safe)
- Add/Update: `d[key] = value`
- Remove: `del d[key]`, `d.pop(key)`, `d.clear()`
- Keys/Values: `d.keys()`, `d.values()`, `d.items()`
- Membership: `"key" in d`
- Copy: `d.copy()` vs aliasing with `=`
- Merge: `{**d1, **d2}` or `d1.update(d2)`

```bash
person = {"name": "Ada", "age": 35}
print(person["name"])          # -> "Ada"
print(person.get("city", "?")) # -> "?" (safe)

person["city"] = "London"       # add new key
person["age"] = 36              # update existing

for k, v in person.items():
    print(k, v)

copy = person.copy()
del person["city"]
```

### Dict Comprehensions

```bash
words = ["apple", "banana", "pear"]
lengths = {w: len(w) for w in words}
# -> {"apple": 5, "banana": 6, "pear": 4}
```

---

## Generator Expressions

Lazy sequences computed on demand (saves memory).

- **Formula:** `(expression for item in iterable if condition)`

```bash
total = sum(n * n for n in range(1, 11))
```

Generators don’t store all results at once—they compute values one by one when needed.

---

## Unpacking Operator `*` / `**`

- Lists: `[*a, *b]` merges
- Dicts: `{**d1, **d2}` merges (later keys overwrite earlier ones)

```bash
a = [1, 2]
b = [3, 4]
print([*a, *b])   # -> [1, 2, 3, 4]

d1 = {"x": 1}
d2 = {"y": 2}
print({**d1, **d2})   # -> {"x": 1, "y": 2}
```

---

# KEY CONCEPTS SUMMARY

## Lists

- Ordered, mutable, duplicates allowed
- Access by index, slice for sublists
- Methods: `append`, `extend`, `insert`, `remove`, `pop`, `clear`
- Sort in-place with `.sort()`; get a new list with `sorted()`
- Copy safely with `.copy()` or slicing; avoid aliasing
- Use `enumerate` for index + value loops

## Tuples

- Ordered, immutable, duplicates allowed
- Common for fixed records and function returns

## Sets

- Unordered, mutable, unique elements only
- Fast membership tests
- Operations: union (`|`), intersection (`&`), difference (`-`)

## Dictionaries

- Unordered key → value mapping, keys must be unique and immutable
- Access safely with `.get()`
- Add/update with `d[key] = value`
- Remove with `del`, `pop`, `clear`
- Iterate with `.items()` for key and value
- Copy with `.copy()`; merge with `.update()` or `{**d1, **d2}`
- Dict comprehensions: `{key: value for item in iterable}`

## Comprehensions & Generators

- List comprehension: `[expr for item in iterable if cond]`
- Dict comprehension: `{k: v for item in iterable if cond}`
- Set comprehension: `{expr for item in iterable if cond}`
- Generator expression: `(expr for item in iterable if cond)` (lazy evaluation)

## Stacks & Queues

- Stack (LIFO) with list: `append`, `pop`
- Queue (FIFO) with deque: `append`, `popleft`

## Best Practices

- Choose the right structure: list (order), set (uniqueness), dict (mapping), tuple (fixed)
- Use comprehensions for concise transformations
- Prefer generator expressions for large/lazy sequences
- Avoid modifying collections while iterating
- Use unpacking (`*`, `**`) to merge lists and dicts cleanly
