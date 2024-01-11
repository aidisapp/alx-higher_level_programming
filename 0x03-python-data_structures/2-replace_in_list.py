#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list


if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5]
    idx = 2
    new_element = 10
    result = replace_in_list(my_list, idx, new_element)
    print("Updated list:", result)
