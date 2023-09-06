#!/usr/bin/python3
def remove_char_at(str, n):
    if 0 <= n < len(str):
        ls = list(str)

        del ls[n]
        new_str = ''.join(ls)
        return new_str
    else:
        return(str)
