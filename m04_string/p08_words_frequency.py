"""
Author      : Satish Kumar
Created On  : 19/01/2026

Problem Statement : Given a string, the task is to find how many times each word appears in it.

Approaches:
    1. Using collections.Counter
        Counter() automatically counts how many times each word appears in a list
        when you split the string into words using .split().
    2. Using dict.get() with a for loop
        for word in s.split() iterates through each word.
        w_freq.get(word, 0) fetches the word’s count (or 0 if it’s new).
        The count is incremented by 1 for every occurrence.
    3. Using List Comprehension with collections.Counter
        [word for word in s.split()] creates a list of all words.
        Counter() then counts each word’s occurrence.

"""

# Approach 1
from collections import Counter
s = "hello world hello everyone"
res = Counter(s.split())
print(res)

# Counter({'hello': 2, 'world': 1, 'everyone': 1}) # Sample output

# Approach 2
s = "hello world hello everyone"
res = {}
for word in s.split():
    res[word] = res.get(word, 0) + 1
print(res)

# {'hello': 2, 'world': 1, 'everyone': 1} # Sample output

# Approach 3
from collections import Counter
s = "hello world hello everyone"
res = Counter([word for word in s.split()])
print(res)

# Counter({'hello': 2, 'world': 1, 'everyone': 1}) # Sample output
