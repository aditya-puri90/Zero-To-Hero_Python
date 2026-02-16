"""
Script to divide two numbers provided by the user.
"""
# Write the python programm to do arithmetic operation Division

num1=float(input("Enter the num1:"))
num2=float(input("Enter the num2:"))
if num2==0:
    print("Error:Division by zero is not allowed")
else:
    div=num1/num2
    print(f"Division:{num1}/{num2}={div}")