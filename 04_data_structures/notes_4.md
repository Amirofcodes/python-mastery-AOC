# 04 · Data Structures – Notes

A fast refresher on Python's core collections and patterns you'll use in the drills. Read once, then code from memory.

---

## Lists (mutable, ordered)

- Create: `letters = ["a", "b", "c"]`
- Length: `len(letters)`
- Indexing/Slicing: `letters[0]`, `letters[-1]`, `letters[1:3]`, `letters[:2]`, `letters[::2]`
- Add/Remove: `append(x)`, `insert(i, x)`, `pop(i)`, `remove(x)`, `clear()`
- Search: `x in letters`, `letters.index(x)` (raises `ValueError` if not found)
- Copy vs reference: `list(a)` / `a.copy()` vs `b = a`
- Sort: `letters.sort()` in-place; `sorted(letters, key=..., reverse=True)` returns new list

### enumerate

Use when you need index + value in loops.

```
for idx, name in enumerate(["Ana", "Ben", "Cleo"], start=0):
    print(idx, name)
```

---

## Unpacking

```
x, y, z = [3, 7, 9]
a, *middle, b = [1, 2, 3, 4]
```

---

## map, filter, comprehensions

- `map(func, iterable)` transforms each item
- `filter(func, iterable)` keeps items where func(item) is True
- List comprehension: `[f(x) for x in items if cond(x)]`

Examples:

```
prices_eur = [10, 20, 30]
prices_usd = list(map(lambda p: p * 1.1, prices_eur))
evens = [n for n in range(1, 21) if n % 2 == 0]
```

---

## zip

Combine corresponding items from multiple iterables.

```
ids = [1, 2, 3]
names = ["A", "B", "C"]
pairs = list(zip(ids, names))
```

---

## Stacks and Queues

- Stack (LIFO): use a list → `append()` to push, `pop()` to pop, `stack[-1]` to peek
- Queue (FIFO): use `collections.deque` → `append()` to enqueue, `popleft()` to dequeue

```
from collections import deque
queue = deque(["a", "b"])
queue.append("c")
first = queue.popleft()
```

---

## Tuples (immutable, ordered)

```
color = (255, 160, 64)
r, g, b = color
# color[0] = 128  # TypeError
```

Tuple uses: fixed records, dictionary keys, safe multi‑value returns.

---

## Arrays (typed, memory‑efficient)

```
from array import array
ints = array('i', [1, 2, 3])
ints.append(4)
# ints.append(2.5)  # TypeError
```

Prefer lists unless you need many numeric values with tighter memory.

---

## Sets (unique, unordered)

- Create: `unique = {1, 2, 3}` or `set(iterable)`
- Add/Remove: `add(x)`, `discard(x)`, `remove(x)`
- Membership: `x in unique`
- Operations: union `a | b`, intersection `a & b`, difference `a - b`

---

## Dictionaries (key → value mapping)

```
person = {"name": "Ada", "age": 35}
person["age"] = 36
for key, value in person.items():
    print(key, value)
```

### Dict Comprehensions

```
words = ["apple", "banana", "pear"]
lengths = {w: len(w) for w in words}
```

---

## Generator Expressions

Lazy sequences computed on demand.

```
total = sum(n * n for n in range(1, 11))
```

---

## Unpacking Operator `*` / `**`

- Lists: `[*a, *b]` merges
- Dicts: `{**d1, **d2}` merges (later keys overwrite earlier ones)

---

You're ready to tackle the drills. Keep outputs small and clear, and test each step as you go.
