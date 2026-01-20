"""
Author      : Satish Kumar
Created On  : 21.01.2026

Problem Statement : split a string into parts based on a delimiter
                and then join those parts with a different separator

Approaches:
    1. Using split() and join()
    2. Using str.partition() and str.replace()
        This method splits the string manually using partition(), iterating over it to separate head and tail parts.
         After splitting, replace() or manual manipulation joins the parts.
         While functional, it’s less efficient due to multiple iterations and extra logic.

"""

# Approach 1
a = "Hello, how are you?"
b = a.split()       # Split by space
c = "-".join(b)     # Join with hyphen

print(b)
print(c)

# Approach 2
a = "Hello, how are you?"
words, rem = [], a

while rem:
    head,_,rem = rem.partition(" ")
    if head:
        words.append(head)

c = "-".join(words)
print(words)
print(c)
