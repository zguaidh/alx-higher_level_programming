#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challeng

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""


import requests
import sys


if __name__ == '__main__':
    url = "https://developer.github.com/v3/repos/commits/"
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
