#!/usr/bin/python3
'''
Displays the integers of a list in reverse order.
'''


def print_reversed_list_integer(my_list=None):
    if my_list is None:
        my_list = []

    for i in reversed(my_list):
        print("{:d}".format(i))
