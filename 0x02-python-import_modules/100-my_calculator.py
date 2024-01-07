#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def compute_args(args):
    n = len(args) - 1

    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(args[1])
    op = args[2]
    b = int(args[3])

    if op == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
    elif op == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
    elif op == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
    elif op == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    compute_args(sys.argv)
