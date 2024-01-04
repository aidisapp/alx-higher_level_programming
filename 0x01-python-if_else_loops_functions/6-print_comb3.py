#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        end = ", " if (i < 9 or j < 8) else "\n"
        print("{:02d}".format(i * 10 + j), end=end)
