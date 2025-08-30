# 04_data_structures - Comprehensive Mastery Drills
#
# Instructions:
# 1. Copy this template to drills.py to start fresh practice
# 2. Complete each drill by typing the solution yourself to build muscle memory
# 3. Only use concepts from previous sections + data structures from notes_4_comprehensive.md
# 4. Test every method and pattern until they become second nature
# 5. Focus on learning ALL the different ways to accomplish each task
#
# Notes: See notes_4_comprehensive.md for detailed explanations

# ===== LISTS - COMPREHENSIVE MASTERY (8 DRILLS) =====

# Drill 1: List creation methods
# Prompt: Create the same list [1, 2, 3, 4, 5] using 5 different methods:
# literal syntax, list(), range, repetition/concatenation, and one creative method.
# Core concept: List creation methods
# TODO: Show 5 different ways to create [1, 2, 3, 4, 5]


# Drill 2: List access and slicing mastery
# Prompt: Given `data = [10, 20, 30, 40, 50, 60, 70]`, extract:
# - First and last elements
# - Middle 3 elements
# - Every second element
# - Reversed list
# - Last 3 elements
# Core concept: All indexing and slicing patterns
# TODO: Use different indexing/slicing to get each result


# Drill 3: List modification - all methods
# Prompt: Start with `items = ["a", "b", "c"]`. Demonstrate:
# append(), insert(), extend(), +=, remove(), pop(), del, clear()
# Show how each method changes the list. Print state after each operation.
# Core concept: All list modification methods
# TODO: Apply each modification method and show results


# Drill 4: List searching and counting
# Prompt: Given `numbers = [5, 3, 8, 3, 1, 3, 9, 2]`, find:
# - Is 3 present? Is 10 present?
# - First index of 3, handle case when item not found
# - Count how many times 3 appears
# - Find index of 3 starting from position 2
# Core concept: Searching patterns and error handling
# TODO: Use in, index(), count() with proper error handling


# Drill 5: List sorting - in-place vs new list
# Prompt: Given `scores = [88, 95, 72, 91, 83]`:
# - Sort original list in place (ascending and descending)
# - Create new sorted lists (don't modify original)
# - Sort by absolute distance from 85
# Compare methods: .sort() vs sorted(), with/without reverse and key parameters.
# Core concept: All sorting methods and parameters
# TODO: Demonstrate .sort() vs sorted() with different parameters


# Drill 6: List copying - shallow vs reference
# Prompt: Create `original = [1, 2, [3, 4]]`. Make:
# - A reference (changes affect both)
# - Three types of shallow copies
# - Show what happens when you modify the nested list in each case
# Core concept: Reference vs copying, shallow copy behavior
# TODO: Show reference assignment and 3 shallow copy methods


# Drill 7: List as stack operations
# Prompt: Create a stack using a list. Implement push, pop, and peek operations.
# Demonstrate LIFO (Last In, First Out) behavior with 5 operations.
# Handle empty stack cases gracefully.
# Core concept: Stack implementation with lists
# TODO: Implement stack operations and show LIFO behavior


# Drill 8: List performance patterns
# Prompt: Compare membership testing: create a list of 1000 numbers,
# time checking if 999 is in the list vs if 1 is in the list.
# Explain why position matters for list membership testing.
# Core concept: List performance characteristics
# TODO: Demonstrate O(n) membership testing behavior


# ===== TUPLES - COMPREHENSIVE MASTERY (4 DRILLS) =====

# Drill 9: Tuple creation methods
# Prompt: Create the same tuple (1, 2, 3) using 4 different methods:
# parentheses, without parentheses, constructor, single element tuple.
# Also create an empty tuple.
# Core concept: All tuple creation methods
# TODO: Show different ways to create tuples, including single element


# Drill 10: Tuple unpacking mastery
# Prompt: Given `data = ("Alice", 25, "Engineer", "NYC", "Python", "Advanced")`:
# - Unpack first 3 elements
# - Unpack first, last, and middle elements using starred unpacking
# - Swap two variables using tuple unpacking
# - Pass tuple as function arguments using unpacking
# Core concept: All unpacking patterns
# TODO: Demonstrate basic, starred, and function unpacking


# Drill 11: Tuple methods and immutability
# Prompt: Given `numbers = (1, 2, 3, 2, 4, 2, 5)`:
# - Find first index of 2 and count occurrences
# - Try to modify tuple (comment the error)
# - Show how tuples can be used as dictionary keys
# Core concept: Tuple methods, immutability, use as keys
# TODO: Use .index(), .count(), show immutability, dict key usage


# Drill 12: When to use tuples vs lists
# Prompt: Create examples showing when tuples are better than lists:
# - Function returning multiple values
# - Fixed configuration that shouldn't change
# - Dictionary keys (coordinates)
# - Records that represent fixed structure
# Core concept: Tuple use cases and design choices
# TODO: Show 4 practical examples where tuples are preferred


# ===== DICTIONARIES - COMPREHENSIVE MASTERY (6 DRILLS) =====

# Drill 13: Dictionary creation methods
# Prompt: Create the same dictionary {"a": 1, "b": 2, "c": 3} using 4 methods:
# literal syntax, dict(), dict from pairs, dict.fromkeys() with update.
# Core concept: All dictionary creation methods
# TODO: Show 4 different ways to create the same dictionary


# Drill 14: Dictionary access methods
# Prompt: Given `student = {"name": "Alice", "grade": 95}`:
# - Access existing key with [] and get()
# - Try to access missing key - show KeyError handling
# - Use get() with default values
# - Use setdefault() to add key with default if missing
# Core concept: All access methods and error handling
# TODO: Demonstrate [], get(), setdefault() and error handling


# Drill 15: Dictionary modification methods
# Prompt: Start with `data = {"x": 1, "y": 2}`. Demonstrate:
# - Direct assignment to add/update
# - update() with dict, pairs, and keywords
# - pop() and popitem() methods
# - del statement and clear()
# Core concept: All modification methods
# TODO: Use every modification method and show results


# Drill 16: Dictionary iteration patterns
# Prompt: Given `grades = {"Alice": 95, "Bob": 87, "Carol": 92}`:
# - Iterate over keys (2 ways)
# - Iterate over values
# - Iterate over key-value pairs
# - Find student with highest grade using iteration
# Core concept: All iteration patterns
# TODO: Show keys(), values(), items() iteration


# Drill 17: Dictionary merging methods
# Prompt: Given three dicts with some overlapping keys:
# `dict1 = {"a": 1, "b": 2}`, `dict2 = {"c": 3, "d": 4}`, `dict3 = {"b": 20, "e": 5}`
# - Merge using update() (modifies original)
# - Merge using unpacking (creates new)
# - Show how conflicts are resolved in each method
# Core concept: Dictionary merging and conflict resolution
# TODO: Use update() and unpacking, show conflict handling


# Drill 18: Dictionary patterns
# Prompt: Implement these common patterns:
# - Count characters in "hello world"
# - Group students by major: [("Alice", "CS"), ("Bob", "Math"), ("Carol", "CS")]
# - Create a simple calculator using dict as switch statement
# Core concept: Counting, grouping, and switch patterns
# TODO: Implement 3 common dictionary patterns


# ===== SETS - COMPREHENSIVE MASTERY (2 DRILLS) =====

# Drill 19: Set operations mastery
# Prompt: Given `set1 = {1, 2, 3, 4}` and `set2 = {3, 4, 5, 6}`:
# - Perform union, intersection, difference, symmetric difference
# - Use both operators (|, &, -, ^) and methods (.union(), .intersection(), etc.)
# - Test subset, superset, and disjoint relationships
# Core concept: All set operations and relationships
# TODO: Use operators and methods for all set operations


# Drill 20: Sets for practical problems
# Prompt: Solve these problems using sets:
# - Remove duplicates from [1, 2, 2, 3, 3, 3, 4] preserving order
# - Find common elements in three lists of numbers
# - Check if user has all required permissions
# - Find missing fields in form data
# Core concept: Practical set applications
# TODO: Use sets to solve real-world uniqueness problems


# ===== INTEGRATION CHALLENGES (2 DRILLS) =====

# Drill 21: Mixed data structures
# Prompt: Create a gradebook system using nested data structures:
# - Students dict with name -> grades list
# - Add grades, calculate averages
# - Find top performer, failing students
# - Group students by grade letter (A, B, C, D, F)
# Core concept: Complex data structure combinations
# TODO: Build system using dicts, lists, and tuples together


# Drill 22: Performance comparison
# Prompt: Create performance tests comparing:
# - List vs set membership testing (1000 items)
# - Dict lookup vs list search for key-value pairs
# - List append vs insert at beginning (100 operations)
# Show why choosing the right data structure matters.
# Core concept: Performance implications of data structure choice
# TODO: Measure and compare performance of different structures


# ===== END OF COMPREHENSIVE DRILLS =====
#
# After completing these 22 drills, you should be fluent in:
# - All creation methods for each data structure
# - All access and modification patterns
# - When to choose each structure for optimal performance
# - How to combine structures for complex data modeling
# - Common patterns and idioms used in professional Python code
#
# This comprehensive foundation prepares you for advanced topics like
# comprehensions, functional programming, and object-oriented programming.
