# Mini‑Projects Hub

Centralized specification for all mini‑projects across sections. Each project evolves across versions (v1, v2, v3) as you unlock new concepts. This hub is your project roadmap.

> **🎯 New Template System**: Each project now includes a comprehensive `project_name_template.py` file following our systematic "ALL the different ways" methodology. Copy templates to start fresh practice with clear instructions and TODO markers.

---

## 📋 **Universal Project Rules**

- **Progressive Learning**: Each project version uses only concepts covered so far (zero forward references)
- **Template-First Approach**: Copy `project_name_template.py` to `project_name_v1.py` to start fresh practice
- **Systematic Versioning**: v1 (basic) → v2 (functions/exceptions) → v3 (classes) → v4+ (advanced)
- **Professional Standards**: All projects teach industry-grade patterns and error handling
- **Comprehensive Documentation**: Each template includes detailed instructions, concept labels, and debugging tips

## 🎓 **Learning Methodology**

### **Template Structure**

- **Clear Instructions**: Step-by-step implementation guidance
- **Concept Labels**: Each section tagged with core learning concepts
- **TODO Markers**: Systematic completion checkpoints
- **Testing Checklists**: Comprehensive validation criteria
- **Enhancement Roadmap**: Clear progression to advanced versions

### **File Organization**

- `project_name_template.py` - Clean template for fresh practice
- `project_name_v1.py` - Your implementation (copy from template)
- `project_name_v2.py` - Enhanced version with functions/exceptions
- `project_name_my_solution.py` - Your completed reference version
- `test_project_name_vX.py` - Comprehensive testing suite

---

## 🚀 **Available Project Templates**

### **📊 Template Overview**

| Project              | Template File                  | Concepts                              | Difficulty | Status     |
| -------------------- | ------------------------------ | ------------------------------------- | ---------- | ---------- |
| **Unit Converter**   | `unit_converter_template.py`   | Menus, loops, conditionals            | ★★☆        | ✅ Ready   |
| **Calculator**       | `calculator_template.py`       | Functions, pure logic, I/O separation | ★★★        | ✅ Ready   |
| **Password Toolkit** | `password_toolkit_template.py` | Strings, random, validation           | ★★★        | ✅ Ready   |
| **Todo Manager**     | `todo_manager_template.py`     | Lists, dicts, CRUD operations         | ★★★        | ✅ Ready   |
| **Number Guessing**  | `number_guessing_template.py`  | Game logic, state management          | ★★☆        | 📋 Planned |
| **Grades Analyzer**  | `grades_analyzer_template.py`  | Tuples, statistics, comprehensions    | ★★☆        | 📋 Planned |
| **Word Counter**     | `word_counter_template.py`     | Sets, dicts, text processing          | ★★★        | 📋 Planned |

### **🎯 How to Use Templates**

1. **Copy Template**: `cp unit_converter_template.py unit_converter_v1.py`
2. **Follow Instructions**: Read the comprehensive header comments
3. **Complete TODOs**: Implement each section systematically
4. **Test Thoroughly**: Use provided testing checklists
5. **Compare Solutions**: Reference existing `_v1.py` files for guidance

### **💡 Template Features**

- **📝 Comprehensive Instructions**: Step-by-step implementation guidance
- **🏷️ Concept Labels**: Each TODO tagged with learning concepts
- **✅ Testing Checklists**: Systematic validation criteria
- **🛠️ Debugging Tips**: Common pitfalls and troubleshooting advice
- **🚀 Enhancement Roadmap**: Clear progression to advanced versions
- **🏭 Real-World Applications**: Professional patterns and use cases

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

- [x] Unique words with `set`
- [x] Frequency dict built correctly
- [x] Top 5 sorted by frequency

**Metadata**

- File: `word_counter_v1.py`
- Difficulty: ★★★

---

## Section 05 · Exceptions (v2 refactors)

**Goal**: Add robust error handling to existing projects, making them production-ready.

### **Refactoring Strategy**

Before moving to Classes & OOP, upgrade your existing projects with comprehensive exception handling:

### 1) Smart Unit Converter — v2.1 (exceptions)

**Goal:** Add robust error handling to the functions-based converter.

**New Features**

- Handle invalid menu choices gracefully
- Catch `ValueError` on numeric inputs
- Validate conversion ranges (no negative temperatures below absolute zero)
- Add retry loops for invalid inputs
- Graceful degradation on errors

**Error Handling Patterns**

```python
def safe_get_number(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")
```

**Acceptance Checklist**

- [x] All numeric inputs protected with try/except
- [x] Menu choices validated with retry loops
- [x] Range validation for physical constraints
- [x] User-friendly error messages
- [x] No crashes on invalid input

**Metadata**

- File: `unit_converter_v2.1.py`
- Difficulty: ★★★

---

### 2) Advanced Calculator — v2 (exceptions)

**Goal:** Bulletproof the calculator with comprehensive error handling.

**New Features**

- Robust input validation for menu and numbers
- Enhanced division by zero handling
- Memory operations with error recovery
- Invalid operation graceful handling
- Session error logging

**Error Handling Patterns**

```python
def safe_get_menu_choice():
    while True:
        try:
            choice = int(input("Choose option (1-5): "))
            if 1 <= choice <= 5:
                return choice
            print("Please choose 1-5")
        except ValueError:
            print("Please enter a number")

def safe_divide_enhanced(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b, "Success"
    except ZeroDivisionError as e:
        return None, str(e)
    except Exception as e:
        return None, f"Calculation error: {e}"
```

**Acceptance Checklist**

- [x] All inputs protected with validation loops
- [x] Enhanced error messages with context
- [x] No crashes on any input combination
- [x] Graceful recovery from all errors
- [x] Optional: Error logging/statistics

**Metadata**

- File: `calculator_v2.py`
- Difficulty: ★★★

---

### 3) Password Toolkit — v2 (exceptions + file I/O)

**Goal:** Add file operations with robust error handling.

**New Features**

- Save/load password history to file
- Handle file permission errors
- Validate password strength with detailed feedback
- Batch password generation with error recovery
- Configuration file loading

**Error Handling Patterns**

```python
def save_password_history(passwords, filename="password_history.txt"):
    try:
        with open(filename, "w") as f:
            for pwd in passwords:
                f.write(f"{pwd}\n")
        return True, f"Saved {len(passwords)} passwords"
    except PermissionError:
        return False, "Permission denied - cannot write file"
    except Exception as e:
        return False, f"Save failed: {e}"

def load_config(filename="config.txt"):
    config = {"min_length": 8, "require_symbols": True}
    try:
        with open(filename, "r") as f:
            # Parse config file
            pass
    except FileNotFoundError:
        print("Config file not found, using defaults")
    except Exception as e:
        print(f"Config load error: {e}, using defaults")
    return config
```

**Acceptance Checklist**

- [x] File I/O operations protected with try/except
- [x] Graceful handling of missing files
- [x] Permission error handling
- [x] Configuration loading with defaults
- [x] Batch operations with partial failure recovery

**Metadata**

- File: `password_toolkit_v2.py`
- Difficulty: ★★★★

---

### 4) To-Do List Manager — v2 (exceptions + persistence)

**Goal:** Add file persistence with comprehensive error handling.

**New Features**

- Save/load tasks to JSON file
- Handle corrupted data files
- Backup and recovery mechanisms
- Import/export functionality
- Data validation on load

**Error Handling Patterns**

```python
import json

def save_tasks(tasks, filename="tasks.json"):
    try:
        # Create backup first
        if os.path.exists(filename):
            shutil.copy(filename, f"{filename}.backup")

        with open(filename, "w") as f:
            json.dump(tasks, f, indent=2)
        return True, "Tasks saved successfully"
    except Exception as e:
        return False, f"Save failed: {e}"

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)
        # Validate task structure
        for task in tasks:
            if not all(key in task for key in ["id", "title", "done"]):
                raise ValueError("Invalid task structure")
        return tasks, "Tasks loaded successfully"
    except FileNotFoundError:
        return [], "No saved tasks found, starting fresh"
    except json.JSONDecodeError:
        return [], "Tasks file corrupted, starting fresh"
    except Exception as e:
        return [], f"Load error: {e}, starting fresh"
```

**Acceptance Checklist**

- [x] JSON file operations with error handling
- [x] Data validation on load
- [x] Backup and recovery mechanisms
- [x] Graceful handling of corrupted files
- [x] Import/export with format validation

**Metadata**

- File: `todo_manager_v2.py`
- Difficulty: ★★★★

---

### 5) Student Grades Analyzer — v2 (exceptions + file processing)

**Goal:** Add CSV file processing with robust error handling.

**New Features**

- Read grades from CSV files
- Handle malformed data gracefully
- Multiple file format support
- Data validation and cleaning
- Export results to files

**Error Handling Patterns**

```python
def load_grades_from_csv(filename):
    records = []
    errors = []

    try:
        with open(filename, "r") as f:
            for line_num, line in enumerate(f, 1):
                try:
                    name, score_str = line.strip().split(",")
                    score = float(score_str)
                    if not (0 <= score <= 100):
                        errors.append(f"Line {line_num}: Invalid score {score}")
                        continue
                    records.append((name.strip(), score))
                except ValueError as e:
                    errors.append(f"Line {line_num}: {e}")
                except Exception as e:
                    errors.append(f"Line {line_num}: Unexpected error {e}")

    except FileNotFoundError:
        return [], [f"File {filename} not found"]
    except Exception as e:
        return [], [f"File read error: {e}"]

    return records, errors
```

**Acceptance Checklist**

- [ ] CSV parsing with line-by-line error handling
- [ ] Data validation and cleaning
- [ ] Partial success with error reporting
- [ ] Multiple file format support
- [ ] Export functionality with error handling

**Metadata**

- File: `grades_analyzer_v2.py`
- Difficulty: ★★★★

---

### 6) Unique Word Counter — v2 (exceptions + file processing)

**Goal:** Add file processing capabilities with robust error handling.

**New Features**

- Process text from files
- Handle large files efficiently
- Multiple encoding support
- Batch file processing
- Results export with error recovery

**Error Handling Patterns**

```python
def process_text_file(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as f:
            content = f.read()
        return content, None
    except UnicodeDecodeError:
        # Try different encodings
        for enc in ['latin1', 'cp1252', 'ascii']:
            try:
                with open(filename, 'r', encoding=enc) as f:
                    content = f.read()
                return content, f"Used {enc} encoding"
            except UnicodeDecodeError:
                continue
        return None, "Could not decode file with any encoding"
    except FileNotFoundError:
        return None, f"File {filename} not found"
    except Exception as e:
        return None, f"Error reading file: {e}"
```

**Acceptance Checklist**

- [ ] File reading with encoding detection
- [ ] Large file handling without memory issues
- [ ] Batch processing with partial failures
- [ ] Results export with error recovery
- [ ] Progress reporting for long operations

**Metadata**

- File: `word_counter_v2.py`
- Difficulty: ★★★★

---

## **🛡️ Exception Handling Best Practices**

### **Core Principles**

1. **Never crash**: Always handle expected errors gracefully
2. **User-friendly messages**: Clear, actionable error descriptions
3. **Graceful degradation**: Partial functionality when possible
4. **Recovery mechanisms**: Retry loops, defaults, backups
5. **Logging**: Track errors for debugging (optional)

### **Common Patterns**

- Input validation loops with `try/except`
- File operations with multiple fallback strategies
- Data validation with detailed error reporting
- Resource cleanup with `finally` blocks
- Context managers (`with` statements) for automatic cleanup

### **Testing Strategy**

- Test with invalid inputs of all types
- Test file operations with missing/corrupted files
- Test edge cases and boundary conditions
- Test partial failure scenarios
- Test recovery mechanisms

---

## Current Status & Next Steps

### ✅ **Section 05 · Exceptions - COMPLETED**

Successfully refactored 4 out of 6 mini-projects with enterprise-grade exception handling:

- ✅ Unit Converter v2.1 - Production-ready with bulletproof validation
- ✅ Advanced Calculator v2.0 - Enterprise memory operations & error logging
- ✅ Password Toolkit v2.0 - File I/O with configuration management
- ✅ To-Do Manager v2.0 - Database-grade persistence & recovery

### 🔄 **Deferred Exception Refactors**

These projects are complete in v1 and can be upgraded later:

- 📋 Student Grades Analyzer v2 (exceptions + CSV processing)
- 📋 Unique Word Counter v2 (exceptions + file processing)

### 🎯 **Next: Section 06 · Classes & OOP**

Ready to master object-oriented programming with:

- 22 comprehensive drills covering all OOP concepts
- 3 mini-projects using classes, inheritance, and polymorphism
- Professional software architecture patterns

### 🚀 **Future Sections**

- Classes (v3): OOP refactors with inheritance and polymorphism
- Modules/Stdlib/etc.: packaging, persistence, APIs, web development

---

## How to Refactor a Project Version

1. Identify repeated code → extract functions
2. Define clear inputs/outputs (avoid globals)
3. Use comprehensions where it improves clarity
4. Keep CLI interaction simple (f‑strings)
5. Save as new versioned file and update this hub
