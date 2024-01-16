#!/usr/bin/python3
'''
Script prints numbers from 0->99
'''
for i in range(100):

    if i == 99:
        print(i)
    else:
        print(i if i > 9 else '0{}'.format(i), end=', ')
