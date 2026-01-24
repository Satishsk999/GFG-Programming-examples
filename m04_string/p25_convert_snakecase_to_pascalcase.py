"""
Author      : Satish Kumar
Created On  : 24.01.2026

Problem Statement : Given a string in snake_case, the task is to convert it into PascalCase,
                where each word starts with an uppercase letter and there are no underscores

Approaches:
    1. Using split() and capitalize()
        This method splits the string by underscores, capitalizes each word and then joins them back together.
        It is efficient in terms of both time and readability.
    2. Using str.title() and replace()
        replace("_", " ") handles the conversion of underscores to spaces.
        title() ensures that the first letter of each word is capitalized.
        replace(" ", "") removes any spaces, ensuring the result is in pascal case.
    3. Using string.capwords()
        s.replace('_', ' ') replaces underscores with spaces.
        string.capwords() capitalizes the first letter of each word.
        replace(' ', '') removes all spaces to form PascalCase.

"""

# Approach 1
s= 'geeksforgeeks_is_best'

res = ''.join(word.capitalize() for word in s.split('_'))
print(res)

# Approach 2

s= 'geeksforgeeks_is_best'
res = s.replace("_", " ").title().replace(" ", "")
print(res)

# Approach 3

import string
s = 'geeksforgeeks_is_best'
res = string.capwords(s.replace('_', ' ')).replace(' ', '')
print(res)

