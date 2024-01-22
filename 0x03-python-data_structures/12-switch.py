#!/usr/bin/python3
'''
The code swaps values of variables
`a` and `b` and prints them.
'''


a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
