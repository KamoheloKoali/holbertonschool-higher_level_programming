#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
        return
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end="")
            if row.index(element) < len(row) - 1:
                print(" ", end="")
            else:
                print()
