# 06 · Classes & OOP

Master Python’s object model through focused **micro‑drills** that build real intuition for instances, methods, attributes, inheritance, and the data model. Each drill targets a specific concept with zero forward‑refs beyond this section.

> **Learning Rule:** Build only on primitives, control flow, functions, data structures, and _this_ OOP section. Keep examples small, PEP 8 clean, and separate **logic** from **I/O**.

---

## 🎯 **Course Concepts Covered**

**Core OOP:** objects & classes → constructors `__init__` → instance vs class attributes → instance/class/static methods → `__repr__` vs `__str__` → equality `__eq__` & identity → encapsulation (`_name`, `__mangle`) → `@property`

**Inheritance & Polymorphism:** single inheritance → overriding → `super()` → multi‑level inheritance → multiple inheritance & MRO → polymorphism → duck typing

**Python Data Model:** truthiness/comparisons → arithmetic dunders → custom containers (len/iter/getitem/contains) → extending built‑ins vs composition → ABCs → dataclasses → decorator preview (methods)

---

## 1 · Micro‑drills (22)

| #   | Prompt                                                                                             | Core Concept(s)                              | Done |
| --- | -------------------------------------------------------------------------------------------------- | -------------------------------------------- | ---- |
| 1   | Prove `obj.m(x)` ≡ `Class.m(obj, x)` with a tiny `Echo.say` example.                               | Method binding · `self`                      | ☐    |
| 2   | Build `Car(model, year)` and verify stored attributes.                                             | Constructors `__init__` · per‑object state   | ☐    |
| 3   | Show class vs instance attr shadowing with `Car.wheels`.                                           | Class vs instance attributes                 | ☐    |
| 4   | Add `User.from_username()` that uses a class attribute `domain`.                                   | `@classmethod` · alternate constructors      | ☐    |
| 5   | Put a `clamp(x, low, high)` under a class as a static utility.                                     | `@staticmethod` · namespacing                | ☐    |
| 6   | Implement both `__repr__` and `__str__` for `Task`.                                                | Developer vs user representations            | ☐    |
| 7   | Implement `User.__eq__` comparing only `user_id` with `NotImplemented` for other types.            | Equality semantics · `NotImplemented`        | ☐    |
| 8   | Use `_internal` and name‑mangled `__token`; inspect actual attribute name.                         | Encapsulation conventions · name mangling    | ☐    |
| 9   | `Rect`: read‑only `area` property; `width` validates `> 0`.                                        | `@property` · validation                     | ☐    |
| 10  | `Animal.speak()` vs `Dog.speak()` override.                                                        | Single inheritance · overriding              | ☐    |
| 11  | Subclass calls `super().__init__()` to keep parent initialization.                                 | `super()` in constructors                    | ☐    |
| 12  | Multi‑level chain A→B→C using `super()`; verify MRO contains A and B.                              | MRO intuition · cooperative calls            | ☐    |
| 13  | Mixins that cooperate with `super()`; final string shows MRO order.                                | Multiple inheritance · cooperative `super()` | ☐    |
| 14  | Function `announce(obj)` that works for `Dog` and `Robot` without inheritance.                     | Duck typing · polymorphism                   | ☐    |
| 15  | `Score`: custom truthiness (`__bool__`) and `<` (`__lt__`).                                        | Data model · comparisons & truthiness        | ☐    |
| 16  | `Vector2`: implement `__add__` and a clear `__repr__`.                                             | Arithmetic dunders                           | ☐    |
| 17  | `Bag`: support `len`, `for`, `in`, and indexing via dunders.                                       | Custom containers · iteration protocol       | ☐    |
| 18  | Compare `LimitedList(list)` vs `LimitedBag` (composition) for a capacity limit.                    | Extending built‑ins vs composition           | ☐    |
| 19  | Define ABC `Serializer` with `dumps()` and implement `JsonSerializer`.                             | Abstract Base Classes (ABCs)                 | ☐    |
| 20  | Use `@dataclass` to auto‑generate `__init__`, `__repr__`, and `__eq__` for `Point`.                | Dataclasses                                  | ☐    |
| 21  | Decorator preview: count method calls on `Greeter.hello()`.                                        | Decorators (method wrapper preview)          | ☐    |
| 22  | Integration: `Todo` model using constructor, `repr/str`, equality, `classmethod`, and `@property`. | Putting it all together                      | ☐    |

> All drills are provided in `drills_template.py` with clear prompts and TODO markers. Copy to `drills.py` to start fresh practice.

---

## 2 · How to Use This Section

1. Copy `drills_template.py` to `drills.py` to start fresh practice.
2. Open `notes_6.md` alongside your `drills.py` for reference.
3. Complete each drill by typing the solution yourself to build muscle memory.
4. Run `python drills.py` to test your implementations.
4. Commit progress:

   - `feat(06_classes): complete drill 07 - equality semantics`
   - Update **PROGRESS.md** accordingly.

**Discipline:**

- Keep examples **pure** where possible (return values > prints).
- Maintain **logic vs I/O** separation once classes are involved.
- Keep tests/editor friendly: small methods, clear names, minimal side effects.

---

## 3 · Advanced Practice Challenges (Optional)

1. **Model a Task Store**

   - `Task` with equality by id, and `TaskStore` managing add/toggle/remove.
   - Use `@classmethod` for factory, `@property` for validation, and `__repr__` for debugging.

2. **Password Policy & Result**

   - `Policy(min_len, require_digit, require_symbol)` with a `validate(text)` method returning a result object.
   - Consider `@dataclass` for the result, manual class for the policy.

3. **Calculator State**

   - `CalculatorState` with accumulator + memory register; operations are pure functions, state changes via methods.
   - Add `__repr__` for clear debugging and a `reset()` convenience.

---

## 4 · Mastery Checkpoints

**Drill Mastery**

- [ ] Complete all 22 drills unaided
- [ ] Can re‑implement any drill from scratch
- [ ] Can explain method binding (`self`) and attribute lookup in simple English

**Concept Understanding**

- [ ] Distinguish identity (`is`) vs equality (`==`)
- [ ] Choose between **class** and **instance** attributes correctly
- [ ] Explain why and when to call `super()`
- [ ] Read an MRO for a small hierarchy
- [ ] Know when to use a property vs a method
- [ ] Decide between subclassing built‑ins vs composition

**Code Quality**

- [ ] Clean `__init__` with safe defaults (no mutable defaults)
- [ ] Informative `__repr__`, friendly `__str__`
- [ ] `__eq__` returns `NotImplemented` for unrelated types
- [ ] Minimal public surface; internal state is `_internal` or name‑mangled when appropriate
- [ ] Tests cover typical and edge cases for your class behavior

---

## 5 · Integration with Next Section

**Next up: 07 · Modules**
You’ll package your classes into modules, explore imports, and organize codebases. This will make your class designs reusable across mini‑projects and lay the groundwork for the portfolio webapp.

---

**Ready to think in objects and speak Python’s data model? Let’s build it. 🚀**
