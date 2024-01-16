#!/usr/bin/python3
'''
This script encompasses a function that both 
prints and returns the last digit of a number.
'''


def print_last_digit(number):
    strNum = str(number)
    lastDigit = strNum[-1]
    print(int(lastDigit), end='')

    return int(lastDigit)
