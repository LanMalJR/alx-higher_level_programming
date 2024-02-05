#!/usr/bin/python3
'''
Prints the initial x integers from a list,
filtering non-integer elements.
'''


def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print('{:d}'.format(my_list[i]), end='')
                count += 1
        print()
        return count
    except IndexError:
        raise