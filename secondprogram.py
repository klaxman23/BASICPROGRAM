#Write a program to remove the dublicate values.

num = [1,2,3,1,2,3,4,5,6,7] # Take some sample list of data.

num1 = [] # empty list 

for i in num: # Loop will run
    if i not in num1: # here comparing the values repeted values remove.
        num1.append(i) # non repeted value take a insert the value in num1.
        
print(num1) # print the value in num1