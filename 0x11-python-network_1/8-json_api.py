#!/usr/bin/python3
"""Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    input = argv[1] if len(argv) > 1 else ""

    response = requests.post(url, data={"q": input})

    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
