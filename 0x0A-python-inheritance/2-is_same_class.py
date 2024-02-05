#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Check whether obj is an instance of a_class"""

    if type(obj) == a_class:
        return True
    else:
        return False
