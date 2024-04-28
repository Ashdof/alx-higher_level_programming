#!/usr/bin/env bash
# send  request to a given url and display the size of the body of the response message in bytes
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
