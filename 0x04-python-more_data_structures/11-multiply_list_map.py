#!/usr/bin/python3
def multiply_list_map(my_list=None, number=0):
    return [(x := x * number) for x in (my_list or [])]

