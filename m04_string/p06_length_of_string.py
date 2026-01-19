"""
Author      : Satish Kumar
Created On  : 19/01/2026

Problem Statement :Given a string, the task is to find its length

Approaches:
    1. Using len() function
    2. Using for loop and in operator
    3. Using enumerate function
        enumerate(a) returns both index (i) and value (ch) for each iteration.
        Here, we count how many times the loop runs, which equals the string length.
    4. Using str.count()
        count() method is used to count occurrence of given substring.
        Here, we are using count method to count the spaces between characters,
        which is always one more than number of character in given string
        (hence, we are excluding this with -1)

"""

# Approach 1
a = "geeks"
print(len(a))

# Approach 2
a = "Python"
count = 0
for char in a:
    count += 1
print(count)

# Approach 3
a = "Python"
l = 0

for i, ch in enumerate(a):
    l += 1
print(l)

# Approach 4
a = "Hello"
l = a.count("") - 1
print(l)