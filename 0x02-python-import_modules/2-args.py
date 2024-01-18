!/usr/bin/python3

'''
The script displays both the count
and the list of its arguments.
'''
import sys


def main():
    argc = len(sys.argv) - 1
    print_arguments_info(argc)

    for i, arg in enumerate(sys.argv[1:], start=1):
        print_argument(i, arg)

def print_arguments_info(argc):
    arg_str = "{:d} argument"
    arg_str += '' if argc == 1 else 's'
    arg_str += ':'
    print(arg_str.format(argc))

def print_argument(index, arg):
    print("{:d}: {:s}".format(index, arg))

if __name__ == "__main__":
    main()
