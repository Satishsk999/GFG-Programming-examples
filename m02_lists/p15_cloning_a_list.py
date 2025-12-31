"""
Author      : Satish Kumar
Created On  : 31-12-2025

Problem Statement : Given a list of elements, the task is to create a copy of it.

Approaches:
    1. Using copy()
        copy() method is a built-in method in Python that creates a shallow copy of a list.
        This method is simple and highly efficient for cloning a list.
    2. Using List slicing
        This method creates a new list by slicing all elements from the original. It’s concise and performs well.
    3. Using list()
       This method uses Python’s list() constructor to generate a copy of the original list.
    4.Using copy.deepcopy() for nested list
        For nested lists, a deep copy is required to ensure that changes to the cloned list do not affect the original.
        The copy module provides the deepcopy() method for this purpose.

"""

# Approach 1
a = [1, 2, 3, 4, 5]
b = a.copy()
print(b)

# Approach 2
a = [1, 2, 3, 4, 5]
b = a[:]
print(b)

# Approach 3
a = [1, 2, 3, 4, 5]
b = list(a)
print(b)

# Approach 4
import copy
a = [[1, 2], [3, 4], [5, 6]]
b = copy.deepcopy(a)
print(b)
