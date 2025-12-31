"""
Author      : Satish Kumar
Created On  : 31-12-2025

Problem Statement : Print even numbers in a list

Approaches:
    1.Using loop
      - Using a traditional for loop is the most straightforward method,
        but it is generally less efficient and more verbose compared to other methods.

    2.Using list comprehension
        - List comprehensions is an efficient way to filter elements from a list.
        They are generally considered more Pythonic and faster than traditional loops.

    2.Using bitwise AND operator
        - It works by performing a bitwise AND operation with 1,which will return 0 for even numbers and 1 for odd numbers.

        expression val & 1 == 0 uses the bitwise AND operator to check if the least significant bit of a number is 0.
        Even numbers have their least significant bit as 0, so the condition evaluates to True for even numbers.

"""

# Approach 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in a:
    if i % 2 == 0:
        print(i, end=" ")

print()

# Approach 2
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr = [val for val in b if val % 2 == 0]
print(arr)

# Approach 3

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [val for val in c if val & 1 == 0]
print(res)
