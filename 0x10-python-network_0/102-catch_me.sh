#!/bin/bash
# This Script makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!"
curl -sX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -L -H "Origin: sample.com"
