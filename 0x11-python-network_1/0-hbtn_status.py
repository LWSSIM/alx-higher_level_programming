#!/usr/bin/python3
"""Fetchs from https://alx-intranet.hbtn.io/status
(using urlib)
"""


import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()
        dec_content = body.decode("utf-8")

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", dec_content)
