"""
Author      : Satish Kumar
Created On  : 21.01.2026

Problem Statement : Given a string and an index i,
                remove the character at the i-th position and return the resulting string

Approaches:
    1. Using string slicing
    2. Using join with list comprehension
    3. Using replace() with slicing
    4. Using for loop

"""

# Approach 1
s = "PythonProgramming"
i = 6
res = s[:i] + s[i+1:]
print(res)

# Approach 2
s = "PythonProgramming"
i = 6
res = ''.join([s[j] for j in range(len(s)) if j != i])
print(res)

# Approach 3
s = "PythonProgramming"
i = 3
res = s[:i] + s[i:].replace(s[i], '', 1)
print(res)

# Approach 4
s = "PythonProgramming"
i = 6
res = ""
for j in range(len(s)):
    if j != i:
        res += s[j]
print(res)
