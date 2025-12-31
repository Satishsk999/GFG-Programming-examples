"""
Author      : Satish Kumar
Created On  : 31-12-2025

Problem Statement : Remove empty sublists from list

Approaches:
    1.Using for loop
    2.Using list comprehension

"""

# Approach 1

a = [[1, 2], [], [3, 4], [], [5]]
res = []
for b in a:
    if b:
        res.append(b)
print(res)

# Approach 2
a = [[1, 2], [], [3, 4], [], [5]]
res = [i for i in a if i]
print(res)

