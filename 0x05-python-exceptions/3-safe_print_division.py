#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = None
    except ZeroDivisionError:
        print("{:d} / {:d} = {}".format(a, b, result))
    finally:
      new_val = a / b
      print(print("{:d} / {:d} = {}".format(a, b, new_val)))
