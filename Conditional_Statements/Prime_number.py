# Write a python programm to check the prime number.
number=int(input("Enter the number:"))
if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            print(number,"is not a prime number")
            break
        else:
            print(number,"is a prime number")

            