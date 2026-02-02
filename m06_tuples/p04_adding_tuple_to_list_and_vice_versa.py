"""
Author      : Satish Kumar
Created On  :

Problem Statement :

Given a list and a tuple (or vice versa) and the task is to combine them.
This could mean appending the tuple as a single element to the list, merging elements individually,
or combining a list with a tuple after converting it.

For Example:
a = [1, 2, 3]
b = (4, 5)
c = [6, 7]

Adding b to a can produce [1, 2, 3, (4, 5)] or [1, 2, 3, 4, 5].
Adding c to b can produce (4, 5, 6, 7).

Approaches:
    1. Using extend() and + operator
         extend(b) adds each element of b to a and
         tuple(c) converts list c to a tuple, then + concatenates b and c into d.
    2. Using * Operator and append()
        append(b) nests b inside and (*b, *c) unpacks both sequences into a new tuple.
    3. Using insert() and List Comprehension
        insert(len(a), b) adds b at the end of a and
        tuple(x for x in b) creates a tuple from b, then + tuple(c) merges it with c.
    4. Using list() and tuple()
         list(b) converts tuple to list to extend a and
         temp_list.extend(c) merges c, then tuple(temp_list) converts it back to a tuple.

"""

# Approach 1
a = [1, 2, 3]
b = (4, 5)
c = [6, 7]

# add tuple to list a
a.extend(c)
print(a)

# add list to tuple b
d = b + tuple(c)
print(d)

# Approach 2
a = [1, 2, 3]
b = (4, 5)
c = [6, 7]

# add tuple to list a
a.append(b)
print(a)

# add list to tuple b
d = (*b, *c)
print(d)

# Approach 3
a = [1, 2, 3]
b = (4, 5)
c = [6, 7]

# add tuple to list a
a.insert(len(a), b)
print(a)

# add list to tuple b
d = tuple(x for x in b) + tuple(c)
print(d)

# Approach 4
a = [1, 2, 3]
b = (4, 5)
c = [6, 7]

# add tuple to list a
a.extend(list(b))
print(a)

# add list to tuple b
temp_list = list(b)
temp_list.extend(c)
d = tuple(temp_list)
print(d)
