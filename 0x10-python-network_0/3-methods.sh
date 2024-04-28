#!/usr/bin/env bash
# display all the HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
