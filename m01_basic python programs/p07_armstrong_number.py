num = int(input("Enter a number: "))

num_copy = num
no_of_digits = 0

while num_copy != 0:
    num_copy //= 10
    no_of_digits += 1

num_copy = num
armstrong_sum = 0

while num_copy != 0:
    p = num_copy % 10
    armstrong_sum += p ** no_of_digits
    num_copy //= 10

if armstrong_sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
