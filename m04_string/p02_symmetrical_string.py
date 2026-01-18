"""
Author      : Satish Kumar
Created On  : 18/01/2026

Problem Statement : Given a string, the task is to check whether it is symmetrical or not.
    A string is symmetrical if the first half matches the second half
    (ignoring the middle character for odd-length strings).

Approaches:
    1.Using string slicing
    2.Using two pointer technique

"""

# Approach 1
s = "abaaba"
n = len(s)

left = s[:n//2]
right = s[n//2:] if n % 2 == 0 else s[n//2+1:]

if left == right:
    print("Symmetrical")
else:
    print("Not Symmetrical")

# Approach 2
s = "ababa"
n = len(s)

i = 0
j = n // 2

# Skip middle character for odd length
if n % 2 != 0:
    j += 1

is_symmetric = True

while j < n:
    if s[i] != s[j]:
        is_symmetric = False
        break
    i += 1
    j += 1

if is_symmetric:
    print("Symmetrical")
else:
    print("Not Symmetrical")
