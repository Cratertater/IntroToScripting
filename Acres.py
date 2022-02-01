#Variable Declaration
a = 0

#Asking user for input
t = int(input("Enter the total square feet of a tract of land: "))

#Finding amount of acres and rounding to two decimal places
a = round(t/43560, 2)
#Printing how much acres t is
print("Total acres ", a)