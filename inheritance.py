#!/usr/bin/env python

#Parent class defined
class Parent:
    pa = 2
    def __init__(self):
        print('Parent constructor called')

    def pm(self):
        print('I am a parent method')

    def setAttrib(self, attrib):
        Parent.setAttrib = attrib

    def getAttrib(self):
        print('Attrib is:', Parent.pa)

class Child(Parent):
    def __init__(self):
        print('Child constructor called')

    def cm(self):
        print('Child method called')

#Creating instances of classes
john = Child()
john.cm()
john.pm()
john.setAttrib(5000)
john.getAttrib()