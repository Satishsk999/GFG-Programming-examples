"""
Author      : Satish Kumar
Created On  : 16/1/2026

Problem Statement : Adding and Subtracting Matrices in Python

Approaches:
    1. Using numpy
    2. Using nested loops

Edge Cases to be considered:
    1. Dimension Mismatch
    2. Jagged matrices
    3. Non-numeric elements

Time Complexity : O(RxC) for both approaches.
    Python loop overhead is significant and much slower than NumPy for large matrices

Space Complexity : O(R × C) auxiliary space

"""

# Approach 1
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Adding matrices
C = np.add(A, B)
print("Addition Result:\n", C)

# Subtracting matrices
C1 = np.subtract(A, B)
print("Subtraction Result:\n", C1)

#Approach 2

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]

print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

add_result = [[0, 0], [0, 0]]
sub_result = [[0, 0], [0, 0]]

# Perform addition and subtraction
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        add_result[i][j] = matrix1[i][j] + matrix2[i][j]
        sub_result[i][j] = matrix1[i][j] - matrix2[i][j]

print("Addition Result:")
for row in add_result:
    print(row)

print("Subtraction Result:")
for row in sub_result:
    print(row)