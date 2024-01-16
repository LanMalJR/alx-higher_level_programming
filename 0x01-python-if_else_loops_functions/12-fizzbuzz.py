#!/usr/bin/python3
'''
This script incorporates a function that outputs the
solution to the commonly encountered FizzBuzz problem.
'''


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')
