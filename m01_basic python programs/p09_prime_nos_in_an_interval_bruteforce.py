"""
Author      : Satish Kumar
Created On  : 2025-12-23
Description :
    This program prints all prime numbers within a given interval
    using an optimized prime-checking approach (trial division
    up to square root of the number).

Approach :
    - Iterate through each number in the given range
    - Check primality using trial division up to √n

Time Complexity :
    - O(n√n) for the interval
    - O(√n) for individual prime check

Space Complexity :
    - O(1)
"""


def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    start = int(input("Enter the starting index(i>1): "))
    end = int(input("Enter the ending index: "))

    for i in range(start,end+1):
        if is_prime(i):
            print(i)