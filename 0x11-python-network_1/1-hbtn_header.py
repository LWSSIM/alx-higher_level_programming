#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response.
"""

from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        if "X-Request-Id" in response.headers:
            id = response.headers["X-Request-Id"]
            print(id)
