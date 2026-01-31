"""
Author      : Satish Kumar
Created On  : 2025-12-23
Description :
    This program checks whether a given number is a Fibonacci number
    using a brute-force iterative approach.

Approach :
    - Generate Fibonacci numbers iteratively starting from 0
    - Stop when the generated number is greater than or equal to n
    - If the generated number equals n, it is a Fibonacci number

Time Complexity :
    - O(k), where k is the index of n in the Fibonacci sequence

Space Complexity :
    - O(1)
"""


def is_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1

    # Generate Fibonacci numbers until a >= n
    while a < n:
        a, b = b, a + b

    return a == n


if __name__ == '__main__':
    num = 15

    if is_fibonacci(num):
        print(f"{num} is a Fibonacci number")
    else:
        print(f"{num} is not a Fibonacci number")
