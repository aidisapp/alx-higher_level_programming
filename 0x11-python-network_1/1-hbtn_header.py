#!/usr/bin/python3
"""
This is a Python script to fetch the value of the
x-Request-Id variable from a given URL's response header

Dependencies: urllib, sys
"""

from sys import argv
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('x-Request-Id'))
