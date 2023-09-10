#!/usr/bin/python3

def _import(mod, var):
    with open(f'{mod}.py', 'r') as src_f:
        src_c = src_f.read()

    global_dic = {}

    return global_dic.get(var)


if __name__ == "__main__":
    value = _import(variable_load_5, a)

    print(value)
