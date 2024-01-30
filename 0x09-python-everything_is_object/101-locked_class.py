#!/usr/bin/python3
""" LockedClass"""


class LockedClass:
    """A locked class

    Description:
        this is a class that prevents the user from dynamically
        creating new instance attributes
    """

    __slots__ = ['first_name']
