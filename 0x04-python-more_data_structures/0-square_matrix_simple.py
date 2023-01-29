#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list_2 = []
    for x in matrix:
        list_1 = []
        for y in x:
            list_1.append(y * y)
        list_2.append(list_1)
    return list_2