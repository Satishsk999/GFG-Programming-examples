"""
Author      : Satish Kumar
Created On  : 18/01/2026

Problem Statement : Check if a string is palindrome or not

Approaches:
    1. Using two pointer technique
    2. Using string slicing
    3. Using reversed() + join()

"""
# Approach 1

s = "malayalam"
low = 0
high = len(s)-1
while low < high :
    if s[low] != s[high]:
        print("Not Palindrome")
        break
    low += 1
    high -= 1
else:
    print("Yes, it is Palindrome")

# Approach 2
if s == s[::-1]:
    print("Yes, it is palindrome")
else:
    print("Not palindrome")

# Approach 3
res = ''.join(reversed(s))
if s == res:
    print("Yes, it is palindrome")
else:
    print("Not palindrome")
