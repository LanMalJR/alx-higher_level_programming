#!/usr/bin/python3
'''
The code creates a list indicating whether
each integer in the input is even.
'''


def divisible_by_2(my_list=[]):
    return [True if num % 2 == 0 else False for num in my_list]


'''
Print the results
'''
for i in range(len(list_result)):
    print("{:d} {} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))


