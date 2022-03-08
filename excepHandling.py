# Jake Million
# 3/7/22

import math

# getting inputs
inputs = []
divInputs = []
ui = int(input("Enter an integer between 0-100(inclusive): "))
while ui != -1:
    inputs.append(ui)
    ui = int(input("Enter an integer between 0-100(inclusive) or -1 to stop: "))
print(inputs)

# finding average
sum = 0
for i in range(0, len(inputs)):
    sum += inputs[i]
avg = sum/len(inputs)
print("Average of list: ", round(avg, 2))

# finding median
med = round(len(inputs)/2)
print("Median of list: ", inputs[med])

# finding standard of deviation
sdNum = 0
for i in range(0, len(inputs)):
    sdNum += (inputs[i] - avg)**2
standDev = sdNum/len(inputs)
print("Standard of Deviation for the list: ", round(math.sqrt(standDev), 2))

divList = []
try:
    for i in range(0, len(inputs)-1):
        divList.append(inputs[i]/inputs[i+1])
except ZeroDivisionError:
    print("ERROR! Tried to divide by zero.")
