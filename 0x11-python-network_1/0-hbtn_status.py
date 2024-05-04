#!/usr/bin/python3
"""
This Python script to retrieve data from https://alx-intranet.hbtn.io/status
We'll be utilizing the urllib package for HTTP requests
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
