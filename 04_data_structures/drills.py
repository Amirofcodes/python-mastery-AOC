# 04_data_structures - Micro-drills for Lists, Tuples, Sets, Dicts, and Friends
#
# Instructions:
# - Type every solution yourself to build muscle memory.
# - Only use concepts from previous sections + data structures listed here.
# - Keep each drill small and focused. Print outputs to verify behavior.

# ===== DRILLS TO COMPLETE (1-23) =====

# Drill 1: Lists, len(), indexing
# Prompt: Create a list letters = ["a", "b", "c"].
# Print the length, the first item, and the last item.
# TODO: implement
from array import array
from collections import deque
letters = ["a", "b", "c"]

print(
    f"'letters' is a list with {len(letters)} items: '{letters[0]}' first, '{letters[-1]}' last")

# Drill 2: Indexing and slicing
# Prompt: Given nums = [10, 20, 30, 40, 50],
# print the second item and the last two items using slicing.
# TODO: implement
nums = [10, 20, 30, 40, 50]

print(nums[1], nums[-2:])

# Drill 3: Unpacking
# Prompt: Unpack point = [3, 7, 9] into x, y, z and print them.
# TODO: implement
point = [3, 7, 9]
x, y, z = point

print(x, y, z)

# Drill 4: Looping with enumerate
# Prompt: For names = ["Ana", "Ben", "Cleo"],
# print "<index>: <name>" using enumerate.
# TODO: implement
names = ["Ana", "Ben", "Cleo"]

for index, name in enumerate(names):
    print(f"{index}: {name}")


# Drill 5: Add/Remove items
# Prompt: Start with letters = ["a", "b", "c"].
# Perform: append("d"), insert(0, "-"), pop(0), remove("b"). Print final list.
# TODO: implement
letters = ["a", "b", "c"]

letters.append("d")
letters.insert(0, "-")
letters.pop(0)
letters.remove("b")

print(letters)

# Drill 6: Membership and search
# Prompt: For values = [5, 42, 7, 42],
# print the first index of 42 if present, else print "Not found".
# TODO: implement
values = [5, 42, 7, 42]
# first solution
for x in values:
    if x == 42:
        print(values.index(x))
        break
    else:
        if 42 not in values:
            print("Not found")

# optimal solution
if 42 in values:
    print(values.index(42))
else:
    print("Not found")

# Drill 7: Sorting basics
# Prompt: Sort scores = [75, 92, 88, 69] ascending, then descending. Print both results.
# TODO: implement
scores = [75, 92, 88, 69]
ascending = sorted(scores)
descending = sorted(scores, reverse=True)

print(ascending)
print(descending)


# Drill 8: Sort with lambda key
# Prompt: Sort students = [("Ana", 3.7), ("Ben", 3.9), ("Cleo", 3.5)] by GPA.
# Print the sorted list.
# TODO: implement
students = [("Ana", 3.7), ("Ben", 3.9), ("Cleo", 3.5)]
gpa_sort = sorted(students, key=lambda student: student[1])
print(gpa_sort)

# Drill 9: map()
# Prompt: Convert prices_eur = [10, 20, 30] to USD with rate 1.1.
# Use map() and build a list. Print it.
# TODO: implement
prices_eur = [10, 20, 30]
prices_usd = map(lambda p: p * 1.1, prices_eur)
print(list(prices_usd))
# functional programming approach that's equivalent to:
prices_usd2 = []
for p in prices_eur:
    prices_usd2.append(p * 1.1)

# Drill 10: filter()
# Prompt: Keep only even numbers from nums = list(range(1, 21)).
# Use filter() and build a list. Print it.
# TODO: implement
nums = list(range(1, 21))

filtered = list(filter(lambda n: n % 2 == 0, nums))
print(filtered)

# equivalent to:
filtered2 = []
for n in nums:
    if n % 2 == 0:
        filtered2.append(n)

# Drill 11: List comprehensions
# Prompt: Rewrite drills 9 and 10 using comprehensions.
# Build usd list and evens list. Print both.
# TODO: implement
prices_usd3 = [x * 1.1 for x in prices_eur]

nums = list(range(1, 21))
filtered3 = [x for x in nums if x % 2 == 0]
print(prices_usd3)
print(filtered3)


# Drill 12: zip()
# Prompt: Pair ids = [1,2,3] with names = ["A","B","C"] using zip().
# Create a list of tuples and print it.
# TODO: implement
ids = [1, 2, 3]
names = ["A", "B", "C"]

print(tuple(zip(ids, names)))

# Drill 13: Stack with list
# Prompt: Implement push, pop, peek using a list as a stack; demonstrate 3 operations.
# TODO: implement
stack = [5, 9, 0, 4, 2, 1]
print(stack)
stack.append(7)
print(stack)
stack.pop()
print(stack)
print(stack[-1])


# Drill 14: Queue with deque
# Prompt: Use collections.deque to enqueue three items and dequeue two; print remaining.
# TODO: implement

queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(queue)
queue.append(10)
queue.append(11)
queue.append(12)
print(queue)

queue.popleft()
queue.popleft()
print(queue)

# Drill 15: Tuples and immutability
# Prompt: Create color = (255, 160, 64), unpack into r,g,b. Try modifying (comment result) and print originals.
# TODO: implement
color = (255, 160, 64)
r, g, b = color

print(r, g, b)
# color[0] = 128  # TypeError: 'tuple' object does not support item assignment
# Tuples are immutable - cannot change values after creation

# Drill 16: Swapping variables
# Prompt: Swap a = 10 and b = 20 using tuple unpacking. Print before/after.
# TODO: implement
a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)

# Drill 17: Arrays (typed)
# Prompt: Create from array import array; make arr = array('i', [1,2,3]); append 4; print arr.
# Add a commented line showing that arr.append(2.5) would raise TypeError.
# TODO: implement

arr = array('i', [1, 2, 3])
print(arr)
arr.append(4)
print(arr)
# arr.append(2.5)
# TypeError: 'float' object cannot be interpreted as an integer

# Drill 18: Sets - uniqueness
# Prompt: From text = "a b c a b d", build a set of unique words; print size and membership of "c" and "z".
# TODO: implement
text = "a b c a b d"
words = set(text.split())  # split() creates ["a", "b", "c", "a", "b", "d"]
# set() removes duplicates → {"a", "b", "c", "d"}
print(len(words))         # Size of unique words
print("c" in words)       # True - "c" is in the set
print("z" in words)       # False - "z" is not in the set

# Drill 19: Dictionaries
# Prompt: person = {"name": "Ada", "age": 35}; update age to 36; print keys and values.
# TODO: implement
person = {"name": "Ada", "age": 35}
print(person)
person["age"] = 36
print(person)

for key, value in person.items():
    print(key, value)


# Drill 20: Dict comprehension
# Prompt: words = ["apple", "banana", "pear"]; build {w: len(w)} using dict comprehension; print it.
# TODO: implement
words = ["apple", "banana", "pear"]
lengths = {w: len(w) for w in words}
print(lengths)


# Drill 21: Generator expression
# Prompt: Compute sum of squares 1..10 using a generator expression (no list created).
# TODO: implement
total = sum(n * n for n in range(1, 11))

# Drill 22: Unpacking operator * and **
# Prompt: Merge a = [1,2] and b = [3,4] into c using *; merge two dicts using **; print results.
# TODO: implement
a = [1, 2]
b = [3, 4]
c = [*a, *b]

first = {"x": 1, "y": 2}
second = {"z": 3, "w": 4}
Combined = {**first, **second}

print(c)
print(Combined)


# Drill 23: Mini exercise (mixed)
# Prompt: Given transactions = [("+", 30), ("-", 10), ("+", 5)],
# compute final balance starting from 0 using a loop or comprehension; print the result.
# TODO: implement
transactions = [("+", 30), ("-", 10), ("+", 5)]
balance = 0

# Method 1: Simple Loop
for operation, amount in transactions:
    if operation == "+":
        balance += amount
    elif operation == "-":
        balance -= amount
print(balance)

# Method 2: Loop with Conditional Expression
for operation, amount in transactions:
    balance += amount if operation == "+" else -amount


# Method 3: List Comprehension + sum()

balance = sum(amount if op == "+" else -amount for op, amount in transactions)

print(balance)  # 25

# What the generator expression does internally:


def process_transactions():
    for op, amount in transactions:
        if op == "+":
            yield amount
        else:
            yield -amount


balance = sum(process_transactions())

# Alternative Syntax (Actual List Comprehension)
# Creates intermediate list in memory
values = [amount if op == "+" else -amount for op, amount in transactions]
balance = sum(values)


# ===== END OF DRILLS =====
