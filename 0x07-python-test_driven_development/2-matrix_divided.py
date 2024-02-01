#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function,
matrix_divided(matrix, divisor).
"""


def matrix_divided(matrix, divisor):
    """Divides all elements in the matrix by divisor"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if row_size is None:
            row_size = len(row)
        elif row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(divisor) is not int and type(divisor) is not float:
        raise TypeError("divisor must be a number")
    if divisor == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / divisor, 2) for element in row] for row in matrix]
