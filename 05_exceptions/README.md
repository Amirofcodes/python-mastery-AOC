# 05 · Exceptions

Master Python's error handling through focused **micro‑drills** that build robust, crash-resistant programs. Each drill targets specific concepts from exception handling without introducing future topics.

> **Learning Rule**: Build only on primitive types, control flow, functions, and data structures. Learn to handle errors gracefully instead of letting programs crash.

---

## 🎯 **Course Concepts Covered**

**try/except Basics** → **Multiple Exceptions** → **else/finally** → **Raising Exceptions** → **Custom Exceptions** → **Context Managers** → **Exception Propagation**

---

## 1 · Micro‑drills (≈ 50 min total)

| #   | Prompt                                                                                                     | Core Concept(s)                             | Done |
| --- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ---- |
| 1   | Ask for a number, convert with `int()`, handle `ValueError` if invalid input. Print result or error msg.   | Basic try/except · ValueError               | ☐    |
| 2   | Create `safe_divide(a, b)` that handles `ZeroDivisionError` and returns result or error message.           | Function error handling · ZeroDivisionError | ☐    |
| 3   | Read a list of strings, convert each to `int()` with try/except. Print converted numbers and error count.  | Multiple exceptions in loops                | ☐    |
| 4   | Use try/except/else/finally to open a file, read content, and ensure it's always closed.                   | Complete exception flow · finally cleanup   | ☐    |
| 5   | Create `validate_age(age)` that raises `ValueError` if age < 0 or age > 150. Test with valid/invalid ages. | Raising custom exceptions                   | ☐    |
| 6   | Handle multiple exception types: `ValueError`, `TypeError`, `KeyError` in a single try block.              | Multiple specific exceptions                | ☐    |
| 7   | Use `with open()` to read a file safely. Compare with manual file handling using try/finally.              | Context managers · Resource management      | ☐    |

---

## 2 · Advanced Practice Challenges

### **Stretch Goals** (Optional)

1. **Input Validator**

   - Function that validates different data types (int, float, email)
   - Custom exception classes for each validation type
   - User-friendly error messages

2. **Robust Calculator**

   - Extend previous calculator with comprehensive error handling
   - Handle division by zero, invalid operations, type errors
   - Graceful recovery and continued operation

3. **File Processor**
   - Read and process multiple files safely
   - Handle missing files, permission errors, format errors
   - Log errors without stopping processing

---

## 3 · Mastery Checkpoints

### **Before Moving to Classes**

**Drill Mastery**:

- [ ] Complete all 7 drills without references
- [ ] Solve any drill in **< 4 minutes**
- [ ] Explain try/except/else/finally flow clearly
- [ ] Understand when to catch vs raise exceptions

**Concept Understanding**:

- [ ] Know difference between catching and raising exceptions
- [ ] Understand exception hierarchy (ValueError < Exception)
- [ ] Can explain when to use `finally` vs `else`
- [ ] Understand context managers and resource cleanup

**Code Quality**:

- [ ] Catch specific exceptions, not generic `Exception`
- [ ] Provide meaningful error messages to users
- [ ] Clean up resources properly (files, connections)
- [ ] Use exceptions for exceptional cases, not control flow

---

## 4 · Integration with Next Section

**Classes Preview** (Don't implement yet!):

- Your exception handling currently uses built-in exceptions
- Next section will teach how to create custom exception classes
- You'll learn to organize related exceptions in class hierarchies
- Error handling will become more sophisticated with object-oriented design

---

**Ready to make your programs bulletproof? Let's handle errors like a pro! 🛡️**
