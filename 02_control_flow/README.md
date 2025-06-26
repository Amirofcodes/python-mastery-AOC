# 02 · Control Flow

Micro‑drills to lock in comparison operators, conditionals and loops, followed by two bite‑size mini‑projects.

---

## 1 · Micro‑drills (aligns with the 14 lessons in the course)

| #   | Prompt                                                                                                                       | Core concept(s)                               | ✔   |
| --- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | --- |
| 1   | Ask the user’s age and print **Teen / Adult / Senior** using `if / elif / else` with chained comparison (`13 <= age <= 19`). | comparison operators · conditional statements | ☐   |
| 2   | One‑liner: `parity = "even" if num % 2 == 0 else "odd"` then print it.                                                       | ternary operator                              | ☐   |
| 3   | Safely divide two numbers; if divisor is 0, skip via `and` short‑circuit; print result or `undefined`.                       | logical operators · short‑circuit             | ☐   |
| 4   | Loop **5×** asking for a password. `break` on correct entry; `for‑else` prints "Locked out" if never correct.                | `for` loop · `for‑else`                       | ☐   |
| 5   | Print a **5 × 5 multiplication table** (each row one line) using nested `for` loops.                                         | nested loops                                  | ☐   |
| 6   | From `[7, 2, 9, 4, 0]` find the **first** value ≥ 8. Use `break`; `for‑else` prints "No match" if not found.                 | `for‑else` · comparisons                      | ☐   |
| 7   | Build a `while True` **number‑guessing game** (1‑10). Count attempts; break on success; print win/lose.                      | `while` · infinite loop pattern               | ☐   |
| 8   | Prompt for text and **count vowels** using a simple `for char in text:` loop.                                                | iterables · membership                        | ☐   |
| 9   | `a = 3`, `b = 8` — swap them **only if** `b` is larger.                                                                      | conditional · multiple assignment             | ☐   |
| 10  | Print the first **10 terms** of a Collatz sequence for a user number.                                                        | `while` · conditional logic                   | ☐   |
| 11  | `temp = float(input())`; print "Comfy" if `20 <= temp <= 26` else "Too hot / Too cold".                                      | chained comparison · ternary                  | ☐   |
| 12  | Loop `1..100` and print numbers divisible by **3 or 5 but not both** (XOR logic).                                            | logical operators · modulus                   | ☐   |
| 13  | Use `range(10, ‑1, ‑1)` to create a **countdown**; after loop finishes, print "Blast off!" via `else`.                       | `for`‑`else` · reverse range                  | ☐   |
| 14  | Display the first **8 Fibonacci numbers** with a `for` loop and running sum.                                                 | loop · accumulators                           | ☐   |

(Cross off ✔ when done.)

---

## 2 · Mini‑projects

### A. Guess‑the‑Number 2.0 _(easy)_

CLI where the computer picks a secret int 1‑10; player guesses until correct.

- `while True` + `break` for replay.
- Count attempts; adapt the success message.
- **Stretch**: limit to 6 attempts → `while‑else` prints "Game over".

### B. Mini‑ATM CLI _(easy‑medium)_

Simple menu: Deposit • Withdraw • Exit. Balance updates live.

- Outer `while True`; inner logic per choice.
- Reject withdrawal > balance.
- **Stretch**: PIN protection (3 tries) using `for‑else`.

---

## 3 · Practice routine

1. Drills ≈ 5 min each → commit individually.
2. Next day, redo 4 drills from memory.
3. Finish **at least one** mini‑project before moving to Functions.

Ready? `python 02_control_flow/drills.py` — GO 🚦
