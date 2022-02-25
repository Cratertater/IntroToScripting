# Jake Million
# 2/25/22

# importing random for the student marks
import random

# create class of students


class students():
    def __init__(self, name, marks1, marks2, marks3, marks4, marks5, marks6):
        self.__name = name
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3
        self.__marks4 = marks4
        self.__marks5 = marks5
        self.__marks6 = marks6

    def stu1(self):
        n = self.__name
        for i in range(0, 5):
            m = random.randint(0, 100)
            self.__marks1 += m
        avg = self.__marks1/600
        return avg

    def stu2(self):
        self.__name = input("Enter student name: ")
        for i in range(0, 5):
            m = random.randint(0, 100)
            self.__marks2 += m
        avg = self.__marks2/600
        return avg

    def stu3(self):
        self.__name = input("Enter student name: ")
        for i in range(0, 5):
            m = random.randint(0, 100)
            self.__marks3 += m
        avg = self.__marks3/600
        return avg

    def stu4(self):
        self.__name = input("Enter student name: ")
        for i in range(0, 5):
            m = random.randint(0, 100)
            self.__marks4 += m
        avg = self.__marks4/600
        return avg

    def stu5(self):
        self.__name = input("Enter student name: ")
        for i in range(0, 5):
            m = random.randint(0, 100)
            self.__marks5 += m
        avg = self.__marks5/600
        return avg

    def stu6(self):
        self.__name = input("Enter student name: ")
        for i in range(0, 5):
            m = random.randint(0, 100)
            self.__marks6 += m
        avg = self.__marks6/600
        return avg

    def percentSort(self):
        stuMarks = [students.stu1(self.__marks1), students.stu2(self.__marks2), students.stu3(self.__marks3)]
        stuMarks2 = [students.stu4(self.__marks4), students.stu5(self.__marks5), students.stu6(self.__marks6)]
        stuMarks.append(stuMarks2)
        p = 1
        while p < len(stuMarks):
            temp = stuMarks[p]
            i = p-1
            while i >= 0 and stuMarks[i] > temp:
                stuMarks[i+1] = stuMarks[i]
                i -= 1
            stuMarks[i+1] = temp
            p += 1


students.stu1(students("J", 0, 0, 0, 0, 0, 0))
students.stu2(students("B", 0, 0, 0, 0, 0, 0))
students.stu3(students("A", 0, 0, 0, 0, 0, 0))
students.stu4(students("s", 0, 0, 0, 0, 0, 0))
students.stu5(students("d", 0, 0, 0, 0, 0, 0))
students.stu6(students("w", 0, 0, 0, 0, 0, 0))

print(students.percentSort(students("je", 0, 0, 0, 0, 0, 0)))
