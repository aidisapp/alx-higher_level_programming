#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            count += 1
        except IndexError:
            continue
    print()
    return(count)
