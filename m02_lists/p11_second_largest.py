"""
Author      : Satish Kumar
Created On  : 29-12-2025

Problem Statement :
    Python Program to Find Second Largest Number in a List
Approaches:
    1. Using for loop
    2. Using sorting

Edge Cases to be considered:

| Approach          | Time Complexity | Space Complexity |
| ----------------- | --------------- | ---------------- |
| Approach 1 (Loop) | **O(n)**        | **O(1)**         |
| Approach 2 (Sort) | **O(n log n)**  | **O(1)**         |


"""
# Approach 1

a = [10, 20, 4, 45, 99]
max1 = max2 = float('-inf')
for n in a:
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2 and n != max1:
        max2 = n
print(max2)

# Apporach 2
a = [10, 20, 4, 45, 99]
a.sort(reverse=True)
print(a[1])
