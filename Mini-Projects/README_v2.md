# Mini‑Projects Hub (Beginner‑Friendly Prompts)

These prompts tell you exactly what kind of program to create, which concepts to use, and what the program must do. Each project has versions (v1, v2, v3) that evolve as you learn more.

Rules

- Build only with concepts covered so far. No forward references.
- v1 after Control Flow, v2 after Functions (refactor), v3 after Data Structures (use collections/comprehensions).
- Keep code readable; separate I/O from logic as soon as functions are available.

---

## Section 02 · Control Flow (v1 projects)

### 1) Create a program that converts units (Smart Unit Converter — v1)

Create a program that:

- Shows a numbered menu of conversion categories (Length, Temperature, Weight, Currency, Data) and Quit
- Asks the user to choose a category, then the direction (e.g., km → miles or miles → km)
- Asks for a numeric value and prints the converted result with 2–3 decimals
- Repeats until the user chooses Quit

Use only: variables, numbers, strings, input/output, `if/elif/else`, `while`, and arithmetic. No functions yet.

Acceptance checklist

- [ ] Handles invalid menu choices (prints a message and continues)
- [ ] Uses f‑strings for clean output
- [ ] Shows a running counter of conversions this session

---

### 2) Create a program that plays a number guessing game (Enhanced Number Guessing — v1)

Create a program that:

- Picks a random secret number between 1 and 20
- Lets the user guess up to 6 times, showing “Higher” or “Lower” after each wrong guess
- Does not count out‑of‑range guesses (outside 1..20) against the attempt limit
- Prints attempts used on success; prints “Game over” otherwise

Use only: `import random`, integers, input/output, `while`, `break`, `continue`.

Acceptance checklist

- [ ] Max 6 attempts enforced
- [ ] Hints printed after each wrong guess
- [ ] Uses `while` loop and a counter; `while‑else` for game over message

---

## Section 03 · Functions (v2 refactors and new)

### 1) Refactor the unit converter into functions (Smart Unit Converter — v2)

Create a program that:

- Moves each conversion into a pure function (math only, no input/print)
- Adds I/O helper functions for menus, reading numbers, and formatting
- Uses a `run_converter()` function as the main loop

Use only: function definitions, return values, parameters, default parameters.

Acceptance checklist

- [ ] Conversion math lives in pure functions
- [ ] I/O handled by thin helper functions
- [ ] No global mutable state

---

### 2) Create a program that acts as an advanced calculator (Advanced Calculator — v1)

Create a program that:

- Exposes pure math functions: `add`, `subtract`, `multiply`, `divide` (safe divide returns `(None, message)` on zero)
- Uses I/O helpers to read numbers and menu choices
- Has a `run_calculator()` loop that orchestrates the flow

Use only: functions, tuples for multi‑value returns, no lists/dicts required.

Acceptance checklist

- [ ] No input/print in math functions
- [ ] Clear error messages for divide‑by‑zero
- [ ] Clean menu loop with Quit

---

### 3) Create a program that generates and validates passwords (Password Toolkit — v1)

Create a program that:

- Generates passwords: simple (letters+digits) and secure (must include lower, upper, digit, symbol)
- Validates a password against rules (min length, category presence)
- Provides a small CLI menu to generate or validate

Use only: functions, strings, loops, `random.choice` for generation.

Acceptance checklist

- [ ] Generation respects requested length
- [ ] Validation returns True/False (and/or a message)
- [ ] CLI shows a loop with Quit

---

## Section 04 · Data Structures (v3)

### 1) Create a program that manages a to‑do list in memory (To‑Do List Manager — v1)

Create a program that:

- Stores tasks in a list of dicts: `{id: int, title: str, done: bool}`
- Lets the user: add task, list tasks, toggle done by id, delete by id, clear all, quit
- Prints tasks like `[#] [ ] Title` or `[#] [x] Title`

Use: lists, dicts, loops, membership tests, simple list comprehensions for filters.

Acceptance checklist

- [ ] Unique incremental ids
- [ ] Toggle switches the `done` state by id (input validated)
- [ ] List view is tidy and consistent

---

### 2) Create a program that analyzes student grades (Student Grades Analyzer — v1)

Create a program that:

- Works with a list of `(name, score)` tuples
- Computes average, min, and max
- Produces a list of honors (score ≥ 90)
- Builds curved scores (+5 capped at 100)
- Sorts students by score descending

Use: tuples, list comprehensions, `min`/`max`/`sum`, and sorting with `key=lambda`.

---

### 3) Create a program that counts unique words (Unique Word Counter — v1)

Create a program that:

- Reads one line of text, lowers it, strips `.,!?`
- Splits into words and builds a `set` of unique words
- Builds a frequency dictionary of words
- Prints unique count and top 5 words by frequency

Use: sets, dicts, simple comprehensions, sorting by `key=`.
