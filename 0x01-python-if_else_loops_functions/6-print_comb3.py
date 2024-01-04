#!/usr/bin/python3
for i in range(1, 10):
    for j in range(i + 1, 10):
        end = ", " if (i < 9 or j < 8) else "\n"
        print("{:d}, {:d}".format(i, j), end=end)
