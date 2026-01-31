"""
Author      : Satish Kumar
Created On  : 2025-12-24

Description :
    This program computes the nth Fibonacci number using
    an iterative approach.

Approach :
    - Fibonacci sequence definition:
        F(0) = 0, F(1) = 1
        F(n) = F(n-1) + F(n-2)
    - Iteratively compute Fibonacci numbers up to n
    - Maintain only the last two computed values

Time Complexity :
    - O(N)

Space Complexity :
    - O(1)
"""


def nth_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return 0
    if n == 2:
        return 1

    prev, curr = 0, 1

    for _ in range(2, n):
        prev, curr = curr, prev + curr

    return curr


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    print(nth_fib(num))
