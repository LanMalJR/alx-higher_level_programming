#!/usr/bin/python3
'''
This function replaces all occurrences
of an element by another in a new list.

Parameters:
my_list (list): A list of elements.
search (object): The element to search for in the list.
replace (object): The element to replace the found elements with.

Returns:
list: A new list where all occurrences of the search
element are replaced with the replace element.
'''


def search_replace(my_list, search, replace):
    new_list = [replace if elem == search else elem for elem in my_list]

    return new_list
