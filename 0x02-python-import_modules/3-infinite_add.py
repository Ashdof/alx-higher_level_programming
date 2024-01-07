#!/usr/bin/python3

if __name__ == "__main__":
    """A program that prints the addition of all arguments"""
    import sys

    ans = 0
    args = sys.argv
    n = len(args) - 1

    for i in range(n):
        ans += int(args[i + 1])
    print("{}".format(ans))
