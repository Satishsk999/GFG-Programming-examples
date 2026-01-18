"""
Author      : Satish Kumar
Created On  : 18/01/2026

Problem Statement : Given a string, the task is to reverse the words in it without changing the words themselves.

Approaches:
    1.Using split() and join()
        s.split() splits the string into a list of words.
        [::-1] reverses the list of words.
        ' '.join(...) concatenates the reversed words into a single string separated by spaces.
    2.Using a loop
        reversed(words) creates an iterator to traverse the list in reverse order.
        Inside the loop, res += word + " " appends each word followed by a space.
        res.strip() removes the trailing space at the end.
    3.Using deque()
        A deque (double-ended queue) is efficient for large strings, as it allows O(1) pops from both ends.
        This method uses pop() to retrieve words in reverse order.

    4.Using stack()
        This method uses a stack (LIFO structure) to reverse the order of words.
        Words are pushed onto the stack and popped to get them in reverse order.

| Approach                  | Time    | Space   | Verdict |
| ------------------------- | ------- | ------- | ------- |
| 1. split + reverse + join | O(n)    | O(n)    | ✅ BEST  |
| 2. Loop + `+=`            | ❌ O(n²) | ❌ O(n²) | BAD     |
| 3. deque                  | ❌ O(n²) | ❌ O(n²) | BAD     |
| 4. stack                  | ❌ O(n²) | ❌ O(n²) | BAD     |


"""

# Approach 1
s = "greatest the am I"
words = s.split()
res = " ".join(words[::-1])
print(res)

# Approach 2
s = "greatest the am I"
words = s.split()
res = ""

for i in reversed(words):
    res += i + " "

res = res.strip()
print(res)

# Approach 3
from collections import deque
s = "greatest the am I"
words = deque(s.split())
res = ""
while words:
    res += words.pop() + " "

res = res.strip()
print(res)

# Approach 4

s = "greatest the am I"
res = s.split()
stack = []

for i in res:
    stack.append(i)

res = ""
while stack:
    res += stack.pop() + " "

res = res.strip()
print(res)

