"""
Author      : Satish Kumar
Created On  : 2025-12-24

Description :
    This program calculates the sum of all elements in a given
    array (list) of integers.

Approach :
    - Initialize a variable to store the sum
    - Traverse each element in the array
    - Add each element to the sum variable
    - Return the final sum

Time Complexity :
    - O(N), where N is the number of elements in the array

Space Complexity :
    - O(1), since no extra space is used apart from a variable
"""


def array_sum(arr):
    total = 0

    for num in arr:
        total += num

    return total


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(array_sum(numbers))

    # 2nd approach
    """
    Python provides a built-in sum() function to calculate the sum
     of elements in a list, tuple or set.
    """
    result = sum(numbers)
    print('sum is :',result)
