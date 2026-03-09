# Write a python programm to calculate the body mass index.

def bodymassindex(height,weight):
    return round((weight/height**2),2)

h=float(input("Enter the heigtht in meter:"))
w=float(input("Enter the weight in kg:"))

print("Welcome to the BMI calculator:")
bmi=bodymassindex(h,w)
print("Your BMI is:" ,bmi)

if bmi <=18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal:")
elif 25< bmi <= 29.29:
    print("You are overweight:")
else:
    print("You are obese.")