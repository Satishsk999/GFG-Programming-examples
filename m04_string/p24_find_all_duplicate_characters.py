"""
Author      : Satish Kumar
Created On  : 24/01/2026

Problem Statement : Given a string, the task is to find all characters that appear more than once in it.

Approaches:
    1. Using collections.Counter
    2. Using Loop with Dictionary
    3. Using set() and count()

"""

# Approach 1
from collections import Counter

s = "GeeksforGeeks"
d = Counter(s)

res = [c for c, cnt in d.items() if cnt > 1]
print(res)

# Approach 2
s = "GeeksforGeeks"
d = {}
res = []

for c in s:
    d[c] = d.get(c, 0) + 1

for c, cnt in d.items():
    if cnt > 1:
        res.append(c)

print(res)

# Approach 3
s = "GeeksforGeeks"
res = []

for c in set(s):
    if s.count(c) > 1:
        res.append(c)

print(res)