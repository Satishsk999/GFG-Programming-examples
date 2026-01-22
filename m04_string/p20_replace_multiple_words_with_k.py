"""
Author      : Satish Kumar
Created On  : 22.01.2026

Problem Statement : Replace all occurrences of specific words in a string with a single replacement word K.
    text = "apple orange banana"
    words_to_replace = ["apple", "banana"]
    Output: "K orange K"

Approaches:
    1. Using List Comprehension
    2. Using for loop and replace()
        s.replace(word, k) replaces all occurrences of word with k.
        The loop iterates over all target words in li.

Note : replace() removes all occurrences while in the 1st approach , we don't remove substrings
Check sample output for the subtle difference in output.

"""

# Approach 1
s = 'Geeksforgeeks is best for geeks and CS'
li = ["best", "CS", "for"]
k = "K"

res = ' '.join([k if word in li else word for word in s.split()])

print(res)
# Output: Geeksforgeeks is K K geeks and K


# Approach 2
s = "Geeksforgeeks is best for geeks and CS"
li = ["best", "CS", "for"]
k = "K"

for word in li:
    s = s.replace(word, k)
print(s)

# Output: GeeksKgeeks is K K geeks and K
