"""
Author      : Satish Kumar
Created On  : 01.02.2026

Problem Statement :Given a list of numbers, the task is to create a list of tuples
                    where each tuple contains a number and its cube.
 For example:

Input: [1, 2, 3]
Output: [(1, 1), (2, 8), (3, 27)]

Approaches:
    1. Using List Comprehension
        (n, n**3) for n in a iterates over each element n in the list and creates a tuple with the number and its cube.
        Square brackets [ ] collect all tuples into a list.
    2. Using map() with lambda
        lambda n: (n, n**3) defines an anonymous function to create tuples of (number, cube).
        map function applies the lambda to each element of numbers.
        list() converts the result of map into a list.
    3. Using zip()
        This method separates numbers and their cubes into two lists and then combines them with zip().
    4. Using for Loop with append()
        This method uses a standard loop to build the list incrementally.


"""

# Approach 1
l = [1,2,3,4,5]
lt = [(n,n**3) for n in l]
print(lt)

# Approach 2
a = [1, 2, 3, 4, 5]
res = list(map(lambda n: (n, n**3), a))
print(res)

# Approach 3
a = [1, 2, 3, 4, 5]
res = list(zip(a, [n**3 for n in a]))
print(res)

# Approach 4
a = [1, 2, 3, 4, 5]
res = []
for n in a:
    res.append((n, n**3))
print(res)