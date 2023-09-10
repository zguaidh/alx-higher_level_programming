#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    prog_n = sys.argv[0]
    args = sys.argv[1:]
    add = 0
    for i in args:
        add += int(i)
    print(add)
