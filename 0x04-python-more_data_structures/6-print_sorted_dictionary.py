#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary of ordered keys"""
    keys = []

    for k, v in a_dictionary.items():
        keys.append(k)

    keys.sort()
    for i in keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
