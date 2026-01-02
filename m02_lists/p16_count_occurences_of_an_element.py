"""
Author      : Satish Kumar
Created On  : 2/1/2026

Problem Statement : Count Occurrences of an Element in a List in Python

Approaches:
    1. Using count()
    	The count() method is built-in and
    	directly returns the number of times an element appears in the list.
    2. Using a Loop
    3. Using Counter from collections
    	Counter class from the collections module can count occurrences for all elements
    	and returns the results as a dictionary.
    	Note: This method is not efficient for finding occurrence of single element
    	because it requires O(n) extra space to create a new dictionary.
    	But this method is very efficient when finding all occurrences of elements.



"""

# Approach 1
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
print(a.count(3))

# Approach 2
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
count = 0
for val in a:
	if val == 3:
		count += 1
print(count)

# Approach 3
from collections import Counter
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
res = Counter(a)
print(res[3])