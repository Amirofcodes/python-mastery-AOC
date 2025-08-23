# CLASSES & OOP — MASTERING OBJECTS AND THE PYTHON DATA MODEL

> **Goal:** A compact, runnable reference. Copy–paste the “formulas”, skim examples, and use the mini‑quizzes to lock it in.

---

## 0) Mental Model

- **Object** = a _bundle_ of related **attributes** (variables) and **methods** (functions). Example: `Task`, `User`, `Car`.
- **Class** = the _blueprint_ used to design the structure and behavior of its objects.
- You create **many objects** (instances) from **one class**.

```py
# object: concrete thing (phone, book, task)
# class: blueprint to create consistent objects
```

---

## 1) Creating Classes & Instances

**Formula:**

```py
class Name:
    def method(self, arg):
        ...

obj = Name()             # create instance
obj.method(value)        # sugar for Name.method(obj, value)
```

**Example:**

```py
class Task:
    def describe(self):
        return "Generic task"

t = Task()
print(t.describe())           # Generic task
print(Task.describe(t))       # Same call: explicit binding
```

**Key idea:** In an instance method, `self` is **the instance** that the method is bound to at runtime.

---

## 2) Constructors — `__init__`

**Purpose:** Initialize **per‑object** state.

**Formula:**

```py
class Name:
    def __init__(self, p1, p2=0):
        self.a = p1          # instance attribute
        self.b = p2
```

**Example:**

```py
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

c = Car("Civic", 2020)
```

**Gotcha:** Never use **mutable defaults** in `__init__`.

```py
# BAD
class Box:
    def __init__(self, items=[]):  # shared list across instances
        self.items = items

# GOOD
class SafeBox:
    def __init__(self, items=None):
        self.items = [] if items is None else list(items)
```

---

## 3) Attributes — Instance vs Class

- **Instance attribute** → lives in _that_ object’s `__dict__`.
- **Class attribute** → shared by **all** instances; lives on the class.

**Formula:**

```py
class Car:
    wheels = 4                 # class attribute (shared)

    def __init__(self, model):
        self.model = model     # instance attribute
```

**Shadowing:**

```py
Car.wheels = 4
c1 = Car("Civic")
c2 = Car("Model 3")

c1.wheels = 3          # creates *instance* attr; does NOT change Car.wheels
print(c1.wheels, c2.wheels, Car.wheels)   # 3 4 4
```

**When to use which?**

- Class attr: a fact shared by _all_ instances (e.g., `wheels = 4`).
- Instance attr: data that varies per object (`model`, `year`).

---

## 4) Methods — Instance, Class, Static

**Instance method** (most common):

```py
class Counter:
    def __init__(self):
        self.n = 0
    def inc(self):
        self.n += 1
```

**Class method** (needs the class, not a specific instance):

```py
class User:
    domain = "example.com"

    @classmethod
    def from_username(cls, name):
        return cls(f"{name}@{cls.domain}")

    def __init__(self, email):
        self.email = email
```

**Static method** (utility function namespaced under the class):

```py
class Math:
    @staticmethod
    def clamp(x, low, high):
        return low if x < low else high if x > high else x
```

**Binding rule:** `obj.m(x)` → `Class.m(obj, x)`; `Class.m(obj, x)` also works explicitly.

---

## 5) String Representations — `__repr__` vs `__str__`

- `__repr__` → **developer‑facing**, unambiguous; aim for `eval(repr(x))` ≈ `x` when reasonable.
- `__str__` → **user‑facing**, friendly display.

**Formula:**

```py
class Task:
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done
    def __repr__(self):
        return f"Task(id={self.id!r}, title={self.title!r}, done={self.done!r})"
    def __str__(self):
        status = "✔" if self.done else "✗"
        return f"[{status}] {self.title} (#{self.id})"
```

---

## 6) Equality & Identity — `==` vs `is`

- `is` → same **object** (same memory identity).
- `==` → **equal by value**; by default falls back to `is` unless you define `__eq__`.

**Minimal equality:**

```py
class User:
    def __init__(self, user_id, email):
        self.user_id = user_id
        self.email = email
    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id
```

---

## 7) Encapsulation Conventions

- `_name` → internal by convention.
- `__name` → name‑mangled to `_Class__name` to avoid accidental override in subclasses.

```py
class Sample:
    def __init__(self):
        self._internal = 1
        self.__token = "secret"      # becomes _Sample__token
```

> Python relies on **consenting adults**: privacy is by convention, not enforcement.

---

## 8) Properties — `@property`

Use a property to compute or **validate** like an attribute, without changing callers.

**Formula:**

```py
class Rect:
    def __init__(self, w, h):
        self._w = w
        self._h = h

    @property
    def area(self):
        return self._w * self._h

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be positive")
        self._w = value
```

---

## 9) Inheritance — Single, Multi‑level

**Why:** Reuse and specialize behavior (**is‑a** relationship). Prefer composition when reuse isn’t a clean is‑a.

**Formula:**

```py
class Animal:
    def speak(self):
        return "?"

class Dog(Animal):
    def speak(self):
        return "Woof"
```

**Method overriding:** Child defines same method name to specialize.

---

## 10) `super()` — Cooperative Calls

**Formula (Python 3):**

```py
class Logger:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # call next in MRO
        self.events = []
```

**Use it when:** you override `__init__` or other methods _and_ want parent (or next MRO) behavior preserved.

---

## 11) Multiple Inheritance & MRO (Method Resolution Order)

- Python resolves attributes using the **C3 linearization** order.
- `Class.mro()` shows the search path.

```py
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
print(D.mro())
```

**Rule of thumb:** Keep it simple. Use **mixins** for small capability additions; otherwise prefer composition.

---

## 12) Polymorphism & Duck Typing

- **Polymorphism:** same API, different types. You call `.speak()` on any animal.
- **Duck typing:** “if it quacks like a duck” — you care about **behavior**, not the exact type.

```py
def print_title(x):
    # Works for any object that has a .title attribute or property
    print(getattr(x, "title", "<no title>"))
```

---

## 13) Data Model: Magic Methods (Dunders)

### Comparisons & Truthiness

```py
class Score:
    def __init__(self, value):
        self.value = value
    def __bool__(self):            # truthiness in if/while
        return self.value > 0
    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value
```

### Arithmetic

```py
class Vector2:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        if not isinstance(other, Vector2):
            return NotImplemented
        return Vector2(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"
```

### Containers & Iteration

```py
class Bag:
    def __init__(self, items=None):
        self._items = [] if items is None else list(items)
    def __len__(self):
        return len(self._items)
    def __iter__(self):
        return iter(self._items)
    def __contains__(self, x):
        return x in self._items
    def __getitem__(self, i):
        return self._items[i]
```

---

## 14) Extending Built‑ins — Caution

You _can_ subclass `list`, `dict`, etc., but built‑in internals sometimes bypass your overrides. Prefer **composition** unless subclassing is a perfect fit.

```py
class LimitedList(list):
    def __init__(self, limit, *args):
        super().__init__(*args)
        self.limit = limit
    def append(self, x):
        if len(self) >= self.limit:
            raise ValueError("limit reached")
        super().append(x)
```

```py
# Composition alternative
class LimitedBag:
    def __init__(self, limit):
        self._data = []
        self.limit = limit
    def add(self, x):
        if len(self._data) >= self.limit:
            raise ValueError("limit reached")
        self._data.append(x)
```

---

## 15) Abstract Base Classes (ABCs)

Use ABCs to define **required methods** for a family of classes.

```py
from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def dumps(self, obj):
        ...

class JsonSerializer(Serializer):
    def dumps(self, obj):
        import json
        return json.dumps(obj)
```

---

## 16) Data Classes — `@dataclass`

A fast way to generate `__init__`, `__repr__`, `__eq__`, and more for data‑heavy classes.

```py
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(2, 3)
print(p)                 # Point(x=2, y=3)
```

> Use dataclasses when the class is primarily for **data** with simple invariants. If you have complex lifecycle or behavior, write it manually.

---

## 17) Decorators (Preview in Class Context)

You’ve already seen `@classmethod`, `@staticmethod`, `@property`. General decorators wrap callables to add behavior. Full treatment later; for now, recognize the pattern.

```py
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Greeter:
    @log_calls
    def hello(self, name):
        return f"Hello, {name}"
```

---

## Common Pitfalls Checklist

- ⛔ Forgetting `self` in method definitions.
- ⛔ Using mutable defaults in `__init__`.
- ⛔ Accidentally shadowing a class attribute with an instance attribute.
- ⛔ Implementing `__eq__` without handling _unrelated types_ → return `NotImplemented`.
- ⛔ Overriding `__init__` in inheritance chains without calling `super()` where required.
- ⛔ Subclassing built‑ins when composition would be simpler and safer.

---

## Mini‑Quizzes (quick checks)

**Q1.** What does `self` reference at runtime inside an instance method?

**Q2.** When should you choose a **class attribute** over an **instance attribute**?

**Q3.** Why is `items=[]` a bad default in `__init__`? What’s the safe pattern?

**Q4.** If two `User` objects with the same `id` should compare equal, what’s the _minimal_ dunder to implement?

**Q5.** What’s the difference between `__repr__` and `__str__`?

**Q6.** When overriding `__init__` in a subclass, why/when call `super().__init__()`?

**Q7.** What does `D.mro()` tell you in multiple inheritance?

---

## Pocket Formulas (Copy‑Paste)

```py
# Class + constructor
class Name:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b

# Instance vs class attribute
class C:
    shared = 1
    def __init__(self):
        self.own = 2

# repr / str
class R:
    def __repr__(self):
        return f"R(x={self.x!r})"
    def __str__(self):
        return f"R: {self.x}"

# equality
def __eq__(self, other):
    if not isinstance(other, type(self)):
        return NotImplemented
    return self.id == other.id

# property with validation
@property
def width(self):
    return self._w
@width.setter
def width(self, value):
    if value <= 0:
        raise ValueError("width must be positive")
    self._w = value

# inheritance + super
class Child(Parent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ...

# magic: add
def __add__(self, other):
    if not isinstance(other, type(self)):
        return NotImplemented
    return type(self)(self.x + other.x)
```

---

## Acceptance Checklist

- [ ] I can explain **class vs instance attributes** and show shadowing in code.
- [ ] I can trace how `obj.m(x)` binds to `Class.m(obj, x)`.
- [ ] I can write clean `__init__` with safe defaults and set per‑object state.
- [ ] I can implement `__repr__` and `__str__` and state their purpose.
- [ ] I can implement `__eq__` correctly (with `NotImplemented` when needed).
- [ ] I can use `@classmethod`, `@staticmethod`, and `@property` appropriately.
- [ ] I can create a small inheritance chain and use `super()` correctly.
- [ ] I can read an MRO and explain how attribute lookup works in MI.
- [ ] I can add at least one magic method to support arithmetic or iteration.
- [ ] I can decide when to use dataclasses vs hand‑written classes.

---

## Notes on Style

- Follow **PEP 8** (snake_case for methods/attributes, CapWords for classes).
- Keep **logic vs I/O** separated in examples where possible.
- Favor **composition** over inheritance unless a clear is‑a exists.
- Keep `__repr__` concise, informative, and unambiguous.
