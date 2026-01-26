"""
Author      : Satish Kumar
Created On  : 26/01/2026

Problem Statement :Given a list of votes where each element represents a vote for a candidate,
the task is to determine the winner of the election. If multiple candidates receive the same number of maximum votes,
the candidate with the lexicographically smaller name should be declared the winner.
For Example:

Input: [ "john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john" ]
Output: John
Explanation: Candidates are ['john', 'johnny', 'jamie', 'jackie']
'john' and 'johnny' have the maximum votes, but 'john' is lexicographically smaller.

Approaches:
    1. Using Counter
        This method counts all votes using Counter and
        selects the candidate with the highest count, resolving ties by sorting names.

"""

# Approach 1
from collections import Counter
votes = ['john','johnny','jackie','johnny','john','jackie', 'jamie','jamie','john','johnny','jamie','johnny','john']
c = Counter(votes) # Counter({'john': 4, 'johnny': 4, 'jamie': 3, 'jackie': 2})
m = max(c.values()) # 4
w = [i for i in c if c[i] == m]

print(c) # ['john', 'johnny']
print(sorted(w)[0]) # john

