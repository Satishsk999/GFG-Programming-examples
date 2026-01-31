import math

num = int(input("Enter the number whose factorial you want to calculate: "))

result = 1
for i in range(1, num+1):
    result *= i

print(f'The factorial of {num} is {result}')


# Sample output:

# Enter the number whose factorial you want to calculate: 10
# The factorial of 10 is 3628800


# Approach 2:
print(math.factorial(num))
