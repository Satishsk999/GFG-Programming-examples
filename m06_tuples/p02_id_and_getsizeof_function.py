"""
Author      : Satish Kumar
Created On  : 31.01.2026

Problem Statement : explain about id() and getsizeof() function

Explanation:
id() : id() function to obtain memory address of the tuple or its elements.
        This method helps us to understand where objects are stored in memory.

sys.getsizeof(): sys.getsizeof() from sys module is used to find the memory size of a tuple (in bytes).
                It gives us the size of the tuple object itself,
                including the overhead Python uses for its internal structure.

"""

# id() function code
tup = (0, 1, 2, 'a', 3)
for item in tup:
    print(f"Memory address of {item}: {id(item)}")

# Sample output:
# Memory address of 0: 140707478391192
# Memory address of 1: 140707478391224
# Memory address of 2: 140707478391256
# Memory address of a: 140707478424800
# Memory address of 3: 140707478391288

# sys.getsizeof() function code
import sys
tup = (0, 1, 2, 'a', 3)
print(sys.getsizeof(tup)) # 80

for item in tup:
    print(item, sys.getsizeof(item))

# Sample output:
# 80
# 0 28
# 1 28
# 2 28
# a 42
# 3 28

