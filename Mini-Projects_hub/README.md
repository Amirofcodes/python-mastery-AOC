# Mini‑Projects Hub

Centralized specification for all mini‑projects across sections. Each project evolves across versions (v1, v2, v3) as you unlock new concepts. This hub is your project roadmap.

---

## Rules

- Build progressively: each project version uses only concepts covered so far (no forward refs).
- Versioning: v1 after Control Flow, v2 after Functions, v3 after Data Structures, etc.
- Keep projects in this folder. Name files with version suffixes, e.g., `unit_converter_v1.py`.
- Separate logic from I/O as soon as functions are available.

---

## Section 02 · Control Flow (v1 projects)

### 1) Smart Unit Converter — v1 (CLI)

**Goal:** Build a converter with menus, loops, and conditionals.

**Core Features**

- Interactive menu with 5 categories + Quit
- Direction selection for each category
- Conversion logic for Length, Temperature, Weight, Currency, Data
- Loop until Quit with session counter

**Concepts Reinforced**

- Input validation with `if/elif/else`
- Loop control with `while True`, `break`, `continue`
- Arithmetic and f‑strings

**Formulas**

```python
# Length
miles = km * 0.621371
km = miles / 0.621371

# Temperature
fahrenheit = celsius * 9/5 + 32
celsius = (fahrenheit - 32) * 5/9

# Weight
pounds = kg * 2.20462
kg = pounds / 2.20462

# Currency (example rate)
usd = eur * 1.08
eur = usd / 1.08

# Data
gb = mb / 1024
mb = gb * 1024
```

**Suggested Steps**

1. Print menu and read choice
2. Wrap in loop until Quit
3. Implement one conversion pair (km ↔ miles)
4. Add remaining categories
5. Add session counter

**Edge Cases / Pitfalls**

- Invalid menu/direction choices → must not crash
- Assume numeric inputs, but handle out‑of‑range menu numbers
- Watch precision formatting

**Acceptance Checklist**

- [x] Handles invalid menu/direction choices
- [x] Uses f‑strings with 2–3 decimals
- [x] Tracks and prints conversions this session
- [x] No functions or collections used

**Metadata**

- File: `unit_converter_v1.py`
- Difficulty: ★★☆

---

### 2) Enhanced Number Guessing Game — v1

**Goal:** Build a guessing game with attempts and hints.

**Core Features**

- Random secret number (1–20)
- Up to 6 valid guesses
- Hints: Higher/Lower
- End with success or Game Over

**Concepts Reinforced**

- `import random`
- While loop with counter
- `break` and `while‑else`

**Suggested Steps**

1. Generate secret number
2. Read one guess and print hint
3. Add loop for max 6 attempts
4. End on success with attempts used
5. Use `while‑else` for Game Over

**Edge Cases / Pitfalls**

- Out‑of‑range guesses shouldn’t count
- Don’t forget to increment attempt counter properly
- Handle repeated guesses

**Acceptance Checklist**

- [x] Max 6 valid attempts enforced
- [x] Hints printed after each wrong guess
- [x] Uses `while` with counter
- [x] `while‑else` used for Game Over

**Metadata**

- File: `number_guessing_v1.py`
- Difficulty: ★★☆

---

## Section 03 · Functions (v2 refactors & new)

### 1) Smart Unit Converter — v2 (functions)

**Goal:** Refactor v1 into small, testable functions.

**Core Features**

- Pure conversion functions (math only)
- I/O helpers for menus and numbers
- `run_converter()` orchestrates loop
- No global state

**Concepts Reinforced**

- Functions with parameters & return values
- Separation of concerns (logic vs I/O)
- Default parameters

**Suggested Steps**

1. Extract one conversion as pure function
2. Add input helpers
3. Add output formatter
4. Create `run_converter()` as main loop

**Pitfalls**

- Avoid putting `input()` or `print()` inside math functions
- Don’t mutate global variables

**Acceptance Checklist**

- [x] Conversion math in pure functions
- [x] I/O handled by helpers
- [x] No global mutable state
- [x] UX same as v1

**Metadata**

- File: `unit_converter_v2.py`
- Difficulty: ★★★

---

### 2) Advanced Calculator — v1 (functions)

**Goal:** Menu‑driven calculator with pure math functions.

**Core Features**

- Operations: add, subtract, multiply, divide
- Safe divide → return `(None, message)` on zero
- I/O helpers for menus and numbers

**Concepts Reinforced**

- Pure functions
- Tuples for multi‑value returns
- Clean I/O separation

**Acceptance Checklist**

- [x] Math functions are pure
- [x] Division handles zero safely
- [x] Clean separation between I/O and logic

**Metadata**

- File: `calculator_v1.py`
- Difficulty: ★★☆

---

### 3) Password Toolkit — v1 (functions)

**Goal:** Generate and validate passwords.

**Core Features**

- Generate simple (letters+digits) and secure (letters+digits+symbols)
- Validate password against rules (length, categories)
- CLI menu with Quit

**Concepts Reinforced**

- Functions for generation and validation
- Strings and loops
- `random.choice`

**Acceptance Checklist**

- [x] Generation respects length
- [x] Validation checks categories
- [x] CLI loop with Quit

**Metadata**

- File: `password_toolkit_v1.py`
- Difficulty: ★★★

---

## Section 04 · Data Structures (v3)

### 1) To‑Do List Manager — v1 (lists + dicts)

**Goal:** Manage tasks with lists of dicts.

**Core Features**

- Task shape: `{id, title, done}`
- Menu: add, list, toggle, delete, clear, quit
- Display: `[#] [ ] Title` or `[#] [x] Title`

⚠️ **Clarification for Beginners**: The display format means:

- `[#]` is the task id number
- `[ ]` means the task is _not done_
- `[x]` means the task is _done_
- `Title` is the text of the task

**Example**

```
[1] [ ] Buy milk
[2] [x] Finish homework
```

**Concepts Reinforced**

- Lists and dicts
- Membership tests
- List comprehensions

**Acceptance Checklist**

- [x] Unique incremental ids
- [x] Toggle works by id
- [x] List view consistent and clear

**Metadata**

- File: `todo_manager_v1.py`
- Difficulty: ★★★

---

### 2) Student Grades Analyzer — v1 (tuples + comprehensions)

**Goal:** Analyze scores from `(name, score)` tuples.

**Core Features**

- Average, min, max
- Honors list (≥ 90)
- Curved scores (+5, max 100)
- Sort by score desc

⚠️ **Clarification for Beginners**: Sorting with `key=lambda t: t[1]` means:

- Each `t` is a tuple `(name, score)`
- `t[1]` accesses the score
- Sorting uses that score instead of the name

**Concepts Reinforced**

- Tuples
- Comprehensions
- `min`, `max`, `sum`, `sorted`

**Acceptance Checklist**

- [x] Stats computed correctly
- [x] Honors via comprehension
- [x] Sorted with `key=lambda`

**Metadata**

- File: `grades_analyzer_v1.py`
- Difficulty: ★★☆

---

### 3) Unique Word Counter — v1 (sets + dicts)

**Goal:** Count unique words and frequencies.

**Core Features**

- Normalize input (lower, strip punctuation)
- Build set of unique words
- Build frequency dict
- Print unique count and top 5

⚠️ **Clarification for Beginners**: `set(words)` means:

- A set removes duplicates automatically
- So `set(["apple", "apple", "banana"])` → `{"apple", "banana"}`
- Useful when counting unique words

**Concepts Reinforced**

- Sets and dicts
- String normalization
- Sorting with `key=`

**Acceptance Checklist**

- [ ] Unique words with `set`
- [ ] Frequency dict built correctly
- [ ] Top 5 sorted by frequency

**Metadata**

- File: `word_counter_v1.py`
- Difficulty: ★★★

---

## Future Sections (placeholders)

- Exceptions (v3): try/except around inputs and conversions
- Classes (v4): OOP refactors
- Modules/Stdlib/etc.: packaging, persistence, APIs

---

## How to Refactor a Project Version

1. Identify repeated code → extract functions
2. Define clear inputs/outputs (avoid globals)
3. Use comprehensions where it improves clarity
4. Keep CLI interaction simple (f‑strings)
5. Save as new versioned file and update this hub
