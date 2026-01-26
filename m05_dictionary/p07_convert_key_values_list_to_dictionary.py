"""
Author      : Satish Kumar
Created On  : 26/01/2026

Problem Statement : Given a list of key-value pairs, the task is to convert it into a flat dictionary.

Approaches:
    1. Using dict()
        dict() constructor converts a list of key-value pairs into a dictionary by using
        each sublist's first element as a key and the second element as a value.
    2. Using dictionary comprehension
        Dictionary comprehension {key: value for key, value in a}
        iterates through the list a, unpacking each tuple into key and value.
    3. Using a loop
        For loop iterates through each tuple in the list 'a',
        extracting the key and value, and then adds them to a dictionary

"""

# Approach 1
a = [("name", "Emma"), ("age", 25), ("city", "New York")]
res = dict(a)
print(res)
# Approach 2
a = [("name", "Emma"), ("age", 25), ("city", "New York")]
res = {key:value for key,value in a}
print(res)
# Approach 3
a = [("name", "Emma"), ("age", 25), ("city", "New York")]
b = {}
for key, value in a:
    b[key] = value

print(b)