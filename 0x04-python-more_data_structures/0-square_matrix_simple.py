#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square = []

    for row in matrix:
        row_matrix = []
        for i in row:
            row_matrix.append(i ** 2)
        square.append(row_matrix)
    return square
