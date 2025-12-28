"""
Author      : Satish Kumar
Created On  : 28-12-2025

Problem Statement :
    Different ways to clear a list in python
Approaches:
    1. Using clear() method
        clear() removes all elements from the list a in place.
        The list object remains the same, only its contents are erased.
    2. Using del a[:]
        a[:] selects the entire list.
        del a[:] deletes all selected elements, leaving the list empty.
    3. Using a loop with pop()
        a.pop() removes the last element in each iteration.
        Loop continues until the list becomes empty.

Time Complexity : O(n) for all 3 approaches

Space Complexity : O(1) for all 3 approaches

"""

# Approach 1
a = [1,2,3,4,5]
a.clear()
print(a)

# Approach 2
a = [1,2,3,4,5]
del a[:]
print(a)


# Approach 3
a = [1,2,3,4,5]
while a:
    a.pop()

print(a)