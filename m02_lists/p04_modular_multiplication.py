"""
Author      : Satish Kumar
Created On  : 2025-12-26

Description :Given an array of numbers and an integer n,
the task is to find the remainder when all numbers in the array are multiplied and modulo by n
For ex-
Input: arr[] = [100, 10, 5, 25, 35, 14],  n = 11
Output: 9
Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

Approaches:
    Approach 1 (Naive Multiplication):
        -This method multiplies all numbers first and then applies modulo n.
        -It's simple but can overflow if the numbers are large
        -Not recommended for large numbers

    Approach 2 (Modular Multiplication):
        -Modular arithmetic is used to avoid overflow.Instead of multiplying all numbers,
        we take the remainder of each number with n during multiplication

        (a * b) % n = ((a % n) * (b % n)) % n

Edge Cases:
    | Edge Case          | Expected Behavior |
    | ------------------ | ----------------- |
    | `n == 0`           | Invalid input     |
    | Array contains `0` | Result = `0`      |
    | Empty array        | Result = `1 % n`  |
    | Large numbers      | Use Approach 2    |


Time Complexity :  O(n) for both approaches

Space Complexity : O(1) for both approaches

"""

# Approach 1:
arr = [100, 10, 5, 25, 35, 14]
n = 11
mul = 1
for i in arr:
    mul = mul * i

print(mul % n)

# Approach 2

mul = 1
for num in arr:
    mul = (mul * (num % n)) % n

print(mul)


# Optimized solution

arr = [100, 10, 5, 25, 35, 14]
n = 11

# Edge case: modulo by zero
if n == 0:
    print("Modulo by zero is not allowed")
else:
    mul = 1

    # Edge case: empty array
    if len(arr) == 0:
        print(1 % n)
    else:
        for num in arr:
            # Early exit if product becomes zero
            if num == 0:
                mul = 0
                break

            mul = (mul * (num % n)) % n

        print(mul)