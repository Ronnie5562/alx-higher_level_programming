#!/bin/bash
# script that makes a req to 0.0.0.0:5000/catch_me and server responds You got me!
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
