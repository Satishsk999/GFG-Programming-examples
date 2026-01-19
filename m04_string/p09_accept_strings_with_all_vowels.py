"""
Author      : Satish Kumar
Created On  : 19/01/2026

Problem Statement : The task is to check whether a given string contains all the vowels a, e, i, o, u.

Approaches:
    1. Using set() with issubset()
        set('aeiou') creates a set of vowels.
        set(s.lower()) converts the string to lowercase and stores unique characters.
        issubset() checks if all vowels are present in the string.
    2. Using all()
        s.lower() ensures the check is case-insensitive.
        all() returns True only if every vowel in v is found in the string.
        Generator expression (ch in s.lower() for ch in v) efficiently iterates through vowels.
    3. Using a loop
        found stores vowels detected in the string.
        Loop iterates over each character and adds it to found if it’s a vowel.
        Breaks early if all five vowels are found; otherwise prints False after loop.


"""
# Approach 1
s = "geeksforgeeks"
v = set('aeiou')
if v.issubset(set(s.lower())):
    print("True")
else:
    print("False")

# Approach 2
s = "Geeksforgeeks"
v = 'aeiou'
if all(i in s.lower() for i in v):
    print("True")
else:
    print("False")

# Approach 3
s = "education"
v = 'aeiou'
a = set()
for char in s.lower():
    if char in v:
        a.add(char)
    if len(a) == 5:
        print("True")
        break
else:
    print("False")