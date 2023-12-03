#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for numofList in matrix:
      for num in numofList:
          print("{:d}".format(num), end=" ")
      print()
