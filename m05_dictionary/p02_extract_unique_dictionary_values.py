"""
Author      : Satish Kumar
Created On  : 25.01.2026

Problem Statement : Extract unique values from the values of a dictionary in Python.

Approaches:
    1. Using set() + sum() :- One-line method ideal for small-to-medium datasets.
        data.values(): fetches all value lists.
        sum(..., []): flattens nested lists by concatenation.
        set(): removes duplicate elements.
        list(): converts the set into a list
    2. Using set comprehension + values() + sorted():
        {x for v in data.values() for x in v}: nested set comprehension flattens and removes duplicates.
        sorted(): returns a sorted list of unique values.
    3. Using Counter() + append() + sort()
        [x for v in d.values() for x in v]: flattens all values.
        Counter(vals): counts frequency of each element.
        freq.keys(): retrieves unique elements.

"""

# Approach 1
d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}
res = list(set(sum(d.values(), [])))
print(res)

# Approach 2
d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}
res = list(sorted({ele for val in d.values() for ele in val}))
print(res)


# Approach 3
from collections import Counter

d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}

vals = [x for v in d.values() for x in v]
freq = Counter(vals)
res = sorted(list(freq.keys()))
print(res)