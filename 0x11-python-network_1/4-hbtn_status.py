#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status
"""


import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    if response.status_code == 200:
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
