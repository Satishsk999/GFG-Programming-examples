"""
Author      : Satish Kumar
Created On  : 26/01/2026

Problem Statement : Ways to sort list of dictionaries by values - Using lambda function

"""

# Approach 1
dic = [
    {"name": "Harry", "age": 20},
    {"name": "Robin", "age": 20},
    {"name": "Kevin", "age": 19}
]

print("Sorted by age:")
print(sorted(dic, key=lambda x: x['age']))
# Approach 2

print("\nSorted by age and name:")
print(sorted(dic, key=lambda x: (x['age'], x['name'])))

# Approach 3
print("\nSorted by age (descending):")
print(sorted(dic, key=lambda x: x['age'], reverse=True))
