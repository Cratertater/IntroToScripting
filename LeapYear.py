#Getting a year from user
y = int(input("Enter a year: "))
#leap year check
if y % 100 == 0 and y % 400 == 0:
    print(y, "is a leap year.")
elif y % 400 == 0 and y % 4 == 0:
    print(y, "is a leap year.")
else:
    print(y, "is not a leap year.")
