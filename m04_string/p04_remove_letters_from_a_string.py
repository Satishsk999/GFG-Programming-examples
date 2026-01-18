"""
Author      : Satish Kumar
Created On  : 18/01/2026

Problem Statement : Given a string, the task is to remove one or more specific letters from it
For example:
Input:  "hello world"
Remove: "l"
Output: "heo word"

Approaches:
    1.Using replace()
    2.Using list comprehension

Time and Space Complexity : O(n) for both approaches

"""

# Approach 1
s = "hello world"
s = s.replace("l", "")
print(s)

# Approach 2
s = "hello world"
p = ''.join([c for c in s if c != "o"])
print(p)
