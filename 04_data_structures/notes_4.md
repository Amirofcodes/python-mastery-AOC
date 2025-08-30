# 04 · Data Structures - Comprehensive Mastery Guide

Master Python's core collections through complete understanding of **all the different ways** to create, access, and manipulate lists, tuples, sets, and dictionaries.

---

## **Mental Model: Choosing the Right Tool**

- **List** `[]`: Ordered, mutable sequences. Use when order matters and you need to modify.
- **Tuple** `()`: Ordered, immutable sequences. Use for fixed data that won't change.
- **Dictionary** `{}`: Key-value mappings. Use for lookups and associating data.
- **Set** `{}`/`set()`: Unique, unordered collections. Use for membership testing and uniqueness.

---

# **LISTS - Ordered, Mutable Collections**

## **1. Creating Lists - All Methods**

```python
# Method 1: Literal syntax (most common)
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]

# Method 2: Constructor from iterables
letters = list("hello")        # ['h', 'e', 'l', 'l', 'o']
digits = list(range(5))        # [0, 1, 2, 3, 4]
copy_list = list(fruits)       # Creates new list

# Method 3: Repetition
zeros = [0] * 5               # [0, 0, 0, 0, 0]
pattern = ["a", "b"] * 3      # ['a', 'b', 'a', 'b', 'a', 'b']

# Method 4: Concatenation
combined = [1, 2] + [3, 4]    # [1, 2, 3, 4]

# Method 5: Empty list
empty = []
also_empty = list()
```

## **2. Accessing Elements - All Methods**

```python
nums = [10, 20, 30, 40, 50]

# Basic indexing
first = nums[0]        # 10 (first element)
last = nums[-1]        # 50 (last element)
second_last = nums[-2] # 40 (second from end)

# Slicing - [start:stop:step]
middle = nums[1:4]     # [20, 30, 40] (indices 1, 2, 3)
first_three = nums[:3] # [10, 20, 30] (start to index 3)
last_two = nums[-2:]   # [40, 50] (last 2 elements)
every_other = nums[::2] # [10, 30, 50] (every 2nd element)
reversed_list = nums[::-1] # [50, 40, 30, 20, 10] (reversed)

# Length
size = len(nums)       # 5
```

## **3. Modifying Lists - All Methods**

```python
fruits = ["apple", "banana"]

# Adding elements
fruits.append("cherry")           # Add to end: ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")       # Insert at index 1: ['apple', 'orange', 'banana', 'cherry']
fruits.extend(["grape", "kiwi"])  # Add multiple: ['apple', 'orange', 'banana', 'cherry', 'grape', 'kiwi']
fruits += ["mango"]               # Concatenate: ['apple', 'orange', 'banana', 'cherry', 'grape', 'kiwi', 'mango']

# Removing elements
fruits.remove("banana")           # Remove first occurrence
last_item = fruits.pop()          # Remove and return last item
second_item = fruits.pop(1)       # Remove and return item at index 1
del fruits[0]                     # Delete item at index 0
fruits.clear()                    # Remove all elements

# Modifying in place
fruits = ["banana", "apple", "cherry"]
fruits.sort()                     # Sort in place: ['apple', 'banana', 'cherry']
fruits.reverse()                  # Reverse in place: ['cherry', 'banana', 'apple']
fruits[0] = "date"               # Direct assignment: ['date', 'banana', 'apple']
```

## **4. Searching and Counting**

```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# Membership testing
is_present = 3 in numbers        # True
is_absent = 10 not in numbers    # True

# Finding positions
try:
    index = numbers.index(2)     # 1 (first occurrence)
    last_index = numbers.index(2, 2)  # 3 (search starting from index 2)
except ValueError:
    print("Not found")

# Counting occurrences
count = numbers.count(2)         # 3 (appears 3 times)
```

## **5. Copying Lists - Important Differences**

```python
original = [1, 2, [3, 4]]

# Reference (NOT a copy)
ref = original                   # Same object, changes affect both

# Shallow copies (copy list structure, not nested objects)
copy1 = original.copy()          # Method 1: .copy()
copy2 = original[:]              # Method 2: slicing  
copy3 = list(original)           # Method 3: constructor

# For nested objects, you need deep copy
import copy
deep_copy = copy.deepcopy(original)  # Complete independent copy
```

## **6. List as Stack (LIFO - Last In, First Out)**

```python
stack = []

# Stack operations
stack.append("first")    # Push: ['first']
stack.append("second")   # Push: ['first', 'second']
item = stack.pop()       # Pop: 'second', stack is now ['first']
top = stack[-1] if stack else None  # Peek at top without removing
```

---

# **TUPLES - Ordered, Immutable Collections**

## **1. Creating Tuples - All Methods**

```python
# Method 1: Literal syntax
coordinates = (3, 7)
rgb = (255, 160, 64)
empty = ()                       # Empty tuple

# Method 2: Single element (comma required!)
single = (42,)                   # Note the comma!
also_single = 42,                # Comma creates tuple

# Method 3: Without parentheses (tuple packing)
point = 10, 20                   # (10, 20)
person = "Alice", 25, "Engineer" # ("Alice", 25, "Engineer")

# Method 4: Constructor
tuple_from_list = tuple([1, 2, 3])  # (1, 2, 3)
tuple_from_string = tuple("abc")     # ('a', 'b', 'c')

# Method 5: Multiple assignment
x, y = 10, 20  # Same as: temp = (10, 20); x, y = temp
```

## **2. Accessing Tuples**

```python
data = ("Alice", 25, "Engineer", "New York")

# Indexing (same as lists)
name = data[0]           # "Alice"
age = data[1]            # 25
city = data[-1]          # "New York" (last element)

# Slicing (same as lists)
personal = data[:2]      # ("Alice", 25)
work_location = data[2:] # ("Engineer", "New York")

# Length
size = len(data)         # 4
```

## **3. Tuple Methods**

```python
numbers = (1, 2, 3, 2, 4, 2)

# Searching
index = numbers.index(2)         # 1 (first occurrence)
count = numbers.count(2)         # 3 (appears 3 times)

# Membership
is_present = 3 in numbers        # True
```

## **4. Tuple Unpacking - All Patterns**

```python
# Basic unpacking
point = (10, 20)
x, y = point                     # x=10, y=20

# Multi-level unpacking
nested = ((1, 2), (3, 4))
(a, b), (c, d) = nested         # a=1, b=2, c=3, d=4

# Starred unpacking (Python 3.0+)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers   # first=1, middle=[2,3,4], last=5
head, *tail = numbers            # head=1, tail=[2,3,4,5]

# Function arguments unpacking
def greet(name, age, city):
    print(f"{name}, {age}, from {city}")

person = ("Alice", 25, "NYC")
greet(*person)                   # Unpacks tuple as arguments

# Swapping variables
a, b = 10, 20
a, b = b, a                      # Swap: a=20, b=10
```

## **5. When to Use Tuples**

```python
# Use Case 1: Multiple return values
def get_name_age():
    return "Alice", 25           # Returns tuple

name, age = get_name_age()       # Unpack return value

# Use Case 2: Dictionary keys (immutable required)
locations = {
    (0, 0): "origin",
    (1, 1): "northeast",
    (10, 20): "somewhere"
}

# Use Case 3: Fixed records (won't change)
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}

# Use Case 4: Configuration that shouldn't change
DATABASE_CONFIG = ("localhost", 5432, "mydb", "user")
```

---

# **DICTIONARIES - Key-Value Mappings**

## **1. Creating Dictionaries - All Methods**

```python
# Method 1: Literal syntax
person = {"name": "Alice", "age": 25, "city": "NYC"}
empty = {}

# Method 2: Constructor with keyword arguments
person2 = dict(name="Bob", age=30, city="LA")

# Method 3: Constructor from pairs
pairs = [("name", "Carol"), ("age", 35)]
person3 = dict(pairs)

# Method 4: From keys with same value
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)    # {"a": 0, "b": 0, "c": 0}

# Method 5: Dictionary comprehension (preview)
squares = {x: x**2 for x in range(5)}    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## **2. Accessing Dictionary Values - All Methods**

```python
student = {"name": "Alice", "grade": 95, "course": "Python"}

# Method 1: Square bracket notation
name = student["name"]           # "Alice" (raises KeyError if missing)

# Method 2: get() method (safer)
grade = student.get("grade")     # 95
missing = student.get("missing") # None (no error)
default = student.get("missing", "N/A") # "N/A" (custom default)

# Method 3: Checking existence first
if "grade" in student:
    grade = student["grade"]

# Method 4: Using setdefault (get with automatic insertion)
email = student.setdefault("email", "unknown@email.com")  # Sets and returns default if missing
```

## **3. Modifying Dictionaries - All Methods**

```python
student = {"name": "Alice", "grade": 95}

# Adding/updating single values
student["course"] = "Python"     # Add new key-value pair
student["grade"] = 98            # Update existing value

# Updating multiple values
student.update({"semester": 1, "credits": 3})           # From dict
student.update([("year", 2024), ("professor", "Dr. X")]) # From pairs
student.update(gpa=3.8, status="active")                # Using keywords

# Removing values
grade = student.pop("grade")              # Remove and return value
item = student.pop("missing", "default")  # Pop with default if missing
random_item = student.popitem()           # Remove and return arbitrary (key, value)
del student["course"]                     # Delete key (raises KeyError if missing)
student.clear()                          # Remove all items
```

## **4. Dictionary Iteration - All Patterns**

```python
student = {"name": "Alice", "grade": 95, "course": "Python"}

# Iterate over keys (default)
for key in student:
    print(key)                   # name, grade, course

# Explicit keys iteration  
for key in student.keys():
    print(key, student[key])

# Iterate over values
for value in student.values():
    print(value)                 # Alice, 95, Python

# Iterate over key-value pairs (most common)
for key, value in student.items():
    print(f"{key}: {value}")     # name: Alice, grade: 95, course: Python
```

## **5. Dictionary Merging - All Methods**

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 20, "e": 5}  # Note: 'b' conflicts with dict1

# Method 1: update() (modifies original)
dict1.update(dict2)              # dict1 is now {"a": 1, "b": 2, "c": 3, "d": 4}

# Method 2: Unpacking (creates new dict)
merged = {**dict1, **dict2, **dict3}  # {"a": 1, "b": 20, "c": 3, "d": 4, "e": 5}

# Method 3: Union operator (Python 3.9+)
# merged = dict1 | dict2 | dict3    # Same as unpacking
```

## **6. Common Dictionary Patterns**

```python
# Pattern 1: Counting items
text = "hello world"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
# Result: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Pattern 2: Grouping items
students = [("Alice", "CS"), ("Bob", "Math"), ("Carol", "CS"), ("Dave", "Math")]
by_major = {}
for name, major in students:
    by_major.setdefault(major, []).append(name)
# Result: {"CS": ["Alice", "Carol"], "Math": ["Bob", "Dave"]}

# Pattern 3: Dictionary as switch statement
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Error"
}
result = operations.get("+", lambda x, y: "Unknown")(10, 5)  # 15
```

---

# **SETS - Unique, Unordered Collections**

## **1. Creating Sets - All Methods**

```python
# Method 1: Literal syntax (non-empty sets)
colors = {"red", "green", "blue"}
mixed = {1, "hello", 3.14}

# Method 2: Constructor
empty_set = set()                # Must use set(), not {}
from_list = set([1, 2, 3, 2])   # {1, 2, 3} (duplicates removed)
from_string = set("hello")       # {'h', 'e', 'l', 'o'} (unique letters)

# Method 3: Set comprehension (preview)
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

## **2. Set Operations - Mathematical Style**

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (combine all elements)
union = set1 | set2              # {1, 2, 3, 4, 5, 6}
union_method = set1.union(set2)  # Same result

# Intersection (common elements)
intersection = set1 & set2           # {3, 4}
intersection_method = set1.intersection(set2)  # Same result

# Difference (in first but not second)
difference = set1 - set2             # {1, 2}
difference_method = set1.difference(set2)  # Same result

# Symmetric difference (in either but not both)
sym_diff = set1 ^ set2               # {1, 2, 5, 6}
sym_diff_method = set1.symmetric_difference(set2)  # Same result
```

## **3. Set Modification**

```python
colors = {"red", "green"}

# Adding elements
colors.add("blue")               # {"red", "green", "blue"}
colors.update(["yellow", "purple"]) # Add multiple elements

# Removing elements  
colors.remove("red")             # Raises KeyError if not present
colors.discard("orange")         # No error if not present
popped = colors.pop()            # Remove arbitrary element
colors.clear()                   # Remove all elements
```

## **4. Set Testing**

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {4, 5}

# Membership
is_member = 2 in set1            # True

# Subset/superset relationships
is_subset = set1.issubset(set2)      # True (set1 ⊆ set2)
is_superset = set2.issuperset(set1)  # True (set2 ⊇ set1)
are_disjoint = set1.isdisjoint(set3) # True (no common elements)
```

## **5. When to Use Sets**

```python
# Use Case 1: Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list(set(numbers))  # [1, 2, 3, 4] (order may vary)

# Use Case 2: Fast membership testing
valid_codes = {"A001", "B002", "C003"}  # O(1) lookup
user_code = "A001"
if user_code in valid_codes:             # Much faster than list lookup
    print("Valid code")

# Use Case 3: Finding common items
users_a = {"alice", "bob", "charlie"}
users_b = {"bob", "diana", "eve"}
common_users = users_a & users_b         # {"bob"}

# Use Case 4: Data validation
required_fields = {"name", "email", "age"}
provided_fields = {"name", "email", "phone"}
missing_fields = required_fields - provided_fields  # {"age"}
```

---

# **Performance & Choice Guidelines**

## **When to Use Each Data Structure**

| Need | Use | Why |
|------|-----|-----|
| Ordered sequence, mutable | **List** | Can modify, maintain order |
| Ordered sequence, immutable | **Tuple** | Can't change, memory efficient |
| Fast lookup by key | **Dictionary** | O(1) average key access |
| Unique items, fast membership | **Set** | O(1) membership testing |
| Simple collection | **List** | Most versatile, good default |

## **Performance Considerations**

```python
# Fast operations (O(1) average)
dict_lookup = my_dict["key"]     # Dictionary key access
set_membership = item in my_set  # Set membership testing
list_append = my_list.append(x)  # List append to end

# Slow operations (O(n))
list_membership = item in my_list    # List membership (scans all)
list_insert = my_list.insert(0, x)  # List insert at beginning
list_remove = my_list.remove(x)     # List remove (finds then removes)
```

---

# **Error Handling with Data Structures**

```python
# Common errors and how to handle them

# KeyError with dictionaries
try:
    value = my_dict["missing_key"]
except KeyError:
    value = "default"
# Better: use .get() method
value = my_dict.get("missing_key", "default")

# ValueError with lists
try:
    index = my_list.index("item")
except ValueError:
    print("Item not found")

# IndexError with sequences
try:
    item = my_list[100]
except IndexError:
    print("Index out of range")
```

---

This comprehensive guide covers **all the different ways** to work with Python's core data structures. Practice each method until they become second nature - this foundation is crucial for everything that follows in Python programming.
