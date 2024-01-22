#!/usr/bin/python3
'''
Updates an element in a list at a particular
position without altering the original list
'''


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        newList = []
        for i in my_list:
            newList.append(i)

        newList[idx] = element
        return newList
