"""
Author      : Satish Kumar
Created On  : 18/01/2026

Problem Statement : Given two strings, check whether a substring is in the given string.

Approaches:
    1. Using in
        The in operator in Python checks if one string occurs within another.
        It evaluates to True if the substring is present in the main string, otherwise False.
    2. Using operator.contains()
         operator.contains(s, s2) returns True if s2 is found within s, otherwise False.
    3. Using find()
        The find() method scans the string to locate a specific substring.
        It returns the starting index of the first occurrence if found; otherwise, it returns -1.
    4. Using index()
        The index() method works similarly to find() but
        raises a ValueError if the substring does not exist in the string.
        It is useful when you need the exact position of the substring and want an explicit error if it’s missing.

"""

# Approach 1
s = "Geeks welcome to the Geek Kingdom!"
s2 = "Geek"

if s2 in s:
    print("Substring found")
else:
    print("Substring not found")

# Approach 2
import operator as op

s = "Geeks welcome to the Geek Kingdom!"
s2 = "Geek"

if op.contains(s, s2):
    print("Substring found")
else:
    print("Substring not found")

# Approach 3
if s.find(s2)!= -1:
    print("Substring found")
else:
    print("Substring not found")


# Approach 4

s = "Geeks welcome to the Geek Kingdom!"
print(s.index("Kingdom"))