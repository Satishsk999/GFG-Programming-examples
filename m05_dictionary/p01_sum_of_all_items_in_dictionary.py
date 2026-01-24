"""
Author      : Satish Kumar
Created On  : 24.01.2026

Problem Statement : Given a dictionary, the task is to calculate the sum of all its values.

Approaches:
    1. Using sum()
        This method directly accesses all values using d.values() and passes them to the sum() function.
        This approach is highly efficient as it avoids extra list creation and leverages Python’s built-in optimization.
    2. Using list comprehension and sum()
        It is a clean approach, but slightly slower than sum(d.values()) because it constructs a list in memory.
    3. Using a for loop
        it is slightly slower than sum(d.values()) due to manual addition in each iteration.

"""

# Approach 1
d = {'a': 100, 'b': 200, 'c': 400}
res = sum(d.values())
print(res)
# Approach 2
d = {'a': 10, 'b': 20, 'c': 23}
sm = sum([d[key] for key in d])
print(sm)
# Approach 3
d = {'a': 10, 'b': 20, 'c': 30}
res = 0
for i in d.values():
    res += i
print(res)
