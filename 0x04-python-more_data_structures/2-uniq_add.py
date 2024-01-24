#!/usr/bin/python3
'''
This function adds all unique integers
in a list (only once for each integer).

Parameters:
my_list (list): A list of integers.

Returns:
integer: The sum of unique integers in the list.
'''


def uniq_add(my_list=[]):
    unique_set = {num for num in my_list if isinstance(num, int)}

    return sum(unique_set)
