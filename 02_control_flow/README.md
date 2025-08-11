# 02 · Control Flow

Master Python's decision-making and repetition constructs through targeted **micro‑drills** that build logical thinking and loop mastery. Each drill focuses on specific course concepts without introducing future topics.

> **Learning Rule**: Build on primitive types only. No functions, lists, or advanced structures yet - just variables, strings, numbers, and control flow.

---

## 🎯 **Course Concepts Covered**

**Comparison Operators** → **Conditional Statements** → **Ternary Operator** → **Logical Operators** → **Short-circuit Evaluation** → **Chaining Comparison Operators** → **For Loops** → **For..Else** → **Nested Loops** → **Iterables** → **While Loops** → **Infinite Loops**

---

## 1 · Micro‑drills (≈ 50 min total)

| #   | Prompt                                                                                                         | Core Concept(s)                                          | Done |
| --- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ---- |
| 1   | Ask user's age, print **Teen/Adult/Senior** using `if/elif/else` with chained comparison (`13 <= age <= 19`).  | Comparison operators · Conditional statements · Chaining | ☐    |
| 2   | One-liner: `parity = "even" if num % 2 == 0 else "odd"` then print it.                                         | Ternary operator                                         | ☐    |
| 3   | Safely divide two numbers; if divisor is 0, use `and` short-circuit to skip; print result or "undefined".      | Logical operators · Short-circuit evaluation             | ☐    |
| 4   | Loop **5×** asking for password. `break` on correct entry; `for-else` prints "Locked out" if never correct.    | `for` loop · `break` · `for-else`                        | ☐    |
| 5   | Print **5×5 multiplication table** (each row one line) using nested `for` loops with `range()`.                | Nested loops · `range()` function                        | ☐    |
| 6   | From numbers `7, 2, 9, 4, 0` find **first** value ≥ 8. Use `break`; `for-else` prints "No match" if not found. | `for-else` · Comparisons · `break`                       | ☐    |
| 7   | Build `while True` **number-guessing game** (1-10). Count attempts; `break` on success; print win message.     | `while` loop · Infinite loops · `break`                  | ☐    |
| 8   | Prompt for text and **count vowels** using `for char in text:` loop with membership testing.                   | Iterables · String iteration · Membership                | ☐    |
| 9   | `a = 3`, `b = 8` — swap them **only if** `b` is larger using conditional logic.                                | Conditional statements · Multiple assignment             | ☐    |
| 10  | Print first **10 terms** of Collatz sequence: if even divide by 2, if odd multiply by 3 and add 1.             | `while` loop · Conditional logic · Arithmetic            | ☐    |
| 11  | Ask for temperature, print "Comfy" if `20 <= temp <= 26`, else "Too hot" or "Too cold" using ternary.          | Chained comparison · Ternary operator                    | ☐    |
| 12  | Loop `1..100`, print numbers divisible by **3 or 5 but not both** (XOR logic) using modulus.                   | Logical operators · Modulus · XOR logic                  | ☐    |
| 13  | Use `range(10, -1, -1)` for **countdown**; after loop, print "Blast off!" via `for-else`.                      | `for-else` · Reverse range                               | ☐    |

---

## 2 · Advanced Practice Challenges

### **Stretch Goals** (Optional)

1. **Password Strength Checker**

   - Check length, has numbers, has uppercase
   - Use multiple `if` statements and logical operators
   - No string methods beyond basic membership

2. **Simple Calculator Loop**

   - Menu: Add, Subtract, Multiply, Divide, Quit
   - Handle division by zero with conditional logic
   - Continue until user chooses quit

3. **Pattern Printer**
   - Use nested loops to print number triangles
   - Example: 1, 12, 123, 1234, 12345

---

## 3 · Mastery Checkpoints

### **Before Moving to Functions**

**Drill Mastery**:

- [ ] Complete all 13 drills without references
- [ ] Solve any drill in **< 4 minutes**
- [ ] Explain `for-else` and `while-else` clearly

**Project Mastery**:

- [ ] Build Unit Converter CLI in **≤ 35 minutes**
- [ ] Build Number Guessing Game in **≤ 25 minutes**
- [ ] Both projects run without syntax errors

**Concept Understanding**:

- [ ] Know when to use `for` vs `while` loops
- [ ] Understand short-circuit evaluation with examples
- [ ] Can write chained comparisons confidently

**Code Quality**:

- [ ] Consistent indentation and naming
- [ ] Logical flow that's easy to follow
- [ ] Proper input validation patterns

---

## 4 · Integration with Next Section

**Functions Preview** (Don't implement yet!):

- Your mini-projects have repeated code patterns
- Next section will teach how to organize code into reusable functions
- The CLI and Number Game will be refactored using functions

---

**Ready to master Python's control flow? Let's build some logic! 🧠**
