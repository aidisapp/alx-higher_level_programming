#!/usr/bin/python3
"""
This script defines a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a number that's greater than both its left and right neighbors.
    """
    if len(list_of_integers) == 0:
        return None

    new_list = list_of_integers
    beg = 0
    end = len(new_list) - 1

    if new_list[beg] >= new_list[beg + 1]:
        return new_list[beg]
    if new_list[end] >= new_list[end - 1]:
        return new_list[end]

    while beg <= end:
        mid = (beg + end) // 2
        if new_list[mid] >= new_list[mid - 1] and new_list[
                                                mid] >= new_list[mid + 1]:
            return new_list[mid]
        elif new_list[mid] < new_list[mid - 1]:
            end = mid - 1
        else:
            beg = mid + 1
