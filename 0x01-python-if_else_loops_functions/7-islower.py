#!/usr/bin/python3
'''
This script features a function that verifies
the presence of a lowercase character.
'''
def islower(c):
    if ord(c) <= 122 and ord(c) >= 97:
        return True
    else:
        return False
