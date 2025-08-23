"""
06_CLASSES — DRILLS (22)

How to use:
1) Pick a drill in order. Read the docstring carefully.
2) Fill in the TODOs. Keep PEP 8, and separate logic from I/O.
3) Run this file or your own tests. Uncomment asserts under each drill when ready.
4) Commit with message: `feat(06_classes): complete drill NN - <topic>`

These drills follow the order in notes_6.md and escalate gradually.
"""

# ---------------------------------------------------------------------------
# DRILL 01 — Method Binding & `self`
# ---------------------------------------------------------------------------


def drill_01_binding():
    """Goal: Understand that `obj.m(x)` == `Class.m(obj, x)`.

    Write a class `Echo` with a method `say(self, msg)` that returns `f"<{msg}>"`.
    Then create one instance and prove (with code) that calling the method via
    the instance or via the class are equivalent.

    Acceptance:
      - Class Echo defined with say(self, msg) -> str
      - Two calls produce the same string
    """
    # TODO: your code here
    class Echo:
        def say(self, msg):
            return f"<{msg}>"

    e = Echo()
    a = e.say("hi")
    b = Echo.say(e, "hi")
    assert a == b == "<hi>"


# ---------------------------------------------------------------------------
# DRILL 02 — Constructors (__init__) & per‑object state
# ---------------------------------------------------------------------------

def drill_02_init():
    """Goal: Initialize instance attributes in __init__.

    Implement class `Car` with __init__(self, model, year) storing both as
    instance attributes. Create one car and assert the attributes.
    """
    # TODO: your code here
    class Car:
        def __init__(self, model, year):
            self.model = model
            self.year = year

    c = Car("Civic", 2020)
    assert (c.model, c.year) == ("Civic", 2020)


# ---------------------------------------------------------------------------
# DRILL 03 — Class vs Instance attributes (shadowing)
# ---------------------------------------------------------------------------

def drill_03_class_vs_instance():
    """Goal: Distinguish shared class data from per-instance data.

    Create class `Car` with class attribute `wheels = 4` and instance attr
    `model` from __init__. Then set `c1.wheels = 3` and verify that it does not
    affect `Car.wheels` or other instances.
    """
    # TODO: your code here
    class Car:
        wheels = 4

        def __init__(self, model):
            self.model = model

    c1 = Car("Civic")
    c2 = Car("Model 3")
    c1.wheels = 3  # instance shadowing
    assert (c1.wheels, c2.wheels, Car.wheels) == (3, 4, 4)


# ---------------------------------------------------------------------------
# DRILL 04 — @classmethod factory
# ---------------------------------------------------------------------------

def drill_04_classmethod():
    """Goal: Use class data inside an alternate constructor.

    Build class `User` with class attr `domain = "example.com"` and a normal
    __init__(self, email). Add @classmethod `from_username(cls, name)` that
    returns an instance with email f"{name}@{cls.domain}".
    """
    # TODO: your code here
    class User:
        domain = "example.com"

        def __init__(self, email):
            self.email = email

        @classmethod
        def from_username(cls, name):
            return cls(f"{name}@{cls.domain}")

    u = User.from_username("alice")
    assert u.email == "alice@example.com"


# ---------------------------------------------------------------------------
# DRILL 05 — @staticmethod utility (namespacing)
# ---------------------------------------------------------------------------

def drill_05_staticmethod():
    """Goal: Put a pure function under a class namespace.

    Create class `Math` with a @staticmethod `clamp(x, low, high)` returning
    x limited to [low, high].
    """
    # TODO: your code here
    class Math:
        @staticmethod
        def clamp(x, low, high):
            return low if x < low else high if x > high else x

    assert Math.clamp(5, 0, 10) == 5
    assert Math.clamp(-2, 0, 10) == 0
    assert Math.clamp(99, 0, 10) == 10


# ---------------------------------------------------------------------------
# DRILL 06 — __repr__ vs __str__
# ---------------------------------------------------------------------------

def drill_06_repr_str():
    """Goal: Implement developer vs user friendly representations.

    Implement class `Task(id, title, done=False)` with:
      - __repr__ -> "Task(id=<id!r>, title=<title!r>, done=<done!r>)"
      - __str__  -> "[✔/✗] <title> (#<id>)"
    """
    # TODO: your code here
    class Task:
        def __init__(self, id, title, done=False):
            self.id = id
            self.title = title
            self.done = done

        def __repr__(self):
            return f"Task(id={self.id!r}, title={self.title!r}, done={self.done!r})"

        def __str__(self):
            return f"[{'✔' if self.done else '✗'}] {self.title} (#{self.id})"

    t = Task(1, "Write notes", True)
    assert repr(t) == "Task(id=1, title='Write notes', done=True)"
    assert str(t) == "[✔] Write notes (#1)"


# ---------------------------------------------------------------------------
# DRILL 07 — Equality semantics (__eq__) + NotImplemented
# ---------------------------------------------------------------------------

def drill_07_eq():
    """Goal: Implement value equality safely.

    Build class `User(user_id, email)` with __eq__ comparing only user_id and
    returning NotImplemented for unrelated types.
    """
    # TODO: your code here
    class User:
        def __init__(self, user_id, email):
            self.user_id = user_id
            self.email = email

        def __eq__(self, other):
            if not isinstance(other, User):
                return NotImplemented
            return self.user_id == other.user_id

    a = User(1, "a@x")
    b = User(1, "b@y")
    c = User(2, "c@z")
    assert a == b and not (a == c)
    assert (a == 5) is False  # Python falls back to NotImplemented -> False


# ---------------------------------------------------------------------------
# DRILL 08 — Encapsulation conventions (_name, __mangle)
# ---------------------------------------------------------------------------

def drill_08_encapsulation():
    """Goal: Use leading underscore and name-mangling.

    Create class `Sample` setting self._internal = 1 and self.__token = "abc".
    Prove that `__token` is stored as _Sample__token (name-mangled).
    """
    # TODO: your code here
    class Sample:
        def __init__(self):
            self._internal = 1
            self.__token = "abc"

    s = Sample()
    assert s._internal == 1
    assert getattr(s, "_Sample__token") == "abc"
    assert not hasattr(s, "__token")


# ---------------------------------------------------------------------------
# DRILL 09 — Properties with validation
# ---------------------------------------------------------------------------

def drill_09_property():
    """Goal: Expose attribute-like API with validation.

    Implement class `Rect(w, h)` with a read-only `area` property and a
    `width` property that validates value > 0 in the setter.
    """
    # TODO: your code here
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

    r = Rect(2, 3)
    assert r.area == 6
    r.width = 5
    assert (r.width, r.area) == (5, 15)


# ---------------------------------------------------------------------------
# DRILL 10 — Inheritance basics & overriding
# ---------------------------------------------------------------------------

def drill_10_inheritance():
    """Goal: Create a base class and a specialized subclass.

    Class `Animal.speak()` returns "?". Class `Dog(Animal)` overrides speak()
    to return "Woof". Verify both.
    """
    # TODO: your code here
    class Animal:
        def speak(self):
            return "?"

    class Dog(Animal):
        def speak(self):
            return "Woof"

    assert Animal().speak() == "?"
    assert Dog().speak() == "Woof"


# ---------------------------------------------------------------------------
# DRILL 11 — super() in __init__
# ---------------------------------------------------------------------------

def drill_11_super_init():
    """Goal: Preserve parent initialization when specializing.

    Base `Logger` sets self.events = []. Subclass `TimedLogger` also stores
    self.started = True but MUST call super().__init__().
    """
    # TODO: your code here
    class Logger:
        def __init__(self):
            self.events = []

    class TimedLogger(Logger):
        def __init__(self):
            super().__init__()
            self.started = True

    tl = TimedLogger()
    assert tl.started is True and isinstance(tl.events, list)


# ---------------------------------------------------------------------------
# DRILL 12 — Multi-level inheritance + MRO peek
# ---------------------------------------------------------------------------

def drill_12_multilevel_mro():
    """Goal: Understand attribute lookup through a chain.

    Create A -> B(A) -> C(B). Put method f in A, override in B to add "B",
    and in C call the inherited version via super().f() and add "+C".
    Verify result "A+B+C". Inspect mro with C.mro().
    """
    # TODO: your code here
    class A:
        def f(self):
            return "A"

    class B(A):
        def f(self):
            return super().f() + "+B"

    class C(B):
        def f(self):
            return super().f() + "+C"

    assert C().f() == "A+B+C"
    assert A in C.mro() and B in C.mro()


# ---------------------------------------------------------------------------
# DRILL 13 — Multiple inheritance & cooperative super()
# ---------------------------------------------------------------------------

def drill_13_multiple_inheritance():
    """Goal: Make mixins cooperate using super().

    Define mixins `M1` and `M2` both overriding `f` and calling super().
    Create class `X(M1, M2)` with a base providing f -> "X". The final result
    should be "X+M2+M1" given MRO (X, M1, M2, Base, ...).
    """
    # TODO: your code here
    class Base:
        def f(self):
            return "X"

    class M2(Base):
        def f(self):
            return super().f() + "+M2"

    class M1(M2):
        def f(self):
            return super().f() + "+M1"

    class X(M1, M2):
        pass

    assert X().f() == "X+M2+M1"


# ---------------------------------------------------------------------------
# DRILL 14 — Polymorphism & duck typing
# ---------------------------------------------------------------------------

def drill_14_duck_typing():
    """Goal: Accept any object that implements the needed behavior.

    Write function `announce(obj)` that returns obj.speak(). Provide two
    unrelated classes with speak(): `Dog` and `Robot`. No inheritance required.
    """
    # TODO: your code here
    def announce(obj):
        return obj.speak()

    class Dog:
        def speak(self):
            return "Woof"

    class Robot:
        def speak(self):
            return "Beep"

    assert announce(Dog()) == "Woof"
    assert announce(Robot()) == "Beep"


# ---------------------------------------------------------------------------
# DRILL 15 — Truthiness & ordering dunders
# ---------------------------------------------------------------------------

def drill_15_dunders_bool_lt():
    """Goal: Define custom truthiness and < comparison.

    Class `Score(value)` is truthy if value > 0 and supports `<` by value.
    """
    # TODO: your code here
    class Score:
        def __init__(self, value):
            self.value = value

        def __bool__(self):
            return self.value > 0

        def __lt__(self, other):
            if not isinstance(other, Score):
                return NotImplemented
            return self.value < other.value

    assert bool(Score(1)) and not bool(Score(0))
    assert Score(1) < Score(2)


# ---------------------------------------------------------------------------
# DRILL 16 — Arithmetic dunder (__add__)
# ---------------------------------------------------------------------------

def drill_16_add():
    """Goal: Return a new object when adding two of the same type.

    Class `Vector2(x, y)` supports v1 + v2 -> Vector2(x1+x2, y1+y2).
    Provide a useful __repr__.
    """
    # TODO: your code here
    class Vector2:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __add__(self, other):
            if not isinstance(other, Vector2):
                return NotImplemented
            return Vector2(self.x + other.x, self.y + other.y)

        def __repr__(self):
            return f"Vector2({self.x}, {self.y})"

    v = Vector2(1, 2) + Vector2(3, 4)
    assert repr(v) == "Vector2(4, 6)"


# ---------------------------------------------------------------------------
# DRILL 17 — Custom container protocol
# ---------------------------------------------------------------------------

def drill_17_container():
    """Goal: Implement len, iteration, membership, indexing.

    Class `Bag(items=None)` wraps a list and supports len(b), for x in b,
    x in b, and b[i].
    """
    # TODO: your code here
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

    b = Bag([1, 2, 3])
    assert len(b) == 3 and 2 in b and list(iter(b)) == [1, 2, 3]
    assert b[0] == 1


# ---------------------------------------------------------------------------
# DRILL 18 — Extending built-ins vs composition
# ---------------------------------------------------------------------------

def drill_18_extend_builtins():
    """Goal: Understand pros/cons of subclassing built-ins.

    Create `LimitedList(list)` that restricts append if length >= limit.
    Also create `LimitedBag` using composition with the same behavior.
    """
    # TODO: your code here
    class LimitedList(list):
        def __init__(self, limit, *args):
            super().__init__(*args)
            self.limit = limit

        def append(self, x):
            if len(self) >= self.limit:
                raise ValueError("limit reached")
            super().append(x)

    ll = LimitedList(2)
    ll.append(1)
    ll.append(2)
    try:
        ll.append(3)
        assert False, "should have raised"
    except ValueError:
        pass

    class LimitedBag:
        def __init__(self, limit):
            self._data = []
            self.limit = limit

        def add(self, x):
            if len(self._data) >= self.limit:
                raise ValueError("limit reached")
            self._data.append(x)

        def __len__(self):
            return len(self._data)

    lb = LimitedBag(1)
    lb.add(42)
    try:
        lb.add(99)
        assert False, "should have raised"
    except ValueError:
        pass
    assert len(lb) == 1


# ---------------------------------------------------------------------------
# DRILL 19 — Abstract Base Classes (ABCs)
# ---------------------------------------------------------------------------

def drill_19_abcs():
    """Goal: Specify required methods.

    Define abstract base class `Serializer` with abstract method dumps(self, obj).
    Implement `JsonSerializer(Serializer)` using json.dumps.
    """
    # TODO: your code here
    from abc import ABC, abstractmethod
    import json

    class Serializer(ABC):
        @abstractmethod
        def dumps(self, obj):
            ...

    class JsonSerializer(Serializer):
        def dumps(self, obj):
            return json.dumps(obj)

    s = JsonSerializer()
    assert s.dumps({"a": 1}) == "{""a"": 1}"


# ---------------------------------------------------------------------------
# DRILL 20 — Data classes (@dataclass)
# ---------------------------------------------------------------------------

def drill_20_dataclass():
    """Goal: Generate init/repr/eq automatically for data containers.

    Create @dataclass `Point(x: int, y: int)` and show repr and equality.
    """
    # TODO: your code here
    from dataclasses import dataclass

    @dataclass
    class Point:
        x: int
        y: int

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    assert p1 == p2 and "Point(" in repr(p1)


# ---------------------------------------------------------------------------
# DRILL 21 — Decorators (method wrapper preview)
# ---------------------------------------------------------------------------

def drill_21_decorator_preview():
    """Goal: Recognize/trace a simple decorator on methods.

    Write decorator `count_calls` that increments `self._calls` before the
    method runs. Use it on class `Greeter.hello(self, name)`.
    """
    # TODO: your code here
    def count_calls(func):
        def wrapper(self, *args, **kwargs):
            self._calls = getattr(self, "_calls", 0) + 1
            return func(self, *args, **kwargs)
        return wrapper

    class Greeter:
        @count_calls
        def hello(self, name):
            return f"Hello, {name}"

    g = Greeter()
    g.hello("A")
    g.hello("B")
    assert g._calls == 2


# ---------------------------------------------------------------------------
# DRILL 22 — Integration: tiny Todo model
# ---------------------------------------------------------------------------

def drill_22_integration_todo():
    """Goal: Combine constructor, repr/str, equality, classmethod, property.

    Build class `Todo(id, title, done=False)` with:
      - classmethod `from_title(title)` -> auto id from a class counter
      - __repr__ and __str__ (per notes style)
      - __eq__ by id
      - property `title` with non-empty validation
    """
    # TODO: your code here
    class Todo:
        _next_id = 1

        def __init__(self, id, title, done=False):
            self.id = id
            self._title = title
            self.done = done

        @classmethod
        def from_title(cls, title):
            t = cls(cls._next_id, title)
            cls._next_id += 1
            return t

        @property
        def title(self):
            return self._title

        @title.setter
        def title(self, value):
            if not value:
                raise ValueError("title cannot be empty")
            self._title = value

        def __repr__(self):
            return f"Todo(id={self.id!r}, title={self.title!r}, done={self.done!r})"

        def __str__(self):
            return f"[{'✔' if self.done else '✗'}] {self.title} (#{self.id})"

        def __eq__(self, other):
            if not isinstance(other, Todo):
                return NotImplemented
            return self.id == other.id

    t1 = Todo.from_title("Read docs")
    t2 = Todo.from_title("Write code")
    assert t1.id == 1 and t2.id == 2
    assert str(t1).startswith("[✗] Read docs")
    t1.title = "Study OOP"
    try:
        t1.title = ""
        assert False, "should have raised"
    except ValueError:
        pass
    assert (t1 == Todo(1, "X")) is True


# ----------------------------------------------------------------------------
# Simple test runner (optional). Comment out if you prefer running per-function.
# ----------------------------------------------------------------------------

def run_tests():
    drills = [
        drill_01_binding,
        drill_02_init,
        drill_03_class_vs_instance,
        drill_04_classmethod,
        drill_05_staticmethod,
        drill_06_repr_str,
        drill_07_eq,
        drill_08_encapsulation,
        drill_09_property,
        drill_10_inheritance,
        drill_11_super_init,
        drill_12_multilevel_mro,
        drill_13_multiple_inheritance,
        drill_14_duck_typing,
        drill_15_dunders_bool_lt,
        drill_16_add,
        drill_17_container,
        drill_18_extend_builtins,
        drill_19_abcs,
        drill_20_dataclass,
        drill_21_decorator_preview,
        drill_22_integration_todo,
    ]
    for i, fn in enumerate(drills, 1):
        fn()
        print(f"✓ Drill {i:02d} passed: {fn.__name__}")


if __name__ == "__main__":
    run_tests()
