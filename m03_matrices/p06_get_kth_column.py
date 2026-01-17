"""
Author      : Satish Kumar
Created On  : 17/10/2026

Problem Statement : Extract the Kth column from a matrix
Example:
Matrix = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
The 2nd column (K=2, 0-indexed) would be [6, 10, 5].

Approaches:
    1. Using loops
    2. Using list comprehension
    3. Using zip

"""

# Approach 1
k = 2
res = []
mat = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]

for row in mat:
    res.append(row[k])

print(res)

# Approach 2
mat = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
result = [row[k] for row in mat]
print(result)

# Approach 3
"""
Transposes the matrix with zip(*) and selects the Kth row of the transposed matrix.
This method is readable but slightly slower due to creating intermediate tuples.
Explanation:

*mat: Unpacks the matrix rows as separate arguments.
zip(*mat): Transposes the matrix, converting rows into columns.
[K]: Selects the Kth column from the transposed result.
list(): Converts the resulting tuple of elements into a list.
"""
mat = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
K = 2

res = list(zip(*mat))[K]
print( res)