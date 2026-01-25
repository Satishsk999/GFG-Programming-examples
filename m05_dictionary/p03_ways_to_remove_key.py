"""
Author      : Satish Kumar
Created On  : 25.01.2026

Problem Statement : Given a dictionary, the task is to remove a specific key from it.

Approaches:
    1. Using pop()
        pop() method removes a specific key from the dictionary and returns its corresponding value.
    2. Using del()
        del() statement deletes a key-value pair from the dictionary directly and
        does not return the value making it ideal when the value is not needed.
    3. Using pop() with Default value
        We can also provide a default value to the pop() method,
        ensuring no error occurs if the key doesn’t exist.
    4. Using popitem() for Last Key Removal
        If we want to remove the last key-value pair in the dictionary,
        popitem() is a quick way to do it. Useful for LIFO operations.

"""

# Approach 1
a = {"name": "Nikki", "age": 25, "city": "New York"}
rv = a.pop("age")
print(a)
print(rv)

# Approach 2
a = {"name": "Nikki", "age": 25, "city": "New York"}
del a["city"]
print(a)

# Approach 3
a = {"name": "Niiki", "age": 25, "city": "New York"}
rv = a.pop("country", "Key not found")
print(a)
print(rv)

# Approach 4
a = {"name": "Nikki", "age": 25, "city": "New York"}
c = a.popitem()
print(a)
print(c)