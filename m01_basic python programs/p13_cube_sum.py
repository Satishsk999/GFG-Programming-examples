"""
Author      : Satish Kumar
Created On  : 1/1/2026

Problem Statement : Python Program for cube sum of first n natural numbers

Approaches:
    1. using formula
    2. using brute force

"""


# Approach 1

n = 5
res = ((n * (n + 1)) // 2) ** 2
print(res)

# Approach 2

n = 5
sum = 0

for i in range(1, n + 1):
    res += i ** 3

print(res)