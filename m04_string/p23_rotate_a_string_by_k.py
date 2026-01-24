"""
Author      : Satish Kumar
Created On  : 23.01.2026

Problem Statement : Given a string of length n, rotate the string either,
Left (anticlockwise) by d positions or Right (clockwise) by d positions where 0 ≤ d ≤ n.
For Example:
    Input: "GeeksforGeeks", d=2
    Output: Left Rotation: "eksforGeeksGe"
            Right Rotation:  "ksGeeksforGee"

Approaches:
    1. Using String Slicing
    2. Using for loop

"""

# Approach 1
s = "GeeksforGeeks"
d = 2

left = s[d:] + s[:d]
right = s[-d:] + s[:-d]

print("Left rotation:", left)
print("Right rotation:", right)

# Approach 2
s = "GeeksforGeeks"
d = 2
n = len(s)

# Left Rotation
left = ""
for i in range(d,n):
    left+= s[i]
for i in range(d):
    left+= s[i]

# Right Rotation
right = ""
for i in range(n - d, n):
    right += s[i]
for i in range(n - d):
    right += s[i]

print("Left Rotation:", left)
print("Right Rotation:", right)
