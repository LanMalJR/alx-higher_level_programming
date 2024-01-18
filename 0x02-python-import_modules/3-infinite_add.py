#!/usr/bin/python3

'''
This program outputs the sum of all provided arguments.
'''

import sys


def main():

    argv = sys.argv
    length = len(argv) - 1
    sum = 0

    for i in range(1, length + 1):
        sum += int(argv[i])

    print(sum)


if __name__ == '__main__':
    main()
