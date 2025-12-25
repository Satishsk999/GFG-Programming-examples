"""
Author      : Satish Kumar
Created On  : 2025-12-25

Description :
    This program finds the largest (maximum) element in an array (list)
    of integers using two different approaches:
        1. Manual traversal of the array
        2. Python built-in max() function

Approach 1 (Manual Traversal) :
    - Assume the first element is the maximum
    - Traverse the array from the second element onward
    - Compare each element with the current maximum
    - Update the maximum when a larger element is found
    - Return the final maximum value

Approach 2 (Built-in Function) :
    - Use Python’s built-in max() function to directly
      determine the largest element in the array

Time Complexity :
    - O(N), where N is the number of elements in the array
      (for both approaches)

Space Complexity :
    - O(1), since only constant extra space is used
"""

def find_max_manual(arr):
    """
    Finds the maximum element in the array using manual traversal.
    """
    res = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > res:
            res = arr[i]
    return res


# -------- Main Program --------

# Input: space-separated integers
arr = list(map(int, input("Enter the list elements: ").split()))

# Approach 1: Manual traversal
result_manual = find_max_manual(arr)
print("Maximum element (Manual Approach):", result_manual)

# Approach 2: Built-in function
result_builtin = max(arr)
print("Maximum element (Built-in Approach):", result_builtin)
