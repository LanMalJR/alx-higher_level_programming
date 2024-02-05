#!/usr/bin/python3
'''
Eliminates all occurrences of the
characters 'c' and 'C' from a string.
'''


def no_c(my_string):
    c = ['c', 'C']
    newString = ''

    for letter in my_string:
        if letter in c:
            continue
        else:
            newString += letter

    return newString
