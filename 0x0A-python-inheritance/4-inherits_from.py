#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Check whether obj is a subclass of a_class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
