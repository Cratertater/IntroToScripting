#Getting users age

a = int(input("Enter a person's age:"))

#Classification

if(a <= 1):
    print("This person in an infant.")
elif(a > 1 and a < 13):
    print("This person is a child")
elif(a >= 13 and a < 20):
    print("This person is a teenager, good luck")
else:
    print("This person is an adult")
