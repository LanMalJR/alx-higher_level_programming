#!/usr/bin/python3
'''
# Defines the function class_to_json, which 
converts a Python class instance to JSON format
'''


def class_to_json(obj):
    '''
    Returns the dictionary description with simple data for
    JSON serialization of an object
    '''
    return obj.__dict__
