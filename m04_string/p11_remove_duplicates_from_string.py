"""
Author      : Satish Kumar
Created On  : 20.01.2026

Problem Statement :The task is to remove all duplicate characters from a string
            while keeping the first occurrence of each character in its original order.
            Input: "geeksforgeeks"
            Output: "geksfor"

Approaches:
    1. Using dict.fromkeys()
        dict.fromkeys(s) creates a dictionary with characters of s as keys, automatically removing duplicates.
        "".join(...) combines the dictionary keys back into a string.
        Efficient because it scans the string once and preserves order.
    2. Using OrderedDict.fromkeys()
        OrderedDict.fromkeys(s) creates an ordered dictionary of unique characters.
        "".join(...) converts the keys into a string in the original order.
    3. Using for Loop with a Set
        seen stores characters that have already appeared.
        The loop adds a character to res only if it hasn’t been seen.

"""

# Approach 1

s = "geeksforgeeks"
res = "".join(dict.fromkeys(s))
print(res)

# Approach 2
from collections import OrderedDict
s = "geeksforgeeks"
res = "".join(OrderedDict.fromkeys(s))
print(res)

# Approach 3
s = "geeksforgeeks"
# print(set(s)) # {'f', 'e', 's', 'o', 'r', 'k', 'g'}
seen = set()
res = ""

for c in s:
    if c not in seen:
        seen.add(c)
        res += c

print(res)
