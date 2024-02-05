#!/usr/bin/python3
'''
This function returns a key with the biggest integer value.

Parameters:
    a_dictionary (dict): A dictionary with integer values.

Returns:
    str or None: A key associated with the biggest integer
    value or None if the dictionary is empty.
'''


def best_score(a_dictionary):
    if a_dictionary:
        maxValue = max(a_dictionary.values())
        maxValueKey = [key for key, value in a_dictionary.items()
                       if value == maxValue]
        return maxValueKey[0] if maxValueKey else None
    else:
        return None
