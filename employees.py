# Jake Million
# Question 2
# 2/15/2022

# creating employee class
class emp():
    def __init__(self, first, last, eid, dep, title):
        self.__first = first
        self.__last = last
        self.__eid = eid
        self.__dep = dep
        self.__title = title
        print(first, "|", last, "|", eid, "|", dep, "|", title)

    def email(self):
        fullName = self.__first + " " + self.__last
        print(fullName)
        email = self.__first + "." + self.__last + "@company.com"
        print(email.lower())

# formatting/employee data
print("\t  Name | ID | Department | Job Title")
emp1 = emp("Susan", "Meyers", "47899", "Accounting", "Vice President")
emp2 = emp("Mark", "Jones", "39119", "IT", "Programmer")
emp3 = emp("Joy", "Rogers", "81774", "Manufacturing", "Engineer")

emp.email(emp1)
print("\n")
emp.email(emp2)
print("\n")
emp.email(emp3)



