# Jake Million
# Question 1
# 2/15/22

# creating class car
class car():
    def __init__(self, model, make, speed):
        self.__model = model
        self.__make = make
        self.__speed = speed
        print("Model:", model, " Make:", make, " Speed:", speed)

    def acc(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def getSpeed(self):
        return self.__speed

# Object car

myCar = car("2008 Fusion", "Ford", 0)
# Calling the accelerate method
for i in range(0,5):
    myCar.acc()
    print("Speed:", myCar.getSpeed())
print("\n")
for i in range(0,5):
    myCar.brake()
    print("Speed:", myCar.getSpeed())





