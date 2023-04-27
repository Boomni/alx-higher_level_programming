#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response

STATUS=$(curl -s -w '%{http_code}' -o /dev/null "$1")
if [ "$STATUS" -eq 200 ]; then
	curl -s "$1"
fi
