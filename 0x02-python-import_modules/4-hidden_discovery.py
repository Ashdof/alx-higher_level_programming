#!/usr/bin/python3

if __name__ == "__main__":
    """A program that prints all names defined by hidden_4 module"""

    import hidden_4

    vals = dir(hidden_4)

    for val in vals:
        if val[:2] != '__':
            print("{}".format(val))
