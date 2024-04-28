#!/usr/bin/env bash
# send a GET request and print the body of the response message
curl -sfL "$1" -X GET
