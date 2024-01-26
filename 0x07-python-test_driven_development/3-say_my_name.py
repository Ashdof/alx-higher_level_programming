#!/usr/bin/python3
"""A module with a function definition that prints a name"""


def say_my_name(first_name, last_name=""):
    """
    Print the name

    Args:
        first_name (string): the first param
        last_name (string): the second param
    """

    err_first_type = "first_name must be a string"
    err_last_type = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(err_first_type)

    elif not isinstance(last_name, str):
        raise TypeError(err_last_type)

    print(f"My name is {first_name} {last_name}")
