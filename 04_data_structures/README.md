# 04 · Data Structures

Master Python's core collections with focused micro-drills and small projects. You'll learn how to store, search, transform, and organize data using lists, tuples, sets, and dictionaries – plus the most useful built-ins like `sorted()`, `zip()`, `map()` and `filter()`.

> Learning Rule: Build only on previous sections (primitive types, control flow, functions). Avoid classes, files, external libraries (except noted built-ins like `collections.deque` and `array`).

---

## 🎯 Course Concepts Covered

Lists → Indexing/Slicing → Unpacking → Looping → Add/Remove → Searching → Sorting → Lambda as key → Map/Filter → List Comprehensions → Zip → Stacks → Queues → Tuples → Swapping → Arrays → Sets → Dictionaries → Dict Comprehensions → Generator Expressions → Unpacking Operator

---

## 1 · Micro-drills (≈ 70–90 min total)

| # | Prompt | Core Concept(s) | Done |
| - | ------ | --------------- | ---- |
| 1 | Create a list `letters = ["a", "b", "c"]`; print length and first/last items. | Lists · `len()` · indexing | ☐ |
| 2 | Given `nums = [10, 20, 30, 40, 50]`, print second and last two items using slicing. | Indexing · slicing | ☐ |
| 3 | Unpack `point = [3, 7, 9]` into `x, y, z` and print. | List unpacking | ☐ |
| 4 | Loop through `names = ["Ana", "Ben", "Cleo"]` printing index + name using `enumerate`. | Looping lists · `enumerate` | ☐ |
| 5 | Start with `letters = ["a", "b", "c"]`; `append("d")`, `insert(0, "-")`, then `pop(0)` and `remove("b")`; print final list. | Add/Remove items | ☐ |
| 6 | Check if `42` appears in `values = [5, 42, 7, 42]`; print first index or "Not found". | Membership · `in` · search | ☐ |
| 7 | Sort `scores = [75, 92, 88, 69]` ascending then descending; print both. | Sorting · `sorted()` · `reverse` | ☐ |
| 8 | Sort a list of tuples `students = [("Ana", 3.7), ("Ben", 3.9), ("Cleo", 3.5)]` by GPA using a lambda key. | Lambda as sort key | ☐ |
| 9 | Using `map`, convert `prices_eur = [10, 20, 30]` to USD with rate `1.1`; make a list. | `map()` · transformation | ☐ |
| 10 | Using `filter`, keep only even numbers from `nums = list(range(1, 21))`. | `filter()` · predicates | ☐ |
| 11 | Rewrite 9 and 10 using list comprehensions. | List comprehensions | ☐ |
| 12 | Use `zip` to pair `ids = [1,2,3]` with `names = ["A","B","C"]` → list of tuples. | `zip()` · pairing | ☐ |
| 13 | Implement a simple stack with a list: `push`, `pop`, `peek`. Demonstrate 3 operations. | Stack (LIFO) via list | ☐ |
| 14 | Implement a simple queue using `collections.deque`: `enqueue`, `dequeue`. Show FIFO behavior. | Queue (FIFO) · `deque` | ☐ |
| 15 | Create a tuple `color = (255, 160, 64)`; unpack into `r,g,b`; show immutability by trying to modify (comment result). | Tuples · immutability | ☐ |
| 16 | Swap `a = 10`, `b = 20` using tuple unpacking; print before/after. | Swapping variables | ☐ |
| 17 | Create an integer array using `array('i', [1,2,3])`; append 4; show that inserting a float raises a `TypeError` (comment). | `array` module · typed arrays | ☐ |
| 18 | From text `"a b c a b d"`, build a `set` of unique words and show membership tests. | Sets · uniqueness | ☐ |
| 19 | Build a dictionary `person` with keys `name`, `age`; update `age`; print keys and values. | Dictionaries · update | ☐ |
| 20 | Dict comprehension: from `words = ["apple", "banana", "pear"]` build `{w: len(w)}`. | Dict comprehensions | ☐ |
| 21 | Generator expression: sum of squares `1..10` without creating a list. | Generator expressions | ☐ |
| 22 | Unpacking operator: merge `[1,2]` + `[3,4]` with `*`, and merge dicts with `**`. | Unpacking operator `*`/`**` | ☐ |
| 23 | Mini exercise: Given `transactions = [("+", 30), ("-", 10), ("+", 5)]`, compute final balance using a loop or comprehension. | Mixed practice | ☐ |

---

## 2 · Mini‑Projects (Data Handling Focus)

### A. To‑Do List Manager (Lists + Dicts) — 35 min

Goal: Manage tasks in memory using lists and dictionaries.

- Features: add task, list tasks, mark done, delete by id, clear all
- Data model: each task is a dict `{"id": int, "title": str, "done": bool}` stored in a list
- Operations use loops, membership tests, and list comprehension for filters
- No files or databases (in‑memory only)

### B. Student Grades Analyzer (Comprehensions + Map/Filter) — 30 min

Goal: Analyze a small list of `(name, score)` tuples.

- Compute class average, highest/lowest
- Build a list of honors (score ≥ 90)
- Normalize scores by +5 points but cap at 100
- Sort by score descending using a lambda key

### C. Unique Word Counter (Sets + Dicts) — 25 min

Goal: Count unique words from a user‑provided line of text.

- Convert to lowercase, split on spaces, strip punctuation like `, . ! ?`
- Use a set for unique words and a dict for frequencies
- Print the top 5 by frequency (sort with `key=`)

> Integration Note: These projects will later power endpoints in your FastAPI showcase.

---

## 3 · Mastery Checkpoints

- [ ] Can explain mutability differences between list, tuple, set, dict
- [ ] Confident with sorting using `key=` and `reverse=`
- [ ] Comfortable with list/dict comprehensions and when to use them
- [ ] Can choose the right collection for stacks vs queues
- [ ] Avoids O(n) scans when a set or dict lookup is appropriate

---

## 4 · Integration with Next Section

Next you will learn Exceptions to make your programs robust. You will add try/except blocks around data operations and validate inputs more safely.

---

Ready to shape data like a pro? Let's build powerful collections! 📊


