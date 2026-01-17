"""
Author      : Satish Kumar
Created On  : 17/01/2026

Problem Statement : Transpose a matrix in python

Approaches:
    1. Using loops
    2. Using list comprehension
    3.Using Numpy

"""


# Approach 1
m = [[1, 2], [3, 4], [5, 6]]
rows = len(m)
cols = len(m[0])

res = [[0]*rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        res[j][i] = m[i][j]

print(res)

# Approach 2
m = [[1, 2], [3, 4], [5, 6]]
res = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

print(res)

# Approach 3
import numpy
m = [[1, 2], [3, 4], [5, 6]]
print(numpy.transpose(m))

"""
 This code uses NumPy to create a 2D array m, then prints its transpose using .T.
  The .T attribute swaps rows and columns
"""

import numpy as np
m = np.array([[1, 2], [3, 4], [5, 6]])
print(m.T)