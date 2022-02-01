#Welcome
print("Welcome to the Change Counting game, see if you can get the right amount of change to equal 1.00")
#Variable declaration
p = .01
n = .5
d = .10
q = .25
#How many of each coin
pNum = float(input("How many pennies: "))
pNum *= p
nNum = float(input("How many nickels: "))
nNum *= n
dNum = float(input("How many dimes: "))
dNum *= d
qNum = float(input("How many quarters: "))
qNum *= q
#Dollar check
sum = pNum + nNum + dNum + qNum
if(sum == 1):
    print("Congratulations! You can do math")
elif(sum < 1):
    print("You were under a dollar by", round(1.00 - sum, 2), "cents.")
else:
    print("You were over a dollar by", round(sum-1.00, 2), "cents.")