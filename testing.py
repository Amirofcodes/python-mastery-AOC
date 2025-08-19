records = [
    ("Alice", 88),
    ("Bob", 95),
    ("Cara", 72),
    ("Dan", 100),
    ("Eli", 90),
]


min_score = min(record[1] for record in records)
print(min_score)

# # Method 1: Using a list comprehension (most Pythonic)
# sum_of_scores = sum(score for name, score in records)
# print(f"Sum using list comprehension: {sum_of_scores}")

# # Method 2: Using indexing to access the second element of each tuple
# sum_of_scores_v2 = sum(record[1] for record in records)
# print(f"Sum using indexing: {sum_of_scores_v2}")

# # Method 3: Using map() function
# sum_of_scores_v3 = sum(map(lambda record: record[1], records))
# print(f"Sum using map: {sum_of_scores_v3}")

# # Method 4: Traditional for loop (more verbose but clear)
# total = 0
# for name, score in records:
#     total += score
# print(f"Sum using for loop: {total}")
