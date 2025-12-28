"""
Author      : Satish Kumar
Created On  : 2025-12-27

Problem Statement:
     Given an array of integers, determine whether the array is monotonic.
    An array is monotonic if it is either entirely non-increasing
    or entirely non-decreasing.

Approaches:
    1. Using sorting(Not recommended)
    2. Using two traversals
    3. Using Single traversal

    Appraoch 1: Using sorting
        This method checks whether the array remains unchanged
        when sorted in ascending or descending order.
        If either matches, the array is monotonic.

    Approach 2: Using two traversals
        Traverse through the list once to check if the array is increasing
        and 2nd time , check if the array is decreasing.

        incr = all(arr[i] <= arr[i+1] for i in range(n-1)):
        generator checks every adjacent pair; all() is True only if every comparison arr[i] <= arr[i+1] holds.
        decr = all(arr[i] >= arr[i+1] for i in range(n-1)):
        similarly checks arr[i] >= arr[i+1] for every adjacent pair.

    Approach 3: Using single pass
        Traverse the array once while checking both incr and decr
        variable




Edge Cases to be considered:
    | Edge Case             | Expected Behavior |
    |----------------------|------------------|
    | Empty array          | True             |
    | Single element       | True             |
    | All elements equal   | True             |

Time Complexity : O(nlogn) for 1st approach and O(n) for 2nd and 3rd approach

Space Complexity :  O(n) for 1st approach as sorted creates a new list
                    and O(1) for 2nd and 3rd approach

"""
# Approach 1

arr = [1, 2, 2, 4, 5]

incr = False
decr = False

if arr == sorted(arr):
    incr = True

if arr == sorted(arr, reverse=True):
    decr = True

print(incr or decr)

# Approach 2

arr = [6, 5, 4, 4]
n = len(arr)

incr = all(arr[i] <= arr[i+1] for i in range(n-1))
decr = all(arr[i] >= arr[i+1] for i in range(n-1))

print(incr or decr)


# Approach 3

arr = [6,5,5,2]

incr = True
decr = True

for i in range(len(arr)-1):
    if arr[i] >= arr[i+1]:
        incr = False
    if arr[i] <= arr[i+1]:
        decr = False

print(incr or decr)