#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Print all elements of a list

    my_list: a list of elements
    """

    for i in range(len(my_list)):
        print('{:d}'.format(my_list[i]))
