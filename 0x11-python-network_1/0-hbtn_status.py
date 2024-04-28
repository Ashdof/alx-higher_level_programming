#!/usr/bin/python3
"""Fetches status information from https://intranet.hbtn.io/status.
the urlib package
"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as stat:
        content = stat.read()

        print("Body response:")
        print(f"\t- type: {content}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
