#!/usr/bin/python3
'''
This script generates and prints all unique
combinations between two numbers.
'''
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print('{}{}'.format(i, j))
        else:
            print('{}{}'.format(i, j), end=', ')
