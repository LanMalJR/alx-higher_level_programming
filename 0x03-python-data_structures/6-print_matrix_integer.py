#!/usr/bin/python3
'''
Displays a matrix containing integers.
'''


def print_matrix_integer(matrix=[[]]):
    if matrix is None or not matrix:
        matrix = [[]]

    for row in matrix:
        print(' '.join("{:d}".format(element) for element in row))
