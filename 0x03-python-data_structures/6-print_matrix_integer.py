#!/usr/bin/python3
'''
Displays a matrix containing integers.
'''


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element != row[-1]:
                print('{}'.format(element), end=' ')
            else:
                print('{}'.format(element))