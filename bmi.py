#user input of weight and height
w = int(input("Enter weight in pounds: "))
h = int(input("Enter height in inches: "))

#Calculate and print bmi
bmi = round((w*703)/pow(h, 2),1)
print("Your BMI:", bmi)

#Checking if Overweight, underweight, or optimal
if bmi >= 13.5 and bmi <= 25:
    print("You are within the optimal BMI range.")
elif bmi < 13.5:
    print("You are underweight.")
else:
    print("You are overweight.")