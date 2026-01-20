"""
Author      : Satish Kumar
Created On  : 20.01.2026

Problem Statement : The task is to find the character in a string that appears the most number of times.

Approaches:
    1. Using Counter():
        Counter(s) creates a dictionary where each character is a key and its frequency is the value.
        max(frequency, key=frequency.get) finds the key (character) with the highest value (frequency).
    2. Using set + Counter:
        set(s) selects unique characters.
        Counter(s).get provides the frequency of each character.
        max(..., key=...) finds the character with the highest frequency.
    3. Using dict.get() with max():
        freq.get(char, 0) + 1 increments the count for each character.
        max(freq, key=freq.get) returns the character with the maximum count.
    4. Using str.count()
        set(s) avoids duplicate calculations.
        s.count(char) counts each character's occurrences.
        The loop updates max_count and max_char whenever a higher frequency is found.
"""

# Approach 1
from collections import Counter
s = "hello world"
freq = Counter(s)
res = max(freq, key= freq.get)
print(res)

# Approach 2
"""
This method scans only unique characters instead of the entire string, 
improving performance for strings with repeated characters
"""

from collections import Counter
s = "hello world"
max_char = max(set(s), key=Counter(s).get)
print(max_char)

# Approach 3
s = "hello world"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

max_char = max(freq, key=freq.get)
print(max_char)

# Approach 4
s = "hello world"
max_char = ''
max_count = 0

for char in set(s):
    count = s.count(char)
    if count > max_count:
        max_count = count
        max_char = char

print(max_char)
