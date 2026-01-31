# t = 10,20,30,4
# print(type(t))

  # Write a program to take a tuple of numbers from the keyboard and print its sum and
# average?

t = tuple(map(int, input("Enter a number :").split()))
print(t)
print(type(t))
print("Sum of the tuple is :", sum(t))
print("Maximum of the tuple is :", max(t))
print("Minimum of the tuple is :", min(t))
print("Length of the tuple is :", len(t))
t1 = sorted(t)
print(" Sorted tuple is :", t1)
tup = (10,20,30,10,10,50)
cnt = (tup.count(10))
print("The no. of occurrences of 10 is :", cnt)
print("The index of occurence of 10 is :", tup.index(10))
