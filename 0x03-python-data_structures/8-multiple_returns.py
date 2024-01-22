#!/usr/bin/python3
'''
Produces a tuple containing the length
of a string and its initial character.
'''


def multiple_returns(sentence):

    strLength = len(sentence)

    if strLength:
        firstChar = sentence[0]
    else:
        firstChar = None

    returnTuple = (strLength, firstChar)

    return returnTuple