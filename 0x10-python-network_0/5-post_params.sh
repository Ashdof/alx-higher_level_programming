#!/usr/bin/env bash
# send a POST request and display the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
