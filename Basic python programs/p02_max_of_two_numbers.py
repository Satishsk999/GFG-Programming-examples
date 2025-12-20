
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# result = max(num1,num2)
result = 0
if num1 > num2:
    result = num1
else:
    result = num2
print(f'The maximum of 2 numbers is :{result} ')