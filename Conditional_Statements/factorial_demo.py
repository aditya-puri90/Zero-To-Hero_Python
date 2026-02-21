# write a python programm to find the factorial of a number.

number1=int (input("enter a number:"))
factorial=1
if number1 < 0:
    print("factorial does not exist for negative numbers")
elif number1 == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,number1+1):
        factorial=factorial*i
        print("the factorial of ",number1,"is ",factorial)