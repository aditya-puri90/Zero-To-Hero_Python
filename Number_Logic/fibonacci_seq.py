# write a python programm to print the fibbonacci sequence up to n terms, where n is priovided by the user.

nterm=int(input("Enter the number of nterms:"))
n1=0
n2=1
count=0
if nterm <= 0:
    print("please enter a positive integer:")
elif nterm == 1:
    print("fibonacci sequence up to ",nterm)
    print(n1)
else:
    print("fibonacci sequence up to ",nterm)
    while count < nterm:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2= nth
        count +=1
        