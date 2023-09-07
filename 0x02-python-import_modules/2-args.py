#!/usr/bin/python3
#if __name__ == __main__:
import sys
prog_n = sys.argv[0]
args = sys.argv[1:]
number = len(args)
if len != 1:
    print("{} argument:".format(number))
    for arg in args:
        print("{}: {}".format(number, arg))
