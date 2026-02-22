# Write a python programm to check Armstrong number or not. An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.

num=int(input("Enter the number:"))
order=len(str(num))
sum=0
temp=num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
    if num == sum:
        print(f"{num} is an Armstrong number.")
        break
    else:
        print(f"{num} is not an Armstrong number.")
        
