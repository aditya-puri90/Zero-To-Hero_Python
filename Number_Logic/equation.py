# Write a python programm to solve the equation ax^2 + bx + c = 0, where a, b and c are real no and a is not equal to 0. 

import math
a=float(input("Enter the valueof a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))

discriminant =b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2= (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2:{root2}")
elif discriminant == 0:
    root = -b /(2*a)
    print(f"Root: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) /(2*a) 
    print(f"Root 1: {real_part}+{imaginary_part}i")
    print(f"Root 2: {real_part}-{imaginary_part}i")
     
