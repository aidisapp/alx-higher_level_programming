#!/usr/bin/python3
"""
This Python script to send a POST request to a URL with an email parameter,
and display the body of the response (decoded in utf-8).

Requirements:
- The URL and email must be passed as command-line arguments
- Dependencies: urllib, sys
"""

from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
