#!/usr/bin/python3

if __name__ == "__main__":
    """
    A program that prints number of and lists of arguments
    """
    import sys

    args = sys.argv
    n = len(args) - 1

    if n == 0:
        print("{:d} arguments.".format(0))
    elif n == 1:
        print("{:d} argument:".format(n))
    else:
        print("{:d} arguments:".format(n))

    for i in range(n):
        print("{:d}: {}".format(i + 1, args[i + 1]))
