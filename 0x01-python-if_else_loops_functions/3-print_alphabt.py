#!/usr/bin/python3
'''
This script outputs the lowercase alphabet,
excluding the letters 'e' and 'q'.
'''
for num in range(97, 123):
    if chr(num) == 'e' or chr(num) == 'q':
        pass
    else:
        print('{}'.format(chr(num)), end="")
