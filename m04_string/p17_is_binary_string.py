"""
Author      : Satish Kumar
Created On  : 21.01.2026

Problem Statement : Check if a given string is binary string or not

Approaches:
    1. Using all()
        all(c in '01' for c in s): creates a generator that iterates through each character in s.
        Checks if each character belongs to the set {'0','1'}.
        Short-circuit evaluation: all() stops immediately if a character fails the condition, making it fast for large strings.
    2. Using set()
        set(s): converts the string into a set of unique characters.
        issubset({'0', '1'}): checks if all unique characters are either '0' or '1'.
        Efficient for strings with repeated characters as it reduces unnecessary checks.
    3. Using for Loop
        Iterates through each character, checking membership in '01'
        Stops immediately when an invalid character is found using break.
        Simple to understand, but concatenation or repeated membership checks are slower than generator-based all()
"""

# Approach 1
s = "101010000111"
if all(c in '01' for c in s):
    print("Yes")
else:
    print("No")

# Approach 2
s = "101010000111"
if set(s).issubset({'0', '1'}):
    print("Yes")
else:
    print("No")

# Approach 3
s = "101010000111"
for char in s:
    if char not in '01':    # checks whether a character is not one of '0' or '1'
        print("No")
        break
else:
    print("Yes")
