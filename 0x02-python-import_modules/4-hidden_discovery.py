#!/usr/bin/python3

'''
This program displays the names that are defined
in the compiled module hidden_4.pyc.
'''

import hidden_4


def main():
    functions = dir(hidden_4)

    for function in sorted(functions):
        if not function.startswith('__'):
            print(function)


if __name__ == '__main__':
    main()
