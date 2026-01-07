"""
Author      : Satish Kumar
Created On  : 7/1/2026

Problem Statement :
    Given a list of numbers, the task is to find the cumulative sum (also known as the running total)
    where each element in the output represents the sum of all elements up to that position in the original list.
    Example:
        Input: [1, 2, 3, 4]
        Output: [1, 3, 6, 10]

Approaches:
    1. Using itertools.accumulate()
         itertools.accumulate(l) returns an iterator
         that generates the running (cumulative) sum of the list elements.

    2. Using a loop
        The traditional way to compute cumulative sums is by using a simple for loop and maintaining a running total.
    3. Using list comprehension
        [sum(l[:i+1]) for i in range(len(l))]: For each index i, sum all elements from start up to i.
        Creates a list of cumulative sums in one line.


"""

# Approach 1
import itertools

l = [1, 2, 3, 4]
res = list(itertools.accumulate(l))
print(res)

# Approach 2
l = [1, 2, 3, 4]
arr = []
total = 0

for i in l:
    total += i
    arr.append(total)

print(res)

# Approach 3
l = [1, 2, 3, 4]
res_arr = [sum(l[:i+1]) for i in range(len(l))]

print(res_arr)
