"""
Author      : Satish Kumar
Created On  : 22.01.2026

Problem Statement : Reverse a string

Approaches:
    1.Using backward traversal – O(n) Time and O(n) Space
    2.Using Two Pointers - O(n) Time and O(n) Space
    3.Using Recursion - O(n) Time and O(n) Space
    4.Using Inbuilt methods - O(n) Time and O(n) Space

"""

# Approach 1
s = "hsitas"
res = []
for i in range(len(s)-1, -1, -1):  # range(start, stop, step)
    res.append(s[i])

res = ''.join(res)
print(res)

# Approach 2
st = "hsitas"

low = 0
high = len(s) - 1
s = list(st)  # make sure to convert string to list
while low < high:
    s[low], s[high] = s[high], s[low]
    low = low + 1
    high = high - 1

s = ''.join(s)
print(s)

# Approach 3
# Recursive Function to reverse a string
def reverseStringRec(arr, l, r):
    if l >= r:
        return

    # Swap the characters at the ends
    arr[l], arr[r] = arr[r], arr[l]

    # Recur for the remaining string
    reverseStringRec(arr, l + 1, r - 1)


def reverseString(s):
    # Convert string to list of characters
    arr = list(s)
    reverseStringRec(arr, 0, len(arr) - 1)

    # Convert list back to string
    return ''.join(arr)

s = "hsitas"
print(reverseString(s))

# Approach 4
s = "hsitas"
print(s[::-1])