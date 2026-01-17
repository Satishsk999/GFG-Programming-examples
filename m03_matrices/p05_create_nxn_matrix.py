"""
Author      : Satish Kumar
Created On  : 17/01/2026

Problem Statement : Create an n × n matrix in Python

Approaches:
    1. Using list comprehension
    2. Using nested loops

"""

# Approach 1
n = 4
p = [[0 for _ in range(n)] for _ in range(n)]
print(p)

# Approach 2
n = 4
m =[]
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    m.append(row)

print(m)
