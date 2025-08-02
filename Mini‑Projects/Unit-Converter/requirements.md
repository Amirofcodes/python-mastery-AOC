# **Smart Unit Converter CLI** _(35 min target)_

**Goal:** Build a comprehensive converter using primitive types + control flow concepts.

#### **Core Features**

- **Interactive Menu**: Display conversion options using strings and print
- **Input Validation**: Use conditionals to check valid menu choices (1-6)
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

- **Only use**: Variables, strings, numbers, input/output, conditionals, loops
- **No imports** except `random` for number generation
- **Input validation**: Handle invalid choices with conditionals
- **Formatted output**: Use f-strings for professional display

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
