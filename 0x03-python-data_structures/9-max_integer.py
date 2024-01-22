#!/usr/bin/python3
'''
Determines the largest integer in a list.
'''


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        max = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
