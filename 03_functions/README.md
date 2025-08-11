# 03 · Functions

Master Python's code organization through focused **micro‑drills** that build understanding of function definition, arguments, scope, and reusability. Each drill targets specific concepts from the course curriculum.

> **Learning Rule**: Build only on primitive types and control flow. No data structures (lists, dicts) or advanced concepts yet - just functions to organize your existing knowledge.

---

## 🎯 **Course Concepts Covered**

**Defining Functions** → **Arguments** → **Types of Functions** → **Keyword Arguments** → **Default Arguments** → **xargs** → **xxargs** → **Scope** → **Debugging**

---

## 1 · Micro‑drills (≈ 60 min total)

| #   | Prompt                                                                                                      | Core Concept(s)                                 | Done |
| --- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ---- |
| 1   | Define `calculate_area(length, width)` that returns area. Test with length=5, width=3.                      | Function definition · Return values             | ☐    |
| 2   | Create `create_greeting(name, greeting="Hello")` returning formatted welcome message.                       | Default parameters · String formatting          | ☐    |
| 3   | Write `get_grade(score)` returning letter grade A-F based on numeric score ranges.                          | Multiple returns · Conditionals in functions    | ☐    |
| 4   | Build `safe_divide(a, b)` returning `(result, message)` tuple, handling division by zero.                   | Input validation · Return tuples                | ☐    |
| 5   | Implement `sum_range(start, end)` using for loop to sum numbers in range (inclusive).                       | Functions with loops · Accumulator pattern      | ☐    |
| 6   | Create `get_positive_number()` that keeps asking until user enters positive number.                         | Functions with user input · While loops         | ☐    |
| 7   | Write `calculate_compound_interest(principal, rate=0.05, time=1, compound_frequency=1)` with defaults.      | Multiple default parameters · Keyword arguments | ☐    |
| 8   | Build `validate_email(email)` checking for "@", "." and minimum 5 characters.                               | String validation · Boolean returns             | ☐    |
| 9   | Create global `call_counter`, function `tracked_add(a, b)` that increments counter and returns sum + count. | Global variables · Function scope               | ☐    |
| 10  | Implement `create_multiplier(factor)` with nested function that multiplies by factor.                       | Nested functions · Closures                     | ☐    |
| 11  | Write `find_maximum(*args)` that finds largest number from variable arguments.                              | Variable arguments (\*args) · For loops         | ☐    |
| 12  | Create lambda functions for math operations and `calculate(a, b, operation)` that uses them.                | Lambda functions · Higher-order functions       | ☐    |

---

## 2 · Advanced Practice Challenges

### **Stretch Goals** (Optional)

1. **Temperature Converter Library**

   - Functions for all temperature conversions (C↔F, C↔K, F↔K)
   - Batch conversion function
   - Temperature validation (absolute zero checks)

2. **Math Utilities Module**

   - Prime number checker
   - Factorial calculator
   - GCD/LCM functions
   - Number base converter (binary, hex, octal)

3. **Text Processing Toolkit**
   - Word counter functions
   - Text statistics (avg word length, sentences)
   - Simple encryption/decryption functions

---

## 3 · Mastery Checkpoints

### **Before Moving to Data Structures**

**Drill Mastery**:

- [ ] Complete all 12 drills without references
- [ ] Solve any drill in **< 5 minutes**
- [ ] Explain function scope and closures clearly
- [ ] Understand when to use default parameters vs required parameters

**Project Mastery**:

- [ ] Build Advanced Calculator in **≤ 40 minutes**
- [ ] Build Password Toolkit in **≤ 30 minutes**
- [ ] Both projects use proper function organization
- [ ] No code duplication between functions

**Concept Understanding**:

- [ ] Know difference between parameters and arguments
- [ ] Understand local vs global scope with examples
- [ ] Can explain when to use lambda vs regular functions
- [ ] Understand \*args and \*\*kwargs usage

**Code Quality**:

- [ ] Functions have single, clear responsibilities
- [ ] Meaningful function and parameter names
- [ ] Proper error handling in functions
- [ ] Functions are testable (pure when possible)

---

## 4 · Integration with Next Section

**Data Structures Preview** (Don't implement yet!):

- Your functions currently work with individual values
- Next section will teach how to organize data in lists, dictionaries, and sets
- Your calculator and password functions will be enhanced to work with collections
- Function parameters will expand to handle complex data structures

---

**Ready to organize your code with functions? Let's build reusable logic! ⚙️**
