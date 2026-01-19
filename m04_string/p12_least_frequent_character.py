"""
Author      : Satish Kumar
Created On  : 20.01.2026

Problem Statement :Given a string, the task is to identify the character that appears the least number of times.

Approaches:
    1. Using collections.Counter and min
        Counter(s) creates a dictionary where each character in the string is a key and the value is its frequency.
        min(freq, key=freq.get) finds the character with the lowest frequency.
    2. Using Dictionary
        d.get(char, 0) retrieves the current frequency of char, defaulting to 0 if the character is not found.
        min(d, key=d.get) finds the character with the lowest frequency in the dictionary d.
    3. Using str.count()
        count() function counts the occurrences of each character and min() is used to identify the character with the lowest frequency.
        This approach is straightforward but becomes inefficient for larger strings due to its quadratic time complexity.
Edge Cases to be considered:

Time Complexity :

Space Complexity :

"""

# Approach 1
from collections import Counter
s = "GeeksforGeeks"
freq = Counter(s)
# print(freq) Counter({'e': 4, 'G': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1})
res = min(freq,key=freq.get)
print(str(res))

# Approach 2
s = "GeeksforGeeks"
d = {}
for char in s:
    d[char] = d.get(char, 0) + 1

res = min(d, key=d.get)
print(str(res))

# Approach 3
s = "GeeksforGeeks"
res = min(s, key=lambda char: s.count(char))
print(str(res))
