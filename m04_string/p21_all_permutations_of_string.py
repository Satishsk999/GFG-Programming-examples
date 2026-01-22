"""
Author      : Satish Kumar
Created On  : 22/01/2026

Problem Statement : Generate all the possible permutations of a given string

Approaches:
        1. Using itertools.permutations:
            itertools.permutations(s): generates all possible permutations of the string s, returning each permutation as a tuple.
            ''.join(p): converts each tuple p into a string by concatenating its elements.
            list comprehension collects all the joined strings (permutations) into a list.
        2. Using Recursion:
            If the string s is empty, print the accumulated answer.
            For each character in s, remove the character and
                recursively permute the remaining characters while adding the character to answer.
            Call permute(s, answer) with the initial string and an empty answer to start generating permutations.


"""

# Approach 1
import itertools

s = "GFG"
li = [''.join(p) for p in itertools.permutations(s)]
print(li)

# Approach 2
def permute(s, s2):
    if len(s) == 0:
        print(s2, end=' ')
        return

    for i in range(len(s)):
        char = s[i]
        left_s = s[0:i]
        right_s = s[i + 1:]
        rest = left_s + right_s
        permute(rest, s2 + char)


s1 = "GFG"
s2 = ""
permute(s1, s2)
