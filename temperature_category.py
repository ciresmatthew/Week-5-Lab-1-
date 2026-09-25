#Matthew Cires
#CMP 131 
#Week 5
#Lab 1
#Temperature
#9/23/26
print("-----------------")
print("Fahrenheit Temperature checker")
print("-----------------")
temp = float(input("Enter the farenheit:"))
if temp >= 80:
    print("It is hot today")
elif temp >= 79:
    print("It is warm today ")
elif temp >= 50:
    print("It is warm today")
elif temp <= 49.9:
    print("It is cold today")
