#!/usr/bin/python3
'''
This function returns a set of common elements in two sets.

Parameters:
    set_1 (set): A set of elements.
    set_2 (set): Another set of elements.

Returns:
    set: A new set containing the common elements of the two input sets.
'''


def common_elements(set_1, set_2):
    mySet = set()

    for i in set_1:
        for j in set_2:
            if i == j:
                mySet.add(i)

    return mySet
