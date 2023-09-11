#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(tuple_a)
    length_b = len(tuple_b)

    if length_a == 0 and length_b == 0:
        return (0, 0)
    elif length_a == 0 and length_b != 0:
        if length_b == 1:
            return (tuple_b[0], 0)
        elif length_b > 1:
            return tuple_b[:2]
    elif length_b == 0 and length_a != 0:
        if length_a == 1:
            return (tuple_a[0], 0)
        elif length_a > 1:
            return tuple_a[:2]
    elif length_a == 1 and length_b == 1:
        return ((tuple_a[0] + tuple_b[0]), 0)
    elif length_a == 1:
        a = tuple_a[0]
        c, d = tuple_b[:2]
        x = a + c
        y = d
        tu = x, y
        return tu
    elif length_b == 1:
        a, b = tuple_a[:2]
        c = tuple_b[0]
        x = a + c
        y = b
        tu = x, y
        return tu
    else:
        a, b = tuple_a[:2]
        c, d = tuple_b[:2]
        x = a + c
        y = d + b
        tu = x, y
        return tu


'#def add_tuple(tuple_a=(), tuple_b=()):'
'#    a = tuple_a[:2]'
'#    b = tuple_b[:2]'
'#    x = sum(a) + sum(b)'
'#    y = tuple_a.get(1, 0) + tuple_b.get(1, 0)'
'#    return (x, y)'
