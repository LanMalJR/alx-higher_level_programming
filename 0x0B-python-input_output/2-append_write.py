#!/usr/bin/python3
'''
Contains the function append_write
'''


def append_write(filename='', text=''):
    '''
    Appends a string at the end of a file
    '''
    with open(filename, 'a') as file:
        numOfCharacters = len(text)
        file.write(text)

    return numOfCharacters
