#!/usr/bin/python3
'''
This function updates a dictionary by replacing or adding a key-value pair.

Parameters:
    a_dictionary (dict): The dictionary to update.
    key (hashable): The key to add or update.
    value (object): The value to associate with the key.

Returns:
    dict: The updated dictionary.
'''


def update_dictionary(a_dictionary, key, value):
    # If the key already exists, update its value
    if key in a_dictionary:
        a_dictionary[key] = value
    # Otherwise, add the new key-value pair
    else:
        a_dictionary.update({key: value})

    return a_dictionary
