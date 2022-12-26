#!/usr/bin/python3
"""A module with a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """Print name

    Description:
        This function prints the full name of a person passed via its
        arguments

    Returns:
        The name of the person in the form <first name> <last name>
    """
    msg_f = "first_name must be a string"
    msg_l = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(msg_f)

    if not isinstance(last_name, str):
        raise TypeError(msg_l)

    print("My name is {} {}".format(first_name, last_name))
