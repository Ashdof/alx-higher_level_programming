#!/usr/bin/python3
"""Solution for task 6"""


def find_peak(list_of_integers):
    """Get the peak

    Description:
    This function returns the peak in a list of
    unsorted integers

    Args:
    list_of_integer (int): the list of integers
    to obtain the peak value or values

    Returns:
    The peak value(2) or None if no peak is found
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)

    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
