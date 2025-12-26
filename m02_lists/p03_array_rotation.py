"""
Author      : Satish Kumar
Created On  : 2025-12-26

Description :
    Rotate the array to the left by 'k' positions.

Approach:
    Using list slicing:
    - arr[k:] → elements from index k to end
    - arr[:k] → first k elements
    - arr[k:] + arr[:k] → rotated array

Edge Cases:
    1. if k > n
        - handled by doing k % len(arr)
    2. if n = 0
        - Handled by using if (n == 0)

Time Complexity : O(N), where N is the no. of elements in the array
    - arr[k:] → copies n - k elements → O(n − k)
    - arr[:k] → copies k elements → O(k)
    - Concatenation (+) → copies all n elements → O(n)

Space Complexity : O(n) (extra space)
    -arr[k:] creates a new list
    -arr[:k] creates another list
    -rotated_arr is a new list of size n

Note: This is not in-place, because a new list is created.
"""

arr = list(map(int, input("Enter the elements: ").split()))

if len(arr) == 0:
    print("Empty array")
else:
    k = int(input("Enter number of positions to rotate: "))
    k = k % len(arr)   # handles k > n

    rotated_arr = arr[k:] + arr[:k]
    print(rotated_arr)
