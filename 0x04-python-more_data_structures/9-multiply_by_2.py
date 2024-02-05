#!/usr/bin/python3
'''
The function returns a new dictionary
with all values multiplied by 2.

Parameters:
    a_dictionary (dict): A dictionary with numeric values.

Returns:
    dict: A new dictionary with the same keys as the
    input dictionary, but with all values multiplied by 2.
'''


def multiply_by_2(a_dictionary):
    newDict = {}

    for key, value in a_dictionary.items():
        newDict[key] = value * 2

    return newDict
