# 04 · Data Structures — Beginner Notes (Read Before Drills)

Collections let you store, search, and transform groups of values.

---

## Lists (ordered, changeable)

```python
letters = ["a", "b", "c"]
print(len(letters), letters[0], letters[-1])

letters.append("d")      # add to end
letters.insert(0, "-")   # add at position
letters.pop(0)           # remove by index
letters.remove("b")      # remove by value (first match)

print(letters)           # ['a', 'c', 'd']
```

Slicing and copying:

```python
nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # [20, 30, 40]
copy1 = nums[:]    # shallow copy
```

Searching and membership:

```python
values = [5, 42, 7, 42]
if 42 in values:
    print(values.index(42))  # first index
```

Sorting:

```python
scores = [75, 92, 88, 69]
asc = sorted(scores)
desc = sorted(scores, reverse=True)
```

---

## enumerate (index + value in loops)

```python
names = ["Ana", "Ben", "Cleo"]
for idx, name in enumerate(names):
    print(f"{idx}: {name}")
```

---

## Unpacking

```python
x, y, z = [3, 7, 9]
a, *mid, b = [1, 2, 3, 4]
```

---

## Transform and Filter (map, filter, comprehensions)

```python
prices_eur = [10, 20, 30]
prices_usd = list(map(lambda p: p * 1.1, prices_eur))

nums = list(range(1, 21))
evens = list(filter(lambda n: n % 2 == 0, nums))

usd2 = [p * 1.1 for p in prices_eur]
evens2 = [n for n in nums if n % 2 == 0]
```

---

## zip (pair items)

```python
ids = [1, 2, 3]
names = ["A", "B", "C"]
pairs = list(zip(ids, names))
```

---

## Stacks (list) and Queues (deque)

```python
# Stack (LIFO)
stack = []
stack.append(10)
top = stack.pop()

# Queue (FIFO)
from collections import deque
q = deque(["a", "b"]) ; q.append("c") ; first = q.popleft()
```

---

## Tuples (fixed, ordered)

```python
color = (255, 160, 64)
r, g, b = color
# color[0] = 0  # TypeError (immutable)
```

Swap with tuples:

```python
a, b = 10, 20
a, b = b, a
```

---

## Arrays (typed)

```python
from array import array
arr = array('i', [1, 2, 3])
arr.append(4)
# arr.append(2.5)  # TypeError
```

---

## Sets (unique elements)

```python
words = set("a b c a b d".split())
print("c" in words)  # True
```

---

## Dictionaries (key → value)

```python
person = {"name": "Ada", "age": 35}
person["age"] = 36
for k, v in person.items():
    print(k, v)
```

Dict comprehension:

```python
fruits = ["apple", "banana", "pear"]
lengths = {f: len(f) for f in fruits}
```

---

## Generator Expressions (lazy)

```python
total = sum(n*n for n in range(1, 11))
```

---

## Unpacking Operators `*` and `**`

```python
c = [* [1, 2], * [3, 4]]
merged = {**{"a": 1}, **{"b": 2}}
```

---

Read these once, then go do the drills. Keep outputs tiny and clear.
