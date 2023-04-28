#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
    - using the package urllib
    - body of response is displayed in tabulation before -
"""


import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as request:
        response = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('UTF-8')))
