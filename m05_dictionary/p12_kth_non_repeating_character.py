"""
Author      : Satish Kumar
Created On  : 27/01/2026

Problem Statement : Given a string 's' and an integer 'k', the task is to find the K’th non-repeating character in the string.
                    A non-repeating character is one that appears exactly once.
Example:
Input: "geeksforgeeks"
k=3

Output: "r"
Explanation: In "geeksforgeeks", the characters that appear only once are f, o, and r.
The third non-repeating character is "r".

Approaches:
    1. Using collections.Counter
        Counter(s): creates a dictionary of individual characters as keys and their frequencies as values ({'e': 4, 'g': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}).
        [ch for ch in s if c[ch] == 1]: collects characters that appear only once 'c'.
        res[k - 1] if k <= len(res) else None: prints the k'th element of "res" if k is less than the length of "res", else it prints none.
    2. Using OrderedDict
        OrderedDict(): Stores characters while preserving their order of appearance.
        freq.get(ch, 0) + 1: Counts how many times each character appears.
        [ch for ch, cnt in freq.items() if cnt == 1]: Collects only the non-repeating characters.
    3. Using Regular Dictionary
        if freq[ch] == 1: Checks for characters that appear only once.
        res.append(ch): Stores non-repeating characters in order.
    4. Using List Comprehension
"""

# Approach 1
from collections import Counter
s = "geeksforgeeks"
k = 3

c = Counter(s)
res = [ch for ch in s if c[ch] == 1]

print(res[k - 1] if k <= len(res) else None)

# Approach 2
from collections import OrderedDict

s = "geeksforgeeks"
k = 3

freq = OrderedDict()
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

res = [ch for ch, cnt in freq.items() if cnt == 1]
print(res[k - 1] if k <= len(res) else None)

# Approach 3
s = "geeksforgeeks"
k = 3

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

res = []
for ch in s:
    if freq[ch] == 1:
        res.append(ch)

print(res[k - 1] if k <= len(res) else None)

# Approach 4
s = "geeksforgeeks"
k = 3

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

res = [ch for ch in s if freq[ch] == 1]
print(res[k - 1] if k <= len(res) else None)

