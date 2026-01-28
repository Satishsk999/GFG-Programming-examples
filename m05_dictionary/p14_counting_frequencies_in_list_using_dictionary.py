"""
Author      : Satish Kumar
Created On  : 28.01.2026

Problem Statement : Counting the Frequencies in a List Using Dictionary

Approaches:
    1. Using Counter from collections
    2. Using defaultdict
    3. Using get() Method
    4. Using Dictionary and for loop

"""

# Approach 1
from collections import Counter
a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
freq = Counter(a)
print(dict(freq))

# Approach 2
from collections import defaultdict

a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
freq = defaultdict(int)

for item in a:
    freq[item] += 1

print(dict(freq))

# Approach 3
a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

freq = {}
for item in a:
    freq[item] = freq.get(item, 0) + 1

print(freq)

# Approach 4
a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

freq = {}
for item in a:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)
