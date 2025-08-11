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

Core: primitive types + conditionals + loops.

- Menu + input validation using `if/elif/else`
- `while True` main loop with `break`
- Conversions: Length, Temperature, Weight, Currency, Data
- Session counter using primitive variables

File example: `Mini-Projects/unit_converter_v1.py`

### 2) Enhanced Number Guessing Game — v1

- Random 1–20, 6 attempts, higher/lower hints
- `while` loop, counters, `break`/`else`

---

## Section 03 · Functions

### 1) Smart Unit Converter — v2 (refactor to functions)

- Extract pure functions per conversion
- Utility functions: `get_number`, `display_menu`, `get_choice`, `format_result`
- No globals: pass state as parameters, return results

Target file: `Mini-Projects/unit_converter_v2.py`

### 2) Advanced Calculator CLI

- Operation functions: add/subtract/multiply/divide (safe divide)
- Input helpers and menu functions
- Optional history passed between functions

### 3) Password Generator & Validator

- Generation functions (simple/secure/memorable)
- Validation and scoring functions

---

## Section 04 · Data Structures

### 1) To‑Do List Manager (lists + dicts)

- In‑memory list of task dicts: `{id, title, done}`
- Add/list/mark‑done/delete/clear
- Use loops, membership tests, and list comprehensions

### 2) Student Grades Analyzer

- Tuples `(name, score)`
- Average, min/max, honors ≥ 90, curve scores, sort by score (lambda key)

### 3) Unique Word Counter

- Clean text, set of unique words, dict of frequencies
- Sort by frequency and show top N

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


