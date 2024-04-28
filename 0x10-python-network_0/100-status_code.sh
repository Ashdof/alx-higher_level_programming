#!/usr/bin/env bash
# send a request passed as argument and display only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
