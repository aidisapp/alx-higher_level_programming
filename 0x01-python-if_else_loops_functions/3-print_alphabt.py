#!/usr/bin/python3
for r in range(97, 123):
    if chr(r) not in ["q", "e"]:
        print("{}".format(chr(r)), end="")
