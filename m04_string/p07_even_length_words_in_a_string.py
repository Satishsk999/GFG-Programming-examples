"""
Author      : Satish Kumar
Created On  : 19/01/2026

Problem Statement : Given a string, the task is to print only the words whose lengths are even.

Approaches:
    1. Using list comprehension

"""

s = "This is a python language"
words = s.split()
even_words = [w for w in words if len(w)%2 == 0 ]
result = ' '.join(even_words)
print(result)
