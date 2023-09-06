#!/usr/bin/python3
def uppercase(str):
    upp = []
    for char in str:
        if char >= 'a' and char <= 'z':
            val = ord(char) - 32
            upp.append(chr(val))
        else:
            upp.append(char)
    STR = ''.join(upp)
    print("{}".format(STR))
