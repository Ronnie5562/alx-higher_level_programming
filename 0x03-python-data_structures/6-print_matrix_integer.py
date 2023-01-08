#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for i in range(len(matrix[x])):
            print("{:d}".format(matrix[x][i), end="")
            if i != (len(matrix[x]) - 1):
                print(" ", end="")

        print("")
