"""
Author      : Satish Kumar
Created On  : 10/1/2026

Problem Statement : Take matrix input from user

"""
# Approach 1 for taking input of matrix with fixed rows and columns

rows = int(input("Enter no. of rows: "))
columns = int(input("Enter no. of columns: "))
matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input()))
    matrix.append(row)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end=" ")
    print()

# Approach 2 for taking input of matrix where length of column is variable

rows = int(input("Enter no. of rows: "))
mat = []
for _ in range(rows):
    row = list(map(int,input().split()))
    mat.append(row)

print(mat)

for row in mat:
    for element in row:
        print(element,end=" ")
    print()