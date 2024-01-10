#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add all unique integers

    Args:
    my_list: the list of integers
    """
    ans = 0
    uniques = []

    for i in sorted(set(my_list)):
        uniques.append(i)
    for i in uniques:
        ans += i

    return ans
