#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    n = len(argv) - 1
    ops = ["+", "*", "-", "/"]
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op == '+':
        ans = add(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, ans))
    elif op == '-':
        ans = sub(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, ans))
    elif op == '*':
        ans = mul(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, ans))
    elif op == '/':
        ans = div(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, ans))
