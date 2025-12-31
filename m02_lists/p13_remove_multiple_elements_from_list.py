"""
Author      : Satish Kumar
Created On  : 31-12-2025

Problem Statement : Remove multiple elements from a list

Approaches:
    1. Using For loop
    2. Using remove() in for loop
    3. Using list comprehension

Edge Cases to be considered:

Time Complexity :

Space Complexity :

"""

# Approach 1
a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]
b = []
for i in a:
    if i not in remove:
        b.append(i)

print(b)
# Approach 2
a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]

for i in a:
    if i in remove:
        a.remove(i)

print(a)

# Approach 3
a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]

c = [i for i in a if i not in remove]
print(c)