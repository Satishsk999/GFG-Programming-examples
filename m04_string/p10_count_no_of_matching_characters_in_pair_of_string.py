"""
Author      : Satish Kumar
Created On  : 20/01/2026

Problem Statement : Given two strings, the task is to count the number of characters that appear in both strings,
                    ignoring case and duplicates if needed.

Approaches:
    1.Using a For Loop
        a = s1.lower(): Convert strings to lowercase for case-insensitive comparison.
        set(a): Get unique characters from s1
        for c in set(a): if c in b: Check if each unique character exists in s2.
        res += 1: Count each matching character.
    2. Using List Comprehension
        set(...): Ensures only unique characters are considered.
        List comprehension collects characters present in both strings.
    3. Using Set Intersection
        s1.lower(), s2.lower(): Converts both strings to lowercase for case-insensitive comparison.
        set(...): Removes duplicates and allows fast comparison.
        & (intersection): Finds characters common to both sets.
        len(): Counts the number of common characters.

"""

# Approach 1
s1 = "apple"
s2 = "grape"

a = s1.lower()
b = s2.lower()
res = 0
# print(set(a)) {'e', 'p', 'l', 'a'}

for ch in set(a):
    if ch in b:
        res += 1
print(res)

# Approach 2
s1 = "apple"
s2 = "grape"
res = 0
res = len([s for s in set(s1.lower()) if s in set(s2.lower())])
print(res)

# Approach 3
s1 = "apple"
s2 = "grape"

res = len(set(s1.lower()) & set(s2.lower()))
print(res)

