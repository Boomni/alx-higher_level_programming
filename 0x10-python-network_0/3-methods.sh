#!/bin/bash
# Takes in URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep ALLOW | cut -d ' ' -f2-
