"""
Approach:
Definition of prime number:

Check if n <= 1, if true, it's not prime.
Loop from 2 to the square root of n, if n % i == 0, it's not prime. If no divisors found, n is prime.

We can check if a number is prime or not by traversing all the numbers from 2 to sqrt(n)+1
and checking if n is divisible by any of those numbers.

Note: We iterate only up to the square root of n because if n has any divisor greater than its square root,
 there must also be a corresponding divisor smaller than the square root.
 So, checking beyond sqrt(n) is unnecessary and would only waste computation.

math.isqrt(n) >>> int(n**0.5)
"""


def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False

        return True

if __name__ == "__main__":
    num = int(input("Enter the number:"))

    if is_prime(num):
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')




