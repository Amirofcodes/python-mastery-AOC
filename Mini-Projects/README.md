# Mini‑Projects Hub

Centralized specification for all mini‑projects across sections. Sections' READMEs now list drills only. Use this hub to plan, build, and refactor projects as you learn new concepts.

---

## Rules

- Progressive only: each project version uses concepts up to the current section (no forward refs).
- Versioning: v1 after Control Flow, v2 after Functions (refactor into functions), v3 after Data Structures (use collections, comprehensions), etc.
- Keep projects in this folder. Name files with version suffixes, e.g., `unit_converter_v1.py`, `unit_converter_v2.py`.

---

## Section 02 · Control Flow

### 1) Smart Unit Converter — v1 (CLI)

**Goal:** Build a comprehensive converter using primitive types + control flow concepts.

#### **Core Features**

- **Interactive Menu**: Display conversion options using strings and `print`
- **Input Validation**: Use conditionals to check valid menu choices (1–6)
- **Conversion Logic**: Handle 5 conversion types with proper direction selection
- **Loop Control**: Use `while True` with `break` for program flow
- **Session Tracking**: Count conversions using primitive variables

#### **Menu Structure**

```
🧮 Smart Converter v1.0
========================
1. Length (km ↔ miles)
2. Temperature (°C ↔ °F)
3. Weight (kg ↔ lb)
4. Currency (EUR ↔ USD)
5. Data (MB ↔ GB)
6. Quit
```

#### **Technical Requirements**

- **Only use**: variables, strings, numbers, input/output, conditionals, loops
- **No functions**; no complex data structures
- **Input validation**: handle invalid choices with conditionals and continue the loop
- **Formatted output**: use f‑strings; show 2–3 decimals where appropriate

#### **Conversion Formulas**

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

Conversions and formulas

```
1. Length: km ↔ miles          miles = km * 0.621371,   km = miles / 0.621371
2. Temperature: °C ↔ °F        F = C * 9/5 + 32,        C = (F - 32) * 5/9
3. Weight: kg ↔ lb             lb = kg * 2.20462,       kg = lb / 2.20462
4. Currency: EUR ↔ USD         usd = eur * 1.08,        eur = usd / 1.08
5. Data: MB ↔ GB               gb = mb / 1024,          mb = gb * 1024
6. Quit
```

Example interaction (truncated)

```
🧮 Smart Converter v1.0
1) Length  2) Temperature  3) Weight  4) Currency  5) Data  6) Quit
Choose: 1
1) km → miles  2) miles → km
Choose: 1
Enter distance in km: 12.5
12.5 km = 7.768 miles
Conversions performed: 1
```

Suggested steps

1. Print the menu once and read a choice
2. Wrap it in a `while True` to repeat until quit
3. Implement one direction of one conversion (e.g., km → miles)
4. Add the reverse direction selection for that conversion
5. Add the remaining conversion categories
6. Add and display the session counter

Acceptance checklist

- [ ] Handles invalid menu/direction numbers (print message; continue loop)
- [ ] Uses f‑strings; prints with 2–3 decimal places
- [ ] Assume numeric inputs; reject out‑of‑range menu/direction numbers politely
- [ ] No functions or collections used

Starter file: `Mini-Projects/unit_converter_v1.py`

---

### 2) Enhanced Number Guessing Game — v1

**Goal:** Build a guessing game loop with hints and an attempts limit.

#### **Core Features**

- **Secret Number**: Pick a random integer 1–20
- **Attempts Limit**: Allow up to 6 guesses
- **Hints**: Print `Higher` or `Lower` after wrong guesses
- **Loop Control**: Use `while` with a counter and `break`; use `while‑else` for `Game over`

#### **Technical Requirements**

- **Only use**: `import random`, input/output, integers, conditionals, loops
- **Range handling**: Reject guesses outside 1–20 without consuming an attempt
- **Formatted messages**: Show attempts used on success

#### **Suggested steps**

1. Generate a secret number in 1–20 (inclusive)
2. Read one guess and print Higher/Lower/Correct
3. Add a loop to allow up to 6 attempts
4. End immediately on correct guess with attempts used
5. Use `while‑else` to print `Game over` on failure

#### **Edge cases**

- Bounds (1 and 20)
- Repeated same guess
- Out‑of‑range inputs (0 or 25)

Acceptance checklist

- [ ] Maximum 6 attempts enforced
- [ ] Prints hint after each incorrect guess
- [ ] Uses `while` loop and a counter variable
- [ ] Uses `break` on success and `while-else` to print `Game over`

---

## Section 03 · Functions

### 1) Smart Unit Converter — v2 (refactor to functions)

**Goal:** Refactor v1 into small, testable functions (same features, cleaner design).

#### **Core Features**

- **Pure Conversion Functions**: math only, no I/O
- **I/O Helpers**: menu display, reading numbers, formatting
- **Main Orchestrator**: `run_converter()` loop that calls helpers
- **No Globals**: pass and return any needed state

#### **Possible decomposition** (examples; choose your own names)

```
display_menu(), choose_direction(...), get_number(...)
convert_* functions for each unit pair
format_result(...), run_converter()
```

#### **Suggested steps**

1. Extract one conversion to a pure function and call it from the loop
2. Extract input helpers (menu, direction, number)
3. Extract output formatting
4. Ensure no global mutable state is used

#### **Acceptance checklist**

- [ ] All conversion math lives in pure functions (no input/print inside)
- [ ] I/O handled by thin wrapper functions; main loop in `run_converter()`
- [ ] No global mutable state; session counter passed/returned if needed
- [ ] Same UX as v1; cleaner code organization

Target: `Mini-Projects/unit_converter_v2.py`

---

### 2) Advanced Calculator CLI — v1 (functions)

**Goal:** Build a menu‑driven calculator with pure math functions and clean I/O.

#### **Core Features**

- **Operations**: add, subtract, multiply, divide (safe divide)
- **I/O Helpers**: input reading, menu selection, output formatting
- **Separation**: no input/print inside math functions

#### **Possible decomposition**

```
add(), subtract(), multiply(), divide()
get_number(), get_choice(), format_equation(), run_calculator()
```

#### **Example output**

```
1) Add  2) Subtract  3) Multiply  4) Divide  5) Quit
Choose: 1
Enter first number: 15.5
Enter second number: 7.2
Result: 15.5 + 7.2 = 22.7
```

#### **Acceptance checklist**

- [ ] Math is pure and testable
- [ ] Division handles zero via `(None, "Cannot divide by zero")`
- [ ] Clean separation between I/O and logic

---

### 3) Password Generator & Validator — v1 (functions)

**Goal:** Generate passwords and validate their strength using functions.

#### **Core Features**

- **Generators**: simple (letters+digits), secure (include symbols)
- **Validation**: length, digits, upper/lower, symbol presence
- **Configurable**: adjustable length and minimum requirements

#### **Possible decomposition**

```
generate_simple_password(), generate_secure_password()
is_strong(), validate_password()
```

#### **Acceptance checklist**

- [ ] Generation respects requested length
- [ ] Validation checks: length, digits, upper/lower, symbol presence
- [ ] Clear messages returned by validator

---

## Section 04 · Data Structures

### 1) To‑Do List Manager — v1 (lists + dicts)

**Goal:** Manage an in‑memory list of task dicts using list/dict operations.

#### **Core Features**

- **Task shape**: `{id, title, done}`
- **Menu**: Add, List, Toggle‑done by id, Delete by id, Clear all, Quit
- **Display**: `[#] [ ] Title` or `[#] [x] Title`

#### **Suggested steps**

1. Add and List tasks (no toggle/delete yet)
2. Implement Toggle done by id
3. Implement Delete by id
4. Implement Clear all

#### **Acceptance checklist**

- [ ] Unique incremental ids
- [ ] Listing shows `[#] [ ] Title` or `[#] [x] Title`
- [ ] Toggle switches `done` state by id (input validated)
- [ ] Uses list comprehensions for simple projections/filters

---

### 2) Student Grades Analyzer — v1 (tuples + comprehensions)

**Goal:** Analyze a list of `(name, score)` tuples and compute class stats.

#### **Core Features**

- **Stats**: average, min, max
- **Lists**: honors (≥ 90), curved scores (+5 up to 100)
- **Sorting**: by score desc

#### **Suggested steps**

1. Compute average with `sum/len`
2. Identify min and max
3. Build honors list (score ≥ 90)
4. Build curved scores with capping
5. Sort by score desc

#### **Acceptance checklist**

- [ ] Uses `min`, `max`, and `sum/len` (or generator expressions)
- [ ] Honors built via list comprehension
- [ ] Sorting with `key=lambda t: t[1]`, `reverse=True`

---

### 3) Unique Word Counter — v1 (sets + dicts)

**Goal:** Count unique words and their frequencies in a normalized input string.

#### **Core Features**

- **Normalization**: lowercase, strip `.,!?`
- **Counting**: build a frequency dict
- **Reporting**: unique count and top 5 words by frequency

#### **Suggested steps**

1. Normalize the string (lower, strip punctuation)
2. Split into words and compute `set` of unique words
3. Build frequency dict
4. Sort by frequency and print top 5

#### **Edge cases**

- Empty input string
- Multiple spaces and punctuation‑only tokens
- Ties in frequency near the cutoff

#### **Acceptance checklist**

- [ ] Uses `set(words)` for unique words
- [ ] Dict counting loop or comprehension
- [ ] Sorted top 5 by frequency with `key=`

---

## Future Sections (placeholders)

- 05 Exceptions: add try/except around inputs and conversions; produce v3 of earlier projects with robust error handling
- 06 Classes: object‑oriented refactors where appropriate
- 07+ Modules/Stdlib/etc.: package projects, add persistence/APIs as learned

---

## How to Refactor a Project Version

1. Identify repeated code → extract functions
2. Define clear inputs/outputs (avoid globals)
3. Replace loops/filters with comprehensions where it improves clarity (from section 04)
4. Keep CLI interaction simple; formatting via f‑strings
5. Save as new versioned file and update this README
