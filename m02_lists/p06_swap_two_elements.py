"""
Author      : Satish Kumar
Created On  : 28-12-2025

Problem Statement :
    Python program to swap two elements in a list

Approaches:
    1. Using temp variable
    2. Using XOR operator
    3. Using Multiple Assignment

Edge Cases to be considered:
    - Index out of range
    - Same index swap
    - Non-integer elements

Time Complexity:
O(1)

Space Complexity:
O(1)

"""
# Approach 1
arr = [1, 3, 2, 4, 5]

temp = arr[1]
arr[1] = arr[2]
arr[2] = temp

print(arr)

# Approach 2 (Technically works but bad practice in Python)

arr = [1, 3, 2, 4, 5]

arr[1] = arr[1] ^ arr[2]
arr[2] = arr[1] ^ arr[2]
arr[1] = arr[1] ^ arr[2]

print(arr)

# Approach 3(recommended solution)

arr = [1, 3, 2, 4, 5]

arr[1], arr[2] = arr[2], arr[1]

print(arr)
