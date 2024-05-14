#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end="")
            if row.index(element) == len(row) - 1:
                print()
            else:
                print(" ", end="")
    return None
