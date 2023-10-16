#!/usr/bin/python3
""" Module for a program that parses from the stdin"""


from sys import stdin


total_size = 0
lines_num = 0
status_code = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
        }


def print_stdout():
    """method that prints the result after computing metrics"""
    print("File size: {}".format(total_size))
    for key, value in status_code.items():
        if value > 0:
            print("{:s}: {:d}".format(key, value))


try:
    for line in stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            total_size += int(tokens[-1])
            code = tokens[-2]
            if code in status_code:
                status_code[code] += 1
        lines_num += 1

        if lines_num % 10 == 0:
            print_stdout()
    print_stdout()

except KeyboardInterrupt:
    print_stdout()
