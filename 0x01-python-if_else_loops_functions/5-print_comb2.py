#!/usr/bin/python3
for b in range(100):
    print("{:02d}".format(b), end=", " if b < 99 else "\n")
