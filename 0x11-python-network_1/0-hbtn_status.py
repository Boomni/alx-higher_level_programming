#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
    - using the package urllib
    - body of response is displayed in tabulation before -
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        response = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
