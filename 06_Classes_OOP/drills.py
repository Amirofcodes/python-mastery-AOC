"""
06_CLASSES — DRILLS (22) — SKELETON ONLY

You asked for *guidance without answers*. This file gives you structured,
progressive drills that match `notes_6.md`, **without solutions**.

How to use:
1) Do drills in order. Each drill says exactly what to build and what to return.
2) Replace each `raise NotImplementedError` with your implementation.
3) Run `run_tests()` to get instant feedback. Unimplemented drills are marked SKIPPED.
4) Commit with: `feat(06_classes): complete drill NN - <topic>`

Rules:
- Keep PEP 8. Separate logic from I/O.
- No forward concepts beyond the drill’s scope.
- Return the requested values so tests can verify without prints.
"""

from typing import Any, Tuple

# ---------------------------------------------------------------------------
# DRILL 01 — Method Binding & `self`
# ---------------------------------------------------------------------------


def drill_01_binding() -> Tuple[str, str]:
    """Goal: Prove that `obj.m(x)` == `Class.m(obj, x)`.

    Build:
      - class `Echo` with method `say(self, msg)` -> f"<{msg}>"
      - Create an instance and call via instance and via class
    Return: `(a, b)` where both are the two call results for the same input.
    Expected: a == b == "<hi>".
    """
    raise NotImplementedError("Implement Echo and return (a, b)")


# ---------------------------------------------------------------------------
# DRILL 02 — Constructors (__init__) & per‑object state
# ---------------------------------------------------------------------------

def drill_02_init() -> Tuple[str, int]:
    """Goal: Set per-object attributes in `__init__`.

    Build: class `Car(model, year)` storing both on `self`.
    Return: `(c.model, c.year)` for `Car("Civic", 2020)`.
    Expected: ("Civic", 2020).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 03 — Class vs Instance attributes (shadowing)
# ---------------------------------------------------------------------------

def drill_03_class_vs_instance() -> Tuple[int, int, int]:
    """Goal: Show instance attribute shadowing over class attribute.

    Build: class `Car` with class attr `wheels = 4`, and instance attr `model`.
    Steps: make `c1.wheels = 3`; create another instance `c2` untouched.
    Return: `(c1.wheels, c2.wheels, Car.wheels)`.
    Expected: (3, 4, 4).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 04 — @classmethod factory
# ---------------------------------------------------------------------------

def drill_04_classmethod() -> str:
    """Goal: Use class data inside an alternate constructor.

    Build: class `User` with class attr `domain = "example.com"` and
    `__init__(self, email)`. Add `@classmethod from_username(cls, name)` that
    returns an instance with email f"{name}@{cls.domain}".
    Return: email of `User.from_username("alice")`.
    Expected: "alice@example.com".
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 05 — @staticmethod utility (namespacing)
# ---------------------------------------------------------------------------

def drill_05_staticmethod() -> Tuple[int, int, int]:
    """Goal: Put a pure function under a class namespace.

    Build: class `Math` with `@staticmethod clamp(x, low, high)`.
    Return: `(clamp(5,0,10), clamp(-2,0,10), clamp(99,0,10))`.
    Expected: (5, 0, 10).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 06 — __repr__ vs __str__
# ---------------------------------------------------------------------------

def drill_06_repr_str() -> Tuple[str, str]:
    """Goal: Implement developer vs user-facing representations.

    Build: class `Task(id, title, done=False)` with:
      - `__repr__` -> "Task(id=<id!r>, title=<title!r>, done=<done!r>)"
      - `__str__`  -> "[✔/✗] <title> (#<id>)"
    Return: `(repr(Task(1, "Write notes", True)), str(Task(1, "Write notes", True)))`.
    Expected: ("Task(id=1, title='Write notes', done=True)", "[✔] Write notes (#1)").
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 07 — Equality semantics (__eq__) + NotImplemented
# ---------------------------------------------------------------------------

def drill_07_eq() -> Tuple[bool, bool, bool]:
    """Goal: Implement value equality safely.

    Build: class `User(user_id, email)` with `__eq__` comparing only `user_id`.
    Must return `NotImplemented` for unrelated types.
    Return: `(a==b, a==c, a==5)` for users a(1), b(1), c(2).
    Expected: (True, False, False).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 08 — Encapsulation conventions (_name, __mangle)
# ---------------------------------------------------------------------------

def drill_08_encapsulation() -> Tuple[int, str, bool]:
    """Goal: Use leading underscore and name-mangling.

    Build: class `Sample` setting `self._internal = 1` and `self.__token = "abc"`.
    Return: `(s._internal, getattr(s, "_Sample__token"), hasattr(s, "__token"))`.
    Expected: (1, "abc", False).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 09 — Properties with validation
# ---------------------------------------------------------------------------

def drill_09_property() -> Tuple[int, int]:
    """Goal: Expose attribute-like API with validation.

    Build: class `Rect(w, h)` with `area` (read-only) and `width` with setter
    that rejects non-positive values.
    Steps: r=Rect(2,3); then set r.width=5; return `(r.width, r.area)`.
    Expected: (5, 15). (Raise ValueError for <= 0.)
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 10 — Inheritance basics & overriding
# ---------------------------------------------------------------------------

def drill_10_inheritance() -> Tuple[str, str]:
    """Goal: Create a base class and a specialized subclass.

    Build: `Animal.speak()->"?"`; `Dog(Animal).speak()->"Woof"`.
    Return: `(Animal().speak(), Dog().speak())`.
    Expected: ("?", "Woof").
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 11 — super() in __init__
# ---------------------------------------------------------------------------

def drill_11_super_init() -> Tuple[bool, bool]:
    """Goal: Preserve parent initialization when specializing.

    Build: Base `Logger.__init__` sets `self.events=[]`.
           Subclass `TimedLogger(Logger)` calls `super().__init__()` and sets
           `self.started=True`.
    Return: `(isinstance(tl.events, list), tl.started)`.
    Expected: (True, True).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 12 — Multi-level inheritance + MRO peek
# ---------------------------------------------------------------------------

def drill_12_multilevel_mro() -> Tuple[str, bool]:
    """Goal: Understand lookup through a chain with super().

    Build: A.f->"A"; B(A).f-> super()+"+B"; C(B).f-> super()+"+C".
    Return: `(C().f(), A in C.mro() and B in C.mro())`.
    Expected: ("A+B+C", True).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 13 — Multiple inheritance & cooperative super()
# ---------------------------------------------------------------------------

def drill_13_multiple_inheritance() -> str:
    """Goal: Make mixins cooperate using super().

    Build: Base.f->"X"; M2(Base).f-> super()+"+M2"; M1(M2).f-> super()+"+M1";
           X(M1, M2) -> use MRO (X, M1, M2, Base, ...).
    Return: X().f(). Expected: "X+M2+M1".
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 14 — Polymorphism & duck typing
# ---------------------------------------------------------------------------

def drill_14_duck_typing() -> Tuple[str, str]:
    """Goal: Accept any object that implements the needed behavior.

    Build: function `announce(obj)` that returns `obj.speak()`.
           Create classes `Dog.speak()->"Woof"` and `Robot.speak()->"Beep"`.
    Return: `(announce(Dog()), announce(Robot()))`.
    Expected: ("Woof", "Beep").
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 15 — Truthiness & ordering dunders
# ---------------------------------------------------------------------------

def drill_15_dunders_bool_lt() -> Tuple[bool, bool, bool]:
    """Goal: Define custom truthiness and `<` comparison.

    Build: `Score(value)` where `bool(Score(v))` is `v>0` and it supports `<`
           by value.
    Return: `(bool(Score(1)), bool(Score(0)), Score(1) < Score(2))`.
    Expected: (True, False, True).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 16 — Arithmetic dunder (__add__)
# ---------------------------------------------------------------------------

def drill_16_add() -> str:
    """Goal: Return a new object when adding.

    Build: `Vector2(x,y)` with `__add__` -> `Vector2(x1+x2, y1+y2)` and a
           useful `__repr__`.
    Return: `repr(Vector2(1,2) + Vector2(3,4))`.
    Expected: "Vector2(4, 6)".
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 17 — Custom container protocol
# ---------------------------------------------------------------------------

def drill_17_container() -> Tuple[int, bool, list, int]:
    """Goal: Implement len, iteration, membership, indexing.

    Build: `Bag(items=None)` that wraps a list and supports len(b), `for` loops,
           membership `in`, and indexing.
    Return: `(len(b), 2 in b, list(iter(b)), b[0])` for `b=Bag([1,2,3])`.
    Expected: (3, True, [1,2,3], 1).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 18 — Extending built-ins vs composition
# ---------------------------------------------------------------------------

def drill_18_extend_builtins() -> Tuple[bool, bool]:
    """Goal: Compare subclassing vs composition.

    Build: `LimitedList(list)` that forbids `append` when len >= limit.
           `LimitedBag` using composition with same behavior (`add`).
    Return: `(ll_blocked, lb_blocked)` booleans indicating both raised.
    Hint: catch exceptions and convert to True/False.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 19 — Abstract Base Classes (ABCs)
# ---------------------------------------------------------------------------

def drill_19_abcs() -> str:
    """Goal: Specify required methods via abstract base class.

    Build: `Serializer(ABC)` with abstract `dumps(self, obj)`; implement
           `JsonSerializer(Serializer)` using `json.dumps`.
    Return: `JsonSerializer().dumps({"a": 1})`.
    Expected: '{"a": 1}'.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 20 — Data classes (@dataclass)
# ---------------------------------------------------------------------------

def drill_20_dataclass() -> Tuple[bool, bool]:
    """Goal: Auto-generate init/repr/eq for data containers.

    Build: `@dataclass Point(x:int, y:int)`.
    Return: `(Point(1,2)==Point(1,2), "Point(" in repr(Point(0,0)))`.
    Expected: (True, True).
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 21 — Decorators (method wrapper preview)
# ---------------------------------------------------------------------------

def drill_21_decorator_preview() -> int:
    """Goal: Recognize/trace a simple decorator on methods.

    Build: decorator `count_calls(func)` that increments `self._calls` before
           the method runs. Use it on class `Greeter.hello(self, name)`.
    Return: call `hello` twice and return `g._calls`.
    Expected: 2.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# DRILL 22 — Integration: tiny Todo model
# ---------------------------------------------------------------------------

def drill_22_integration_todo() -> Tuple[int, int, bool]:
    """Goal: Combine constructor, repr/str, equality, classmethod, property.

    Build: `Todo(id, title, done=False)` with:
      - class counter `_next_id` and `@classmethod from_title(title)`
      - `__repr__`/`__str__` per notes
      - `__eq__` by id
      - property `title` (non-empty validation)
    Return: `(t1.id, t2.id, Todo(1, "X")==t1)` for t1=from_title("Read"),
            t2=from_title("Write").
    Expected: (1, 2, True).
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------
# Test runner — marks SKIPPED on NotImplementedError
# ----------------------------------------------------------------------------

def run_tests() -> None:
    drills = [
        (1, "binding", drill_01_binding, ("<hi>", "<hi>")),
        (2, "init", drill_02_init, ("Civic", 2020)),
        (3, "class_vs_instance", drill_03_class_vs_instance, (3, 4, 4)),
        (4, "classmethod", drill_04_classmethod, "alice@example.com"),
        (5, "staticmethod", drill_05_staticmethod, (5, 0, 10)),
        (6, "repr_str", drill_06_repr_str,
         ("Task(id=1, title='Write notes', done=True)", "[✔] Write notes (#1)")),
        (7, "eq", drill_07_eq, (True, False, False)),
        (8, "encapsulation", drill_08_encapsulation, (1, "abc", False)),
        (9, "property", drill_09_property, (5, 15)),
        (10, "inheritance", drill_10_inheritance, ("?", "Woof")),
        (11, "super_init", drill_11_super_init, (True, True)),
        (12, "multilevel_mro", drill_12_multilevel_mro, ("A+B+C", True)),
        (13, "multiple_inheritance", drill_13_multiple_inheritance, "X+M2+M1"),
        (14, "duck_typing", drill_14_duck_typing, ("Woof", "Beep")),
        (15, "bool_lt", drill_15_dunders_bool_lt, (True, False, True)),
        (16, "add", drill_16_add, "Vector2(4, 6)"),
        (17, "container", drill_17_container, (3, True, [1, 2, 3], 1)),
        (18, "extend_builtins", drill_18_extend_builtins, (True, True)),
        (19, "abcs", drill_19_abcs, '{"a": 1}'),
        (20, "dataclass", drill_20_dataclass, (True, True)),
        (21, "decorator_preview", drill_21_decorator_preview, 2),
        (22, "integration_todo", drill_22_integration_todo, (1, 2, True)),
    ]

    passed = 0
    for idx, name, fn, expected in drills:
        try:
            got = fn()
            assert got == expected, f"Drill {idx:02d} expected {expected!r}, got {got!r}"
            print(f"✓ Drill {idx:02d} passed: {name}")
            passed += 1
        except NotImplementedError:
            print(f"↷ Drill {idx:02d} SKIPPED: {name} (NotImplemented)")
        except AssertionError as e:
            print(f"✗ Drill {idx:02d} FAILED: {name} -> {e}")
            break
    print(f"
Summary: {passed}/22 passed. Implement the rest!")


if __name__ == "__main__":
    run_tests()
