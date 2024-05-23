#!/usr/bin/python3

"""
2-matrix_divided.py divides all elements of a matrix

Examples:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix_divided([[10, 20, 30], [40, 50, 60]], 2.5)
    [[4.0, 8.0, 12.0], [16.0, 20.0, 24.0]]

4    >>> matrix_divided([[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]], 2)
    [[0.75, 1.25, 1.75], [2.25, 2.75, 3.25]]

    >>> matrix_divided([[1.2, 2.4, 3.6], [4.8, 6.0, 7.2]], 1.2)
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

    >>> matrix_divided([[8, 16, 24]], 8)
    [[1.0, 2.0, 3.0]]

    >>> matrix_divided([[5]], 2)
    [[2.5]]
"""


def matrix_divided(matrix, div):
    """
    matrix_divided divides all elements of a matrix and returns
    a new matrix

    Args:
        matrix (list): first parameter
        div (int or float): second parameter

    Returns:
        A new matrix after division of all elements in provided
        matrix

    Raises:
        TypeError: if matrix contains data types other than int and float
        TypeError: if not all the rows in the matrix are equal
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new_matrix = []
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
