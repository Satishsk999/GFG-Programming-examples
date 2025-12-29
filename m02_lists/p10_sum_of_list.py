"""
Author      : Satish Kumar
Created On  : 29-12-2025

Problem Statement : Find sum of elements in List

Approaches:
    1. Using sum()
    2. Using for loop
    2. Using reduce()

Edge Cases to be considered:
    1.reduce() → raises TypeError when the list is empty
    2. all 3 approaches raise typeerror for non-integer elements

Time Complexity : O(n) for all 3 approaches

Space Complexity : O(1) for all 3 approaches

"""

from functools import reduce

# Approach 1
a = [1, 2, 3, 4, 5]
res = sum(a)
print(res)

# Approach 2
sum = 0
for i in a:
    sum += i

print(sum)

# Approach 3
s = 0
s = reduce(lambda x, y: x + y, a)
print(s)