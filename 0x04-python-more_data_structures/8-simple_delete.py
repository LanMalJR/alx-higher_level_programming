#!/usr/bin/python3
'''
This function deletes a key from a dictionary if it exists.

Parameters:
    a_dictionary (dict): The dictionary to modify.
    key (hashable, optional): The key to delete. Defaults to an empty string.

Returns:
    dict: The modified dictionary.
'''


def simple_delete(a_dictionary, key=""):
    keys = a_dictionary.keys()

    if key in keys:
        a_dictionary.pop(key)
        return a_dictionary
    else:
        return a_dictionary
