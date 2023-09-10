#!/usr/bin/python3
import hidden_4


def filter(module):
    all_attr = dir(module)
    user_attr = [attr for attr in all_attr if not attr.startswith("__")]
    return user_attr


if __name__ == "__main__":
    user_attr = filter(hidden_4)
    for attr in user_attr:
        print(attr)
