#  Write a python programm to convert kilometer to meter & miles

kilometer=float(input("Enter the distance in Kilometer:"))

conversion_factor=1000
conversion_factormiles=0.62137

meter=kilometer*conversion_factor
miles=kilometer*conversion_factormiles

print(f"{kilometer} kilometer is equal to {meter} meter")
print(f"{kilometer} kilometer is equal to {miles} miles")
