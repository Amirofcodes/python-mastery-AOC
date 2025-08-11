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

Beginner LeetCode‑style prompt

- Problem: Build a loop‑based console tool that converts units. Show a menu, ask the user for a choice and inputs, perform the conversion, and print a nicely formatted result. Keep running until the user quits.
- Allowed concepts: variables, strings, numbers, `input()`, `print()`, `if/elif/else`, `while True`, `break`, basic arithmetic. No functions yet.

Input format

1) Repeatedly display a menu and read an integer choice 1–6
2) For a chosen conversion, read one number (float)
3) Option 6 exits

Output format

- For each conversion, print a single line like `12.5 km = 7.77 miles`
- Track and print a session counter: `Conversions performed: X`

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

Acceptance checklist

- [ ] Handles invalid menu/direction numbers (print message; continue loop)
- [ ] Uses f‑strings; prints with 2–3 decimal places
- [ ] No crashes on unexpected input types (keep to ints/floats; no try/except yet)
- [ ] No functions or collections used

Starter file: `Mini-Projects/unit_converter_v1.py`

---

### 2) Enhanced Number Guessing Game — v1

Beginner LeetCode‑style prompt

- Problem: Computer picks a random integer 1..20. Player has 6 attempts to guess. After each guess, print `Higher` or `Lower`. Win ends immediately; otherwise print `Game over`.
- Allowed concepts: `import random` for number generation, `input()`, `int()`, `while` loop, counters, `break`, `else` on loop.

Input/Output

- Input: six user guesses as integers (or fewer if guessed early)
- Output: hints after each attempt, final win/lose message with attempt count

Acceptance checklist

- [ ] Maximum 6 attempts enforced
- [ ] Prints hint after each incorrect guess
- [ ] Uses `while` loop and a counter variable
- [ ] Uses `break` on success and `while-else` to print `Game over`

---

## Section 03 · Functions

### 1) Smart Unit Converter — v2 (refactor to functions)

LeetCode‑style refactor prompt

- Goal: Refactor v1 into small, testable functions. Keep the same features and outputs.
- Allowed: user‑defined functions, default parameters, `*args` only if needed. Avoid data structures beyond simple variables; keep history/counters primitive. No classes.

Required functions (signatures suggest intent; adjust as needed)

```
def display_menu() -> int
def choose_direction(title: str, a_label: str, b_label: str) -> int
def get_number(prompt: str) -> float

def convert_km_to_miles(km: float) -> float
def convert_miles_to_km(miles: float) -> float
def convert_c_to_f(c: float) -> float
def convert_f_to_c(f: float) -> float
def convert_kg_to_lb(kg: float) -> float
def convert_lb_to_kg(lb: float) -> float
def convert_eur_to_usd(eur: float) -> float
def convert_usd_to_eur(usd: float) -> float
def convert_mb_to_gb(mb: float) -> float
def convert_gb_to_mb(gb: float) -> float

def format_result(value: float, unit_from: str, converted: float, unit_to: str) -> str
def run_converter() -> None
```

Acceptance checklist

- [ ] All conversion math lives in pure functions (no input/print inside)
- [ ] I/O handled by thin wrapper functions; main loop in `run_converter()`
- [ ] No global mutable state; session counter passed/returned if needed
- [ ] Same UX as v1; cleaner code organization

Target: `Mini-Projects/unit_converter_v2.py`

---

### 2) Advanced Calculator CLI — v1 (functions)

- Problem: Menu‑driven calculator using pure operation functions and I/O helpers.
- Allowed: functions, conditionals, loops. Avoid data structures; if you want history, use a simple counter or defer full history to DS v2.

Required pieces

```
def add(a: float, b: float) -> float
def subtract(a: float, b: float) -> float
def multiply(a: float, b: float) -> float
def divide(a: float, b: float) -> tuple[float | None, str]
def get_number(prompt: str) -> float
def get_choice() -> int
def format_equation(a: float, op: str, b: float, res: float | None) -> str
def run_calculator() -> None
```

Example output

```
1) Add  2) Subtract  3) Multiply  4) Divide  5) Quit
Choose: 1
Enter first number: 15.5
Enter second number: 7.2
Result: 15.5 + 7.2 = 22.7
```

Acceptance checklist

- [ ] Math is pure and testable
- [ ] Division handles zero via `(None, "Cannot divide by zero")`
- [ ] Clean separation between I/O and logic

---

### 3) Password Generator & Validator — v1 (functions)

Problem

- Build functions to generate and validate passwords based on criteria.
- Allowed: functions and basic control flow; avoid data structures beyond strings/ints. If lists are used (e.g., for character pools), keep to simple concatenation and random choice.

Required functions

```
def generate_simple_password(length: int = 8) -> str
def generate_secure_password(length: int = 12) -> str  # include symbols
def is_strong(password: str, min_length: int = 8) -> bool
def validate_password(password: str) -> tuple[int, list[str]]  # score, issues
```

Acceptance checklist

- [ ] Generation respects requested length
- [ ] Validation checks: length, digits, upper/lower, symbol presence
- [ ] Clear messages returned by validator

---

## Section 04 · Data Structures

### 1) To‑Do List Manager — v1 (lists + dicts)

Problem

- Build an in‑memory task manager. Each task is a dict: `{ "id": int, "title": str, "done": bool }` stored in a list.
- Menu: Add task, List tasks, Toggle done by id, Delete by id, Clear all, Quit.

Acceptance checklist

- [ ] Unique incremental ids
- [ ] Listing shows `[#] [ ] Title` or `[#] [x] Title`
- [ ] Toggle switches `done` state by id (input validated)
- [ ] Uses list comprehensions for simple projections/filters

---

### 2) Student Grades Analyzer — v1 (tuples + comprehensions)

Problem

- Given a list of `(name, score)` tuples, compute class average, min/max, honors (≥ 90), and a curved list `score+5 capped at 100`, then sort by score desc.

Acceptance checklist

- [ ] Uses `min`, `max`, and `sum/len` (or generator expressions)
- [ ] Honors built via list comprehension
- [ ] Sorting with `key=lambda t: t[1]`, `reverse=True`

---

### 3) Unique Word Counter — v1 (sets + dicts)

Problem

- Read a line of text; normalize by lowercasing and removing `.,!?` punctuation; compute unique word count and per‑word frequencies in a dict; print top 5 by frequency.

Acceptance checklist

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
