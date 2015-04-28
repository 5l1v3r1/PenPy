#!/usr/bin/env python

num = int(input('What\'s a prime number?:'))

if num > 1:
    for number in range(2, num):
        if (num % number) == 0:
            print ('You lose.,', num, 'is not a prime number')
            break
        else:
            print ('Ding, Ding, Ding.  You get a gold star.', num, 'is a prime number')
            break
    else:
        print('try a different', num)