#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Find multiples of 2 in a list

    my_list: a list of integers
    """
    new_list = []

    if my_list == []:
        return None
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
