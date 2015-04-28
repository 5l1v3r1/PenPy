#!/usr/bin/env python

class Student:
    """
    This is a docstring
    """
    sCount = 0
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        Student.sCount += 1

    def counter(self):
        print('the total students are %d') % Student.sCount

    def sayStudent(self):
        print('Name: ', self.name, 'Subject: ', self.subject)

stu1 = Student("Jill", "python")
stu2 = Student("Joaquin", "C")
stu3 = Student("Jason", "C++")
stu4 = Student("Joe", "Ruby")
stu5 = Student("Johnny", "Node")

stu1.sayStudent()
stu2.sayStudent()
stu3.sayStudent()
stu4.sayStudent()
stu5.sayStudent()

print('The total students are: ', Student.sCount)
print(Student.__doc__)
print(Student.__name__)
print(Student.__module__)
print(Student.__dict__)