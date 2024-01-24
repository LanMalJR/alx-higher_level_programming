#!/usr/bin/python3
'''
This function converts a Roman numeral to an integer.

Parameters:
    roman_string (str): A string representing a Roman numeral.

Returns:
    int: The integer equivalent of the Roman numeral
    or 0 if the input is not a valid Roman numeral.
'''


def roman_to_int(roman_string):
    roman_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    total = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and roman_nums[roman_string[i]]
        < roman_nums[roman_string[i + 1]]:
            total -= roman_nums[roman_string[i]]
        else:
            total += roman_nums[roman_string[i]]

    return total
