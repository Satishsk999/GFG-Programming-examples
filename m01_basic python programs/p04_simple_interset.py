
try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))

    simple_interest = (principal * rate * time) / 100

    print(f'The simple interest is {simple_interest}')
except ValueError:
    print("Please enter valid numeric values.")

# Sample output:
# Enter the principal amount: 1000
# Enter the rate of interest: 10
# Enter the time period: 5
# The simple interest is 500.0
