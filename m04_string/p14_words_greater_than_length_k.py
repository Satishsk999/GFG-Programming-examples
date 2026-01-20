"""
Author      : Satish Kumar
Created On  : 20.01.2026

Problem Statement :  find all the words which are greater than the given length k.

Approaches:
    1. Using for loop
    2. Using list comprehension
    3. Using lambda function

"""

# Approach 1
str = "hello geeks for geeks is computer science portal"
words = str.split()
print(words)
k = 4
res = []
for w in words:
    if len(w)>k:
        res.append(w)

ans = " ".join(res)
print(ans)

# Approach 2
res = " ".join([w for w in str.split() if len(w) > k])
print(res)

# Approach 3
S = "hello geeks for geeks is computer science portal"
K = 4
s = S.split(" ")
l = list(filter(lambda x: (len(x) > K), s))

print(l)