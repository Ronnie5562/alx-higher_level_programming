#!/bin/bash
# sends a request to a URL passed as an argument, and disply stat code
curl -s -o /dev/null -w "%{http_code}" "$1"
