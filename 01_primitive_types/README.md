# 01 · Primitive Types

Short, focused **micro‑drills** to burn variables, strings and numbers into muscle‑memory, followed by a small checkpoint mini‑project.

> Solve each drill from scratch; peek only if you’re stuck for 5 min. Re‑type solutions—don’t copy‑paste.

---

## 1 · Micro‑drills (≈ 20–30 min total)

| #   | Prompt                                                                                                       | Target concept                          | Done |
| --- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------- | ---- |
| 1   | Create three variables `city`, `country`, `population`; print: **`Paris, France has 2.15 million people.`**  | variables · f‑strings · type conversion | ☐    |
| 2   | Given `quote = "Talk is cheap. Show me the code."`, print its **length** and the **last word in uppercase**. | `len()` · slicing · `str.upper()`       | ☐    |
| 3   | Ask for the user’s **birth year**, calculate their **age in months**.                                        | `input()` → `int()` · arithmetic        | ☐    |
| 4   | Clean `password = " P@ssw0rd!   "`: strip spaces, replace `@` → `a`, count characters.                       | `strip` · `replace` · `len`             | ☐    |
| 5   | For `pi = 3.14159`, print it **rounded to 2 decimals** _and_ as an **integer**.                              | `round()` · `int()`                     | ☐    |
| 6   | Make a `sentence` that spans **three lines** using `\n` escapes; then print it.                              | escape sequences                        | ☐    |
| 7   | Swap two numbers **without a temp variable**.                                                                | multiple assignment                     | ☐    |
| 8   | Prompt for a **file path**; print only the **file extension** (e.g. `.png`).                                 | slicing · `str.rfind()`                 | ☐    |
| 9   | Compute **compound interest** on €100 at 4 % for 5 years (no loop).                                          | `**` exponent operator                  | ☐    |
| 10  | Check if an email contains both **`@`** and **`.`**; print **Valid / Invalid** in one boolean expression.    | boolean operators                       | ☐    |

Tick the **Done** column as you complete each drill.

---

## 2 · Checkpoint mini‑project — _Unit & Currency Converter CLI_

**Goal:** practise variables, arithmetic, formatted strings and type‑conversion in one cohesive script.

### Features

1. Text **menu** with these conversions:

   - km ↔ miles
   - °C ↔ °F
   - EUR ↔ USD (hard‑code a rate)
   - kg ↔ lb

2. Ask for the user’s choice (`1–4`) and the value to convert.
3. Calculate and print the result using an f‑string, rounded to 2 decimals.
4. Loop until the user types `q` to quit.
5. On exit, show a tiny **dashboard**: total conversions + average response time (`time.time()`).

#### Stretch goals

- Colour menu items with ANSI codes (e.g. green on success).
- Log each conversion to a CSV file.
- Allow overriding EUR↔USD rate via flag `--rate 1.09`.

---

## 3 · Practice routine

1. **Blitz the drills** – keep each under 5 min.
2. **Commit often** – one drill = one commit.
3. **Spaced repetition** – next day, re‑solve 3 drills from memory.
4. **Only move on** when you can write the converter in ≤ 20 min and ace 6+ drills without notes.

Happy practising — fingers on keyboard! 🏋️‍♂️
