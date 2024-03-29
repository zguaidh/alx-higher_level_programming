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

    response = requests.get(url, params=params)
    try:
        data = response.json()
        if isinstance(eval(data), dict):
            if data:
                for user in data:
                    print(f"[{user['id']}] {user['name']}")
            else:
                print('No result')
        else:
            print('Not a valid JSON')
    except Exception:
        pass
