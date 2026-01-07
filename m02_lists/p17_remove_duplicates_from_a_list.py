"""
Author      : Satish Kumar
Created On  : 7/1/2026

Problem Statement : Program to Print Duplicates from a List of Integers in Python

Approaches:
    1. Using Collections.Counter
    2. Using Set
    3. Using A Dictionary
    4. Using Nested loop

Approach 1:
    a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
    Counter(a) counts how many times each number appears.
    It behaves like a dictionary:
        key → element, value → frequency
        dict_items([(1, 2), (2, 2), (3, 1), (4, 1), (5, 2), (6, 1)])
    List comprehension extracts only the elements with frequency greater than 1.

Approach 2:
    A set in Python stores only unique elements.
    By tracking seen elements in a set, duplicates can be identified efficiently.

    s keeps track of the elements that have already appeared.
    If an element n is already in s, it’s added to dup as a duplicate.

Approach 3:
    A dictionary can be used to count the occurrences of each element.
    Any element with a count greater than 1 is a duplicate.

Approach 4:
    This method compares every element with all others to find duplicates.
    It’s easy to understand but less efficient for larger lists.

Edge Cases to be considered:

Time and Space Complexity :

| Approach | Technique    | Time  | Space | Best Use Case            |
| -------- | ------------ | ----- | ----- | ------------------------ |
| 1        | Counter      | O(N)  | O(K)  | Cleanest & Pythonic      |
| 2        | Set tracking | O(N)  | O(N)  | Preserve duplicate order |
| 3        | Dictionary   | O(N)  | O(K)  | Interview-friendly logic |
| 4        | Brute force  | O(N²) | O(D)  | No hashing allowed       |


"""

# Approach 1
from collections import Counter

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
count = Counter(a)
print(count.items()) # dict_items([(1, 2), (2, 2), (3, 1), (4, 1), (5, 2), (6, 1)])
res = [num for num, freq in count.items() if freq > 1]

print(res)

# Approach 2
b = [1, 2, 3, 1, 2, 4, 5, 6, 5]
s = set()
dup = []

for i in b:
    if i in s:
        dup.append(i)
    else:
        s.add(i)

print(dup)

# Approach 3
c = [1, 2, 3, 1, 2, 4, 5, 6, 5]
cnt = {}
for i in c:
    cnt[i] = cnt.get(i,0) + 1 # cnt.get(n, 0) + 1: updates each element’s frequency.

duplicates = [num for num,freq in cnt.items() if freq > 1]
print(duplicates)

# Approach 4

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
dupl = []

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j] and a[i] not in dupl:
            dupl.append(a[i])

print(dupl)