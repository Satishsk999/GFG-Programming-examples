
try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))

    amount = principal * (1 + rate/100)**time
    compound_interest = amount - principal

    print(f'The compound interest is {compound_interest}')
except ValueError:
    print("Please enter valid numeric values.")


# Sample output:
# Enter the principal amount: 1000
# Enter the rate of interest: 5
# Enter the time period: 2
# The compound interest is 102.5
