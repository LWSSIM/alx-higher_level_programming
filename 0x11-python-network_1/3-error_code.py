#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
    and displays the body of the response
    (decoded in utf-8).
"""

from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
