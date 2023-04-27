#!/bin/bash
# Write a Bash script that takes in a URL, sends a GET request to the URL
curl -sfL "$1" -X GET
