# Write a python programm to find the sum of natural numbers.

limit=int(input("Enter the limit:"))
sum=0
for i in range(1,limit+1):
    sum+=i
    print(f"The sum of first {limit} natural numbers is: {sum}")
    