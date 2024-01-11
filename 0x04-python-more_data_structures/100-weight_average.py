#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Compute the weighted average

    Args:
    my_list: a list of integers

    Return: the weighted average
    """
    if my_list and len(my_list):
        num = 0
        denom = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            denom += (tup[1])
        return (num/denom)

    return 0
