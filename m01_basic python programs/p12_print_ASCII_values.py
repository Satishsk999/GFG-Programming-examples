"""
Author      : Satish Kumar
Created On  : 2025-12-24

Description :
    This module provides utility functions to convert:
    1. A single ASCII character to its corresponding ASCII value
    2. An ASCII value to its corresponding character

    ASCII (American Standard Code for Information Interchange)
    is a character encoding standard that assigns numeric values
    from 0 to 127 to characters.

Approach :
    - Use Python's built-in ord() function to get ASCII value of a character
    - Use Python's built-in chr() function to get character from ASCII value
    - Validate inputs to ensure correctness and avoid invalid conversions

ASCII Range :
    - Valid ASCII values: 0 to 127
    - Values outside this range are not standard ASCII characters

Time Complexity :
    - O(1) for all operations

Space Complexity :
    - O(1)
"""


def char_to_ascii(c):
    # Ensure input is exactly one character
    if len(c) != 1:
        raise ValueError("Input must be a single character")

    # ord() returns the Unicode code point;
    # ASCII characters must be in the range 0–127
    if ord(c) > 127:
        raise ValueError("Character is not an ASCII character")

    return ord(c)


def ascii_to_char(n):
    # ASCII valid range check
    if not (0 <= n <= 127):
        raise ValueError("ASCII value must be in range 0–127")

    return chr(n)


if __name__ == '__main__':
    ch = input("Enter a character: ")
    print(char_to_ascii(ch))
