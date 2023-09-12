#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    import sys
    prog_name = sys.argv[0]
    args = sys.argv[1:]
    op = ['+', '-', '*', '/']
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if args[1] not in op:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if args[1] == '+':
                ADD = add(int(args[0]), int(args[2]))
                print("{} {} {} = {}".format(args[0], args[1], args[2], ADD))
            elif args[1] == '-':
                SUB = sub(int(args[0]), int(args[2]))
                print("{} {} {} = {}".format(args[0], args[1], args[2], SUB))
            elif args[1] == '*':
                MUL = mul(int(args[0]), int(args[2]))
                print("{} {} {} = {}".format(args[0], args[1], args[2], MUL))
            elif args[1] == '/':
                DIV = div(int(args[0]), int(args[2]))
                print("{} {} {} = {}".format(args[0], args[1], args[2], DIV))
