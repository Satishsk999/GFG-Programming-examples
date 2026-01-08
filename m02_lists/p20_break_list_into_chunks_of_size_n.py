"""
Author      : Satish Kumar
Created On  : 8/1/2026

Problem Statement : Break a List into Chunks of Size N
    For ex:-
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        n = 3
        Result: [[1, 2, 3], [4, 5, 6], [7, 8]]

Approaches:
    1. Using List comprehension
    2. Using loops and slicing


"""

# Approach 1
"""
Explanation:

range(0, len(a), n) generates starting indices for each chunk, i.e., 0, 3, 6, etc.
a[i:i + n] slices the list a starting at index i and ending at i + n (the chunk size).
For each index in the range, the list is sliced into chunks of size n.
"""
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3
res = [a[i:i + n] for i in range(0, len(a), n)]
print(res)

# Approach 2
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3
res = []

for i in range(0,len(a),n):
    res.append(a[i:i+n])

print(res)
