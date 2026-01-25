"""
Author      : Satish Kumar
Created On  : 25/01/2026

Problem Statement : Ways to sort list of dictionaries by values in Python – Using itemgetter

"""

# Approach 1 : Sort by a Single Key
from operator import itemgetter

d = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil", "age": 19}
]
print("Sorted by age: ",sorted(d, key=itemgetter('age')))

# Approach 2 : Sort by Multiple Keys
from operator import itemgetter
d = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil", "age": 19}
]
print("Sorted by age and name: ",sorted(d, key=itemgetter('age', 'name')))

# Approach 3 : Sort in Descending Order
from operator import itemgetter
d = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil", "age": 19}
]
print("Sorted by age (descending): ", sorted(d, key=itemgetter('age'), reverse=True))