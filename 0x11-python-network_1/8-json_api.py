#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) <= 1:
        params = {'q': ""}
    else:
        params = {'q': sys.argv[1]}

    response = requests.get(url, data=params)
    try:
        data = response.json()
        if data:
            for user in data:
                print(f"[{user['id']}] {user['name']}")
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
