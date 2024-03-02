#!/home/lwssim/my_env/netw/bin/python3
"""list 10 commits (from the most recent to oldest) from a {repo, user}
"""


import requests
from sys import argv


if __name__ == "__main__":
    repository = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]

        print(f"{sha}: {author_name}")
