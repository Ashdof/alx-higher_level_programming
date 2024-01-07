#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv
    n = len(args)

    if n < 2:
        print("{:d} arguments".format(0))
    elif n == 2:
        n -= 1
        print("{:d} argument".format(n))
        print("{:d}: {}".format(n, args[n]))
    else:
        n -= 1
        print("{:d} arguments".format(n))

        for i in range(1, n + 1):
            print("{:d}: {}".format((i), args[i]))
