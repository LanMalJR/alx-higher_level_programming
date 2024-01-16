#!/usr/bin/python3
'''
This script outputs the last digit of a randomly generated number
and informs you whether the digit falls between
6 and 0, is greater than 5, or is 0.
'''

import random
number = random.randint(-10000, 10000)
if number > 0:
    lastDigit = abs(number) % 10
else:
    lastDigit = (abs(number) % 10) * -1

print(f'Last digit of {number} is {lastDigit}', end=' ')

if lastDigit > 5:
    print('and is greater than 5')
elif lastDigit == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
