#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
    displays the value of the variable X-Request-Id in the response header
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)

    if "X-Request-Id" in response.headers:
        id = response.headers["X-Request-Id"]
        print(id)
