"""
Author      : Satish Kumar
Created On  : 28-12-2025

Problem Statement :
    Reversing a list in python

Approaches:
    1. Using reverse():
        reverse() method reverses the elements of the list in-place
        and it modify the original list without creating a new list.
    2. Using List slicing:
        This method builds a reversed version of the list using slicing with a negative step.
    3. Using reversed():
        Python's built-in reversed() function is another way to reverse the list.
        However, reversed() returns an iterator,
        so it needs to be converted back into a list.

| Approach           | In-Place | Time | Space | Recommended          |
| ------------------ | -------- | ---- | ----- | -------------------- |
| `reverse()`        | Yes      | O(n) | O(1)  | ✔ Yes                |
| `[::-1]`           | No       | O(n) | O(n)  | ✔ If copy needed     |
| `list(reversed())` | No       | O(n) | O(n)  | ✔ If iterator needed |

“In-place” means the operation modifies the original data structure itself,
 instead of creating a new one.

"""

# Approach 1
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)

# Approach 2
a = [1, 2, 3, 4, 5]
rev = a[::-1]
print(rev)

# Approach 3
a = [1, 2, 3, 4, 5]
rev = list(reversed(a))
print(rev)
