#!/bin/bash
# This Script sends a GET request to a given URL with a header variable
curl -s -H "X-School-User-Id":98 "$1"
