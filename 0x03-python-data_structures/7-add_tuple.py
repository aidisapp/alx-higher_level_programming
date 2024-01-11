#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    result_tuple = (a[0] + b[0], a[1] + b[1])
    return (result_tuple)


if __name__ == "__main__":
    # Example usage
    tuple_a = (1, 2)
    tuple_b = (3, 4)
    result = add_tuple(tuple_a, tuple_b)
    print(result)
