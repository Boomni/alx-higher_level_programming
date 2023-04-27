#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
RESPONSE=$(curl -sI "$1" | grep HTTP | awk '{print $2}')
if [ "$RESPONSE" -eq 200 ]; then
	curl -s "$1" -X GET
fi
