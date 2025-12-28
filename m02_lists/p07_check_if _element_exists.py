"""
Author      : Satish Kumar
Created On  : 28-12-2025

Problem Statement :
    Check if element exists in list in Python

Approaches:
    1. Using in statement
    2. Using any() function
    3. Using count()

Time Complexity :

Space Complexity :

"""

# Approach 1
a = [1, 2, 3, 4, 5]
num = 4
if num in a:
    print(f'Element exists in the list')
else:
    print(f'Element does not exist in the list')

# Approach 2
b = [1, 2, 3, 4, 5, 6]
flag = any(x == 40 for x in b)

if flag:
    print("Element exists in the array")
else:
    print("Element does not exist in the array")

# Approach 3
a = [10, 20, 30, 40, 50]

if a.count(30) > 0:
    print("Element exists in the list")
else:
    print("Element does not exist")
