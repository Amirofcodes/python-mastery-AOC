# 06_classes_oop - Micro-drills for Classes, Objects, and Python's Data Model
#
# Instructions:
# 1. Copy this template to drills.py to start fresh practice
# 2. Complete each drill by typing the solution yourself to build muscle memory
# 3. Only use concepts from previous sections + Classes/OOP from notes_6.md
# 4. Focus on objects, inheritance, and Python's data model mastery
# 5. Test each drill before moving to the next
#
# Notes: See notes_6.md for detailed explanations of all concepts
#
# ===== CORE DRILLS (Required - Basic Classes) =====

# Drill 1: Method binding and self
# Prompt: Create class `Echo` with method `say(self, msg)` that returns f"<{msg}>".
# Call it both ways: `obj.say("hi")` and `Echo.say(obj, "hi")`. Both should return "<hi>".
# Core concept: Method binding · self parameter
# TODO: Demonstrate that obj.m(x) == Class.m(obj, x)

def drill_01_binding():
    pass


# Drill 2: Constructor and instance attributes
# Prompt: Create class `Car` with `__init__(self, model, year)` storing both as instance attributes.
# Create a car with model="Civic" and year=2020, return (car.model, car.year).
# Core concept: __init__ constructor · instance attributes
# TODO: Initialize per-object state

def drill_02_init():
    pass


# Drill 3: Class vs instance attributes (shadowing)
# Prompt: Create class `Car` with class attribute `wheels = 4` and instance attribute `model`.
# Set one instance's wheels to 3, create another instance. Return (c1.wheels, c2.wheels, Car.wheels).
# Core concept: Class attributes · instance shadowing · attribute lookup
# TODO: Show class vs instance attribute behavior

def drill_03_class_vs_instance():
    pass


# Drill 4: Class methods for alternate constructors
# Prompt: Create class `User` with class attr `domain = "example.com"` and `__init__(self, email)`.
# Add `@classmethod from_username(cls, name)` that returns instance with email f"{name}@{cls.domain}".
# Return the email from User.from_username("alice").
# Core concept: @classmethod · alternate constructors · class attributes
# TODO: Use class data in factory method

def drill_04_classmethod():
    pass


# Drill 5: Static methods for utility functions
# Prompt: Create class `Math` with `@staticmethod clamp(x, low, high)` returning x clamped to [low, high].
# Test with clamp(5,0,10), clamp(-2,0,10), clamp(99,0,10). Return (5, 0, 10).
# Core concept: @staticmethod · utility functions · namespacing
# TODO: Pure function under class namespace

def drill_05_staticmethod():
    pass


# Drill 6: String representations for debugging and display
# Prompt: Create class `Task(id, title, done=False)` with both `__repr__` and `__str__`.
# __repr__ -> "Task(id=1, title='Write notes', done=True)"
# __str__ -> "[✔] Write notes (#1)" (use ✔ for done, ✗ for not done)
# Core concept: __repr__ vs __str__ · developer vs user representations
# TODO: Implement both string representations

def drill_06_repr_str():
    pass


# Drill 7: Equality semantics with proper error handling
# Prompt: Create class `User(user_id, email)` with `__eq__` comparing only user_id.
# Return NotImplemented for non-User types. Test: User(1,"a")==User(1,"b") should be True.
# User(1,"a")==User(2,"b") should be False. User(1,"a")==5 should be False.
# Core concept: __eq__ method · NotImplemented · type checking
# TODO: Implement safe equality comparison

def drill_07_eq():
    pass


# Drill 8: Encapsulation with naming conventions
# Prompt: Create class `Sample` setting `self._internal = 1` and `self.__token = "abc"`.
# Return (s._internal, getattr(s, "_Sample__token"), hasattr(s, "__token")).
# Expected: (1, "abc", False) showing name mangling behavior.
# Core concept: _private convention · __name_mangling · encapsulation
# TODO: Demonstrate Python's privacy conventions

def drill_08_encapsulation():
    pass


# Drill 9: Properties with validation
# Prompt: Create class `Rect(w, h)` with read-only `area` property and `width` property with validation.
# Width setter should raise ValueError for values <= 0. Set width to 5, return (width, area).
# Core concept: @property · getters/setters · validation
# TODO: Attribute-like API with computed values and validation

def drill_09_property():
    pass


# Drill 10: Basic inheritance and method overriding
# Prompt: Create `Animal` with `speak()` returning "?". Create `Dog(Animal)` overriding speak() to return "Woof".
# Return (Animal().speak(), Dog().speak()). Expected: ("?", "Woof").
# Core concept: Inheritance · method overriding · parent-child classes
# TODO: Specialize behavior in subclass

def drill_10_inheritance():
    pass


# Drill 11: Super() in constructors
# Prompt: Create `Logger` with `__init__` setting `self.events = []`. Create `TimedLogger(Logger)`
# that calls `super().__init__()` and sets `self.started = True`. Return (isinstance(tl.events, list), tl.started).
# Core concept: super() in __init__ · preserving parent initialization
# TODO: Chain constructors properly

def drill_11_super_init():
    pass


# Drill 12: Multi-level inheritance and MRO
# Prompt: Create A.f() -> "A", B(A).f() -> super().f() + "+B", C(B).f() -> super().f() + "+C".
# Return (C().f(), A in C.mro() and B in C.mro()). Expected: ("A+B+C", True).
# Core concept: Method Resolution Order · super() chain · multi-level inheritance
# TODO: Build inheritance chain with cooperative methods

def drill_12_multilevel_mro():
    pass


# Drill 13: Multiple inheritance with cooperative super()
# Prompt: Create Base.f() -> "X", M2(Base).f() -> super().f() + "+M2", M1(M2).f() -> super().f() + "+M1".
# Create X(M1, M2) and call X().f(). Should return "X+M2+M1" following MRO.
# Core concept: Multiple inheritance · cooperative super() · MRO order
# TODO: Make mixins cooperate properly

def drill_13_multiple_inheritance():
    pass


# Drill 14: Polymorphism and duck typing
# Prompt: Create function `announce(obj)` that returns `obj.speak()`. Create unrelated classes
# `Dog` with speak() -> "Woof" and `Robot` with speak() -> "Beep". Test both.
# Return (announce(Dog()), announce(Robot())).
# Core concept: Polymorphism · duck typing · common interface
# TODO: Accept any object with required behavior

def drill_14_duck_typing():
    pass


# ===== ADVANCED DRILLS (Python Data Model) =====

# Drill 15: Custom truthiness and comparison operators
# Prompt: Create class `Score(value)` where `bool(Score(v))` is True if v > 0.
# Implement `__lt__` for Score comparison. Return (bool(Score(1)), bool(Score(0)), Score(1) < Score(2)).
# Core concept: __bool__ method · __lt__ comparison · truthiness
# TODO: Control boolean context and comparison behavior

def drill_15_dunders_bool_lt():
    pass


# Drill 16: Arithmetic operators
# Prompt: Create class `Vector2(x, y)` with `__add__` returning Vector2(x1+x2, y1+y2).
# Implement `__repr__` for clear display. Return repr(Vector2(1,2) + Vector2(3,4)).
# Expected: "Vector2(4, 6)".
# Core concept: __add__ arithmetic · operator overloading · __repr__
# TODO: Support mathematical operations

def drill_16_add():
    pass


# Drill 17: Container protocol (iteration, membership, indexing)
# Prompt: Create class `Bag(items=None)` supporting len(), iteration, membership, and indexing.
# For b=Bag([1,2,3]), return (len(b), 2 in b, list(iter(b)), b[0]).
# Expected: (3, True, [1,2,3], 1).
# Core concept: __len__ · __iter__ · __contains__ · __getitem__ · container protocol
# TODO: Make class behave like built-in collections

def drill_17_container():
    pass


# Drill 18: Extending built-ins vs composition
# Prompt: Create `LimitedList(list)` that raises ValueError when appending if len >= limit.
# Create `LimitedBag` using composition with same behavior via `add` method.
# Return (ll_blocked, lb_blocked) as booleans indicating both raised errors.
# Core concept: Subclassing built-ins · composition pattern · error handling
# TODO: Compare inheritance vs composition approaches

def drill_18_extend_builtins():
    pass


# Drill 19: Abstract Base Classes
# Prompt: Create abstract `Serializer(ABC)` with abstract method `dumps(self, obj)`.
# Implement `JsonSerializer(Serializer)` using json.dumps. Return JsonSerializer().dumps({"a": 1}).
# Core concept: Abstract Base Classes · @abstractmethod · interface definition
# TODO: Define required methods via ABC

def drill_19_abcs():
    pass


# Drill 20: Data classes for automatic generation
# Prompt: Create `@dataclass Point(x: int, y: int)`. Test equality and repr.
# Return (Point(1,2) == Point(1,2), "Point(" in repr(Point(0,0))).
# Expected: (True, True).
# Core concept: @dataclass · automatic __init__/__repr__/__eq__ · type hints
# TODO: Generate boilerplate code automatically

def drill_20_dataclass():
    pass


# ===== INTEGRATION DRILLS (Putting It All Together) =====

# Drill 21: Method decorators preview
# Prompt: Create decorator `count_calls(func)` that increments `self._calls` before method runs.
# Apply to `Greeter.hello(self, name)`. Call hello twice, return g._calls.
# Expected: 2.
# Core concept: Decorators on methods · function wrapping · call counting
# TODO: Recognize method decoration pattern

def drill_21_decorator_preview():
    pass


# Drill 22: Integration - Complete Todo model
# Prompt: Create class `Todo(id, title, done=False)` with:
# - Class counter `_next_id` and `@classmethod from_title(title)`
# - `__repr__` and `__str__` per notes style
# - `__eq__` by id only
# - `title` property with non-empty validation
# Return (t1.id, t2.id, Todo(1, "X") == t1) for t1=from_title("Read"), t2=from_title("Write").
# Core concept: Integration · constructor · factory · equality · property · validation
# TODO: Combine all OOP concepts in one class

def drill_22_integration_todo():
    pass


# ===== TESTING HELPERS =====

def run_tests():
    """Simple test runner - implement drills to see them pass."""
    drills = [
        ("01_binding", drill_01_binding),
        ("02_init", drill_02_init),
        ("03_class_vs_instance", drill_03_class_vs_instance),
        ("04_classmethod", drill_04_classmethod),
        ("05_staticmethod", drill_05_staticmethod),
        ("06_repr_str", drill_06_repr_str),
        ("07_eq", drill_07_eq),
        ("08_encapsulation", drill_08_encapsulation),
        ("09_property", drill_09_property),
        ("10_inheritance", drill_10_inheritance),
        ("11_super_init", drill_11_super_init),
        ("12_multilevel_mro", drill_12_multilevel_mro),
        ("13_multiple_inheritance", drill_13_multiple_inheritance),
        ("14_duck_typing", drill_14_duck_typing),
        ("15_dunders_bool_lt", drill_15_dunders_bool_lt),
        ("16_add", drill_16_add),
        ("17_container", drill_17_container),
        ("18_extend_builtins", drill_18_extend_builtins),
        ("19_abcs", drill_19_abcs),
        ("20_dataclass", drill_20_dataclass),
        ("21_decorator_preview", drill_21_decorator_preview),
        ("22_integration_todo", drill_22_integration_todo),
    ]
    
    implemented = 0
    for name, drill_func in drills:
        try:
            drill_func()
            print(f"✓ Drill {name}: IMPLEMENTED")
            implemented += 1
        except:
            print(f"○ Drill {name}: Not implemented yet")
    
    print(f"\n{implemented}/22 drills implemented")
    if implemented == 22:
        print("🎉 All drills complete! You've mastered Python OOP!")
    else:
        print(f"Keep going! {22 - implemented} drills remaining.")


if __name__ == "__main__":
    run_tests()
