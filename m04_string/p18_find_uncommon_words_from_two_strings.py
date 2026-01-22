"""
Author      : Satish Kumar
Created On  : 22.01.2026

Problem Statement : Extract words that appear in only one of two given strings while ignoring common words.

Approaches:
    1. Using collections.Counter
        s1.split() and s2.split() divide the strings into words.
        Counter(...) + Counter(...) merges word counts from both strings.
        [word for word in count if count[word] == 1] selects words that appear exactly once.
    2. Using get()
        (s1 + " " + s2).split() merges and splits both strings into words.
        d.get(word, 0) + 1 increments the word count or initializes it to 1.
        List comprehension selects words that appear only once.
    3. Using set
        The symmetric difference (^) extracts words that are present in one string but not the other.
        set(s1.split()) and set(s2.split()) create sets of unique words.
        set1 ^ set2 gives words present in only one set.
        list(...) converts the set back to a list.
    4. Using for loop
        This approach manually compares each word with all others using nested loops to count occurrences.
        It does not require additional data structures but is highly inefficient due to repetitive comparisons.


"""

# Approach 1
from collections import Counter
s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"

count = Counter(s1.split()) + Counter(s2.split())
print(count) # Counter({'Geeks': 4, 'for': 2, 'Learning': 1, 'from': 1})
res = [word for word in count if count[word] == 1]
print(res)

# Approach 2
s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"
d = {}

for word in (s1 + " " + s2).split():
    d[word] = d.get(word, 0) + 1

res = [word for word in d if d[word] == 1]
print(res)

# Approach 3
s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"

set1 = set(s1.split())
set2 = set(s2.split())

res = list(set1 ^ set2)
print(res)

# Approach 4
s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"
words = (s1 + " " + s2).split()

res = []
for word in words:
    if words.count(word) == 1:
        res.append(word)

print(res)
