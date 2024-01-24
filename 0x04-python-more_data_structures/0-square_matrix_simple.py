#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    This function computes the square value of all integers of a matrix.
    The original matrix remains unchanged.

    Parameters:
        matrix (list of lists): A matrix of integers.

    Returns:
        list of lists: A new matrix where each element is the square of the corresponding element in the original matrix.
    """
    # Validate the input matrix
    if not all(isinstance(row, list) for row in matrix):
        raise ValueError("Input should be a list of lists")
    if not all(isinstance(element, int) for row in matrix for element in row):
        raise ValueError("All elements in the matrix should be integers")

    # Compute the square matrix
    new_matrix = [[element ** 2 for element in row] for row in matrix]

    return new_matrix
