#!/usr/bin/env bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
# -The size must be displayed in bytes
URL="$1"
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2
