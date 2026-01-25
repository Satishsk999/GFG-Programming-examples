"""
Author      : Satish Kumar
Created On  : 25.01.2026

Problem Statement : Given two dictionaries,
the task is to merge them into a single dictionary that contains all key-value pairs.

Approaches:
    1. Using | Operator
        | operator combines d1 and d2 into d1 new dictionary d3.
        Duplicate keys are handled by keeping the value from the dictionary on the right (d2).
    2. Using Dictionary Unpacking (**)
        **d1 and **d2 unpack the key-value pairs of d1 and d2 into the new dictionary d3.
        Keys from d2 overwrite duplicates from d1.
    3. Using update()
        d1.update(d2) adds all key-value pairs from d2 to d1.
        If a key exists in both d1 and d2 (e.g., 'y'), the value from d2 (3) replaces the value in d1 (2).
    4. Using loop
        d1.copy() creates a shallow copy of d1 to preserve the original dictionary.
        for loop iterates through each key-value pair in d2 and adds or updates it in d3.

"""

# Approach 1
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1 | d2
print(d3)

# Approach 2
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = {**d1, **d2}
print(d3)

# Approach 3
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}
d1.update(d2)
print(d1)

# Approach 4
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1.copy()
for key, value in d2.items():
    d3[key] = value

print(d3)