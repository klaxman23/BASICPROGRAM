# Write a program to sum of the 1 to n.

n = int(input("Enter a value: ")) # Taking the user input value:

sum = 0  # inital sum value should be 0

for i in range(1,n+1): # Looping will repeat.
    sum = sum + i # each value increment the value.
    
print("Your result:",sum) # Result will print once loop will end.

