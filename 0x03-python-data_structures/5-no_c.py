#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all occurrences of c and C

    my_string: a string
    """
    new_str = ""

    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        new_str += i

    return new_str
