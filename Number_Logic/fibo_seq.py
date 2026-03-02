# Write a python programm to display the fibonacci sequence

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterm = int(input("How many terms? "))
if nterm <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterm):
        print(recur_fibo(i))