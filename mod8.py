#!/usr/bin/env python

def printfunc(str):
    """
    This is a docstring
    """
    :param str:
    :return:
    print(str)
    return

printfunc('poop')
appendItems = ('appended', 'success')

def changeList(li):
    """
    this is a comment
    """
    li.append(appendItems)
    print(li)
    return

longList = [1,2,3,4]

changeList(longList)

def person(name, age, salary = '100k', job = 'Cyber Security'):
    """
    Information about the person
    """
    print('My name is', name)
    print('My age is', age)
    print('My job is', job)
    print('My salary is', salary)
    return
person('Johnny', '34')

def printValue(var1, *vartuple):
    """
    print all dis
    """
    print(var1)
    for var in vartuple:
        print(var)
    return

printValue(1)
printValue(1,2,3,4,5)
printValue(1, 'value', 'two', 4.0)

