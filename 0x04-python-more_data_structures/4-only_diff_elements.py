#!/usr/bin/python3
'''
This function returns a set of elements that
are in either set_1 or set_2 but not in both.

Parameters:
    set_1 (set): A set of elements.
    set_2 (set): Another set of elements.

Returns:
    set: A new set containing the elements that
    are in either set_1 or set_2 but not in both.
'''


def different_elements(set_1, set_2):
    diff_set = set()

    for element in set_1:
        if element not in set_2:
            diff_set.add(element)

    for element in set_2:
        if element not in set_1:
            diff_set.add(element)

    return diff_set
