"""
Author      : Satish Kumar
Created On  : 26/01/2026

Problem Statement : Given two lists one containing dictionary keys and the other containing corresponding values
                    Create a dictionary that preserves the order of keys as they appear.
For Example:

Input: keys = ["name", "age", "city"], values = ["Harry", 30, "New York"]
Output: {'name': 'Harry', 'age': 30, 'city': 'New York'}

Approaches:
    1. Using zip and Dictionary Constructor
        This method pairs keys and values using zip and converts them into a dictionary in a single step.
    2. Using for Loop with Direct Assignment
        zip(keys, values): Combines keys and values for iteration.
        Each key-value pair is appended to the dictionary using assignment.
    3. Using OrderedDict from collections
        OrderedDict(zip(keys, values)) creates an ordered dictionary preserving the order of keys.

"""

# Approach 1
keys = ["name", "age", "city"]
values = ["Robin", 30, "New York"]
d = dict(zip(keys, values))
print(d)

# Approach 2
keys = ["name", "age", "city"]
values = ["Robin", 30, "New York"]
d = {}
for k, v in zip(keys, values):
    d[k] = v
print(d)

# Approach 3
from collections import OrderedDict
keys = ["name", "age", "city"]
values = ["Robin", 30, "New York"]
d = OrderedDict(zip(keys, values))
print(d)
