#!/bin/bash
# Script that takes in a URL, sends a request to that URL, 
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
