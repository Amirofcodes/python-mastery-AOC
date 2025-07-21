# 01 · Primitive Types

Master Python's fundamental data types through focused **micro‑drills** that build muscle memory for variables, strings, and numbers. Each drill targets specific concepts from the course curriculum.

> **Learning Rule**: Type every solution from scratch. No copy-paste. If stuck for 5+ minutes, peek at hints, then re-implement from memory.

---

## 🎯 **Course Concepts Covered**

**Variables** → **Variable Names** → **Strings** → **Escape Sequences** → **Formatted Strings** → **String Methods** → **Numbers** → **Working with Numbers** → **Type Conversion**

---

## 1 · Micro‑drills (≈ 40 min total)

| #   | Prompt                                                                                                         | Target Concepts                                | Done |
| --- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ---- |
| 1   | Create `city`, `country`, `population` variables; print: **`Paris, France has 2.15 million people.`**          | Variables · F-strings                          | ✅   |
| 2   | Given `quote = "Talk is cheap. Show me the code."`, print its **length** and **last word in UPPERCASE**.       | String methods · Slicing · `len()` · `upper()` | ✅   |
| 3   | Ask user's **birth year**, calculate **age in months**. Handle string → int conversion.                        | `input()` · Type conversion · Arithmetic       | ✅   |
| 4   | Clean `password = " P@ssw0rd!   "`: strip spaces, replace `@` → `a`, count final characters.                   | String methods · `strip()` · `replace()`       | ✅   |
| 5   | For `pi = 3.14159`, print it **rounded to 2 decimals** and as an **integer**.                                  | Numbers · `round()` · `int()` casting          | ✅   |
| 6   | Create a sentence spanning **3 lines** using `\n`. Then print it.                                              | Escape sequences                               | ✅   |
| 7   | Swap two numbers **without a temp variable** using Python's multiple assignment.                               | Multiple assignment · Variable names           | ✅   |
| 8   | Ask for **file path**, extract and print only the **extension** (e.g., `.png`).                                | String slicing · `rfind()` method              | ✅   |
| 9   | Calculate **compound interest**: €100 at 4% for 5 years using the formula A = P(1+r)^n.                        | Working with numbers · `**` operator           | ✅   |
| 10  | Validate email: check if it contains **both** `@` and `.` using boolean operators in one expression.           | Boolean operators · String membership          | ☐    |
| 11  | Create variables using different **naming conventions**: `snake_case`, `camelCase`, test which Python prefers. | Variable names · Python conventions            | ☐    |
| 12  | Format the number `1234567.89` with **thousands separators** and **2 decimal places**.                         | Formatted strings · Number formatting          | ☐    |
| 13  | Extract **first name** and **last name** from `"John Doe"` using string methods (no splitting yet).            | String methods · `find()` · Slicing            | ☐    |
| 14  | Convert temperature: ask for **Celsius**, show **Fahrenheit** with formula F = C × 9/5 + 32.                   | Type conversion · Arithmetic · F-strings       | ☐    |
| 15  | Create a **multi-line string** using triple quotes, then count total **words** (hint: use `split()`).          | Multi-line strings · String methods            | ☐    |

---

## 2 · Enhanced Mini‑Project — _Smart Unit & Currency Converter CLI_

**Goal:** Build a comprehensive converter that demonstrates all primitive type concepts in one cohesive application.

### **Core Features** (Must implement)

1. **Interactive Menu System**

   ```
   🧮 Smart Converter v1.0
   ========================
   1. Length (km ↔ miles)
   2. Temperature (°C ↔ °F)
   3. Weight (kg ↔ lb)
   4. Currency (EUR ↔ USD)
   5. Data (MB ↔ GB)
   6. View History
   7. Quit
   ```

2. **Conversion Logic**

   - Ask for conversion type and direction
   - Handle user input with proper type conversion
   - Use f-strings for formatted output (2 decimal places)
   - Store each conversion with timestamp

3. **Data Validation**

   - Check for valid menu choices (1-7)
   - Validate numeric inputs (handle errors gracefully)
   - Ensure positive values for conversions

4. **Session Tracking**
   - Count total conversions performed
   - Calculate average conversion value
   - Show session summary on exit

### **Technical Requirements**

- **Variables**: Use descriptive names following Python conventions
- **Strings**: Menu formatting, user prompts, results display
- **Numbers**: All conversion formulas, statistics calculations
- **Type Conversion**: Handle `input()` → `int()`/`float()` safely
- **Formatted Strings**: Professional output with proper decimal places
- **String Methods**: Input cleaning (`strip()`, `lower()`)

### **Sample Conversion Formulas**

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

### **Stretch Goals** (Optional)

- **Color Output**: Use ANSI codes for green success, red errors
- **Input History**: Show last 5 conversions before each prompt
- **Rate Updates**: Allow updating currency exchange rate
- **Export Feature**: Save session history to a text file

### **Success Criteria**

- [ ] Handles all 5 conversion types correctly
- [ ] Validates user input without crashing
- [ ] Uses f-strings for all output formatting
- [ ] Implements session tracking with statistics
- [ ] Code is clean, readable, and well-commented
- [ ] Can be completed in **≤ 45 minutes**

---

## 3 · Practice Routine

### **Daily Workflow**

1. **Morning Drill Blitz** (15 min): Complete 3-4 drills rapidly
2. **Evening Review** (10 min): Re-solve 2 previous drills from memory
3. **Weekly Challenge**: Build the mini-project in one session

### **Mastery Checkpoints**

- [ ] Can solve any drill in **< 3 minutes** without notes
- [ ] Explain each concept to an imaginary student
- [ ] Complete mini-project from scratch in **45 minutes**
- [ ] Zero syntax errors on first run (clean code habits)

### **Before Moving to Control Flow**

- [ ] All 15 drills completed and committed
- [ ] Mini-project fully functional
- [ ] Updated `PROGRESS.md` with achievements
- [ ] Next-day retention test: solve 5 random drills perfectly

---

**Ready to build that muscle memory? Fire up your editor and let's code! 💪**
