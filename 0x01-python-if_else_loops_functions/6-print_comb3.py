#!/usr/bin/python3
x = 0
y = 0

for x in range(9):
    for y in range(x + 1, 10):
        if x != y:
            print(x, end="")
            print(y, end="")
        elif x == y:
            pass
        elif x != 8 or y != 9:
            print(",", end="")
            print(" ", end="")
