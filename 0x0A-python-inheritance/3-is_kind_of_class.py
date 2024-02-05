#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Check whther obj is a subclass of a_class"""

    if isinstance(obj, a_class) or type(obj) == a_class:
        return True

    return False
