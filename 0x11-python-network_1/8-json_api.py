#!/usr/bin/python3
"""
Send POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    resp = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = resp.json()
        if response == {}:
            print("No result")
        else:
            print("[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
