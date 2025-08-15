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
values = [5, 42, 7, 42]

if 42 in values:
    print(values.index(42))
else:
    print("Not found")

# Drill 7: Sorting basics
# Prompt: Sort scores = [75, 92, 88, 69] ascending, then descending. Print both results.
# TODO: implement


# Drill 8: Sort with lambda key
# Prompt: Sort students = [("Ana", 3.7), ("Ben", 3.9), ("Cleo", 3.5)] by GPA.
# Print the sorted list.
# TODO: implement


# Drill 9: map()
# Prompt: Convert prices_eur = [10, 20, 30] to USD with rate 1.1.
# Use map() and build a list. Print it.
# TODO: implement


# Drill 10: filter()
# Prompt: Keep only even numbers from nums = list(range(1, 21)).
# Use filter() and build a list. Print it.
# TODO: implement


# Drill 11: List comprehensions
# Prompt: Rewrite drills 9 and 10 using comprehensions.
# Build usd list and evens list. Print both.
# TODO: implement


# Drill 12: zip()
# Prompt: Pair ids = [1,2,3] with names = ["A","B","C"] using zip().
# Create a list of tuples and print it.
# TODO: implement


# Drill 13: Stack with list
# Prompt: Implement push, pop, peek using a list as a stack; demonstrate 3 operations.
# TODO: implement


# Drill 14: Queue with deque
# Prompt: Use collections.deque to enqueue three items and dequeue two; print remaining.
# TODO: implement


# Drill 15: Tuples and immutability
# Prompt: Create color = (255, 160, 64), unpack into r,g,b. Try modifying (comment result) and print originals.
# TODO: implement


# Drill 16: Swapping variables
# Prompt: Swap a = 10 and b = 20 using tuple unpacking. Print before/after.
# TODO: implement


# Drill 17: Arrays (typed)
# Prompt: Create from array import array; make arr = array('i', [1,2,3]); append 4; print arr.
# Add a commented line showing that arr.append(2.5) would raise TypeError.
# TODO: implement


# Drill 18: Sets - uniqueness
# Prompt: From text = "a b c a b d", build a set of unique words; print size and membership of "c" and "z".
# TODO: implement


# Drill 19: Dictionaries
# Prompt: person = {"name": "Ada", "age": 35}; update age to 36; print keys and values.
# TODO: implement


# Drill 20: Dict comprehension
# Prompt: words = ["apple", "banana", "pear"]; build {w: len(w)} using dict comprehension; print it.
# TODO: implement


# Drill 21: Generator expression
# Prompt: Compute sum of squares 1..10 using a generator expression (no list created).
# TODO: implement


# Drill 22: Unpacking operator * and **
# Prompt: Merge a = [1,2] and b = [3,4] into c using *; merge two dicts using **; print results.
# TODO: implement


# Drill 23: Mini exercise (mixed)
# Prompt: Given transactions = [("+", 30), ("-", 10), ("+", 5)],
# compute final balance starting from 0 using a loop or comprehension; print the result.
# TODO: implement


# ===== END OF DRILLS =====
