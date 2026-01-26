"""
Author      : Satish Kumar
Created On  : 26.01.2026

Problem Statement : Sorting of dictionary by Key

Approaches:
    1. Using sorted() with lambda:
        key=lambda item: item[0] → sorts using keys.
        Dictionary comprehension rebuilds the key-sorted dictionary.
    2. Using OrderedDict:
        sorted(d.items(), key=lambda item: item[0]): sorts by key.
        Loop prints key-value pairs in ascending key order.
    3. Using for loop with sorted():
        sorted(d.items(), key=lambda item: item[0]): sorts by key.
        Loop prints key-value pairs in ascending key order.

"""

# Approach 1
d = {'watermelon': 1, 'apple': 2, 'banana': 3}
asc = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])} # sorts by key
# asc = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])} # sorts by value

print(asc)


# Approach 2
from collections import OrderedDict

d = {'monday': 10, 'tuesday': 9, 'wednesday': 15}
res = OrderedDict(sorted(d.items(), key=lambda item: item[0])) # sorts by key
# res = OrderedDict(sorted(d.items(), key=lambda item: item[1])) # sorts by value
print(res)


# Approach 3
d = {2: 56, 1: 2, 3: 323}
for k, v in sorted(d.items(), key=lambda item: item[0]):
    print((k, v), end=" ")

