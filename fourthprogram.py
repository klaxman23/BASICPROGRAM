# Write a program to print odd and even numbers with using list comprensive.

arr = [i for i in range(1,101) if i%2==0]
print("Even numbers:",arr)

arr = [i for i in range(1,101) if i%2==1]
print("Odd numbers:",arr)