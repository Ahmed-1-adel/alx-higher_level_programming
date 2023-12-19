#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    isInt = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        isInt = False
    return isInt

