"""
Author      : Satish Kumar
Created On  : 8/1/2026

Problem Statement : Sum of Number Digits in List in Python

Approaches:
    1. Using List comprehension
    2. Using Loops

"""

# Approach 1

a = [123,456]
"""
str(val): converts each number to a string for digit iteration.
int(digit): converts each character back to an integer.
sum(): function calculates the total of digits for each number.
"""


res = [sum(int(digit) for digit in str(val)) for val in a]
print(res)

# Approach 2
res = []
for i in a:
    s = 0
    while i > 0:
        s += i%10
        i = i//10
    res.append(s)

print(res)

