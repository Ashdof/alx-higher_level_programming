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

    vals = list_of_integers[:]
    size = len(vals)

    if size == 1:
        return vals[0]
    else:
        if vals == [] or vals == "None":
            return "None"
        else:
            return max(vals)

    mid = int(size / 2)
    peak = vals[mid]

    if peak > vals[mid - 1] and peak > vals[mid + 1]:
        return peak
    elif peak < vals[mid - 1]:
        return find_peak(vals[:mid])
    else:
        return find_peak(vals[mid + 1:])
