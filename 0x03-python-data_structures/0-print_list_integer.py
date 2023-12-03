#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if len(my_list) == 0:
      print("Empty List")
    else:
      for num in my_list:
          print("{}".format(num))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)