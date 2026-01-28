"""
Author      : Satish Kumar
Created On  : 28.01.2026

Problem Statement : Given a list of tuples, the task is to convert it into a dictionary.

Approaches:
    1. Using dict()
    2. Using Dictionary Comprehension
    3. Using for loop

"""

# Approach 1
a = [("a", 1), ("b", 2), ("c", 3)]
res = dict(a)
print(res)

# Approach 2
a = [("a", 1), ("b", 2), ("c", 3)]
res = {key: value for key, value in a}
print(res)

# Approach 3
a = [("a", 1), ("b", 2), ("c", 3)]
res = {}
for key, value in a:
    res[key] = value

print(res)

