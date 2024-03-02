#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and uses the GitHub API to display your id
"""


import requests
from sys import argv

if __name__ == "__main__":
    un = argv[1]
    ps = argv[2]

    url = f"http://api.github.com/users/{un}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {ps}",
    }

    response = requests.get(url, headers=headers)
    print(response.json().get("id"))
