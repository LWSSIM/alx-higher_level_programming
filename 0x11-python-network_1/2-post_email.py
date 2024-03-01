#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response
    (decoded in utf-8)
"""


from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode("utf-8")

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode("utf-8")

    print(body)
