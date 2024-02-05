#!/usr/bin/python3
'''
Retrieves an element from a list
similar to the process in C.
'''


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]
