#!/bin/bash
# Script that takes in a URL, sends a request to that URL, 
length=$(curl -sI "$1" | grep -i Content-Length | cut -d " " -f2)
echo $length