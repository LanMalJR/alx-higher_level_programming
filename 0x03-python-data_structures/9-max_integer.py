#!/usr/bin/python3
'''
Determines the largest integer in a list.
'''


def max_integer(my_list=[]):
    largest = 0

    if my_list:
        for element in my_list:
            if element > largest:
                largest = element

        return largest
    else:
        return None
