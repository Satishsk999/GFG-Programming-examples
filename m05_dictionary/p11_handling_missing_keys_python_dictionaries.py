"""
Author      : Satish Kumar
Created On  : 27/01/2026

Problem Statement : Handling missing keys in Python dictionaries

Approaches:
    1. Using defaultdict
        defaultdict from the collections module is highly efficient and avoids repeatedly writing checks.
        It allows you to set a default value for missing keys at the time of dictionary creation.
        defaultdict(lambda: 'Key Not found'): creates a dictionary that returns a default value for missing keys instead of raising KeyError.
        dic['a'] = 1 and dic['b'] = 2 add existing keys.
    2. Using get() method
        get(): retrieves the value for a given key.
        If the key exists, it returns its value, if not, it returns the default message provided.
    3. Using setdefault() Method
        setdefault() method works like get(), but if the key is missing, it creates the key with a default value.
    4. Using try-except Block
        try-except block handles missing keys safely.
        Inside try, it tries to access dictionary values.
        If a key doesn’t exist, a KeyError is raised and caught by except, which prints 'Not Found'.
    5. Using if key in dict
        code checks if a key exists in the dictionary using the "in" operator.
        if the key is found, its value is printed; otherwise, a custom message is shown.

"""

# Approach 1
from collections import defaultdict
d = defaultdict(lambda : 'Key not found')
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['v'])

# Approach 2
d = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}
print(d.get('India','Not foundddd'))
print(d.get('Inia','Not found'))

# Approach 3
dic = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}
dic.setdefault('Japan', 'Not Present')
print(dic) # {'India': '0091', 'Australia': '0025', 'Nepal': '00977', 'Japan': 'Not Present'}
print(dic['India'])
print(dic['Japan'])

# Approach 4
dic = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}
try:
    print(dic['India'])
    print(dic['USA'])
except KeyError:
    print('Not Found')

# Approach 5
dic = {'a': 5, 'c': 8, 'e': 2}
if 'q' in dic:
    print(dic['q'])
else:
    print("Key not found")

