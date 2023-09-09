#!/usr/bin/python3
#if __name__ == __main__:
import sys
prog_n = sys.argv[0]
args = sys.argv[1:]
number = len(args)

if number == 1:
    print("{} argument:".format(number))
    for arg in args:
        print("{}: {}".format(number, arg))
elif number > 1:
    print("{} arguments:".format(number))
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
else:
    print("{} arguments.".format(number))
