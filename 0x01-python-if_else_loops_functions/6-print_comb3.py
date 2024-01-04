#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        end = "\n" if i == 9 and j == 9 else ", "
        print("{:02d}, {:02d}".format(i, j), end=end)
