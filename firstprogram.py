num = int(input("Enter a value:"))
num1 = int(input("Enter a value:"))
opr = input("Enter a operator: ")

if opr =="+":
    print("Your result:",num+num1)
elif opr == "-":
    print("Your result:",num-num1)
elif opr =="*":
    print("Your result:",num*num1)
elif opr =="/":
    print("Your result:",num/num1)
else:
    print("Invalid operator")