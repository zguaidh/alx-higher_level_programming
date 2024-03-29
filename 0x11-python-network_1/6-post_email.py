#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""


import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = ('email=' + email).encode('utf-8')
    response = requests.get(url, data=data)
    print(response.text)
