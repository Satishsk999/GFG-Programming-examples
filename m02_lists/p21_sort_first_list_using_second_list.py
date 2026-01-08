"""
Author      : Satish Kumar
Created On  : 9/1/2026

Problem Statement :
    Given two lists of equal length, where the second list defines the order,
    the task is to reorder the first list according to the sorted order of the second list.
For Example:
    Input:
    List A (to sort): ['x', 'y', 'z', 'w']
    List B (order list): [40, 10, 30, 20]

    Output: ['y', 'w', 'z', 'x']

"""

a = ['a', 'b', 'c', 'd']
b = [3, 1, 4, 2]

"""
Explanation:

zip(b, a): pairs each value in b with corresponding value in a.
sorted(zip(b, a)): sorts pairs using values in b.
list comprehension: extracts sorted values of a.
"""

x = [val for _, val in sorted(zip(b, a))]
print(x)


