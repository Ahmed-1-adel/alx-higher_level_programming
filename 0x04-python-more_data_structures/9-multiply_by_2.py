#!/usr/bin/python3
def multiply_by_2(a_dictionary):
  for keys in (sorted(a_dictionary.keys())):
    new_dict = (a_dictionary[keys])
    print("{}: {}".format(keys, new_dict * 2))
