#!/usr/bin/python3
'''
Displays a matrix containing integers.
'''


def print_matrix(matrix=None):
    if matrix is None:
        matrix = [[]]

    for row in matrix:
        print(' '.join("{:d}".format(element) for element in row))
