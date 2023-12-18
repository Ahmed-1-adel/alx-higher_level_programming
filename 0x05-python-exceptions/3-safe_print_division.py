def safe_print_division(a, b):
    try:
        result = None
    except ZeroDivisionError:
        print("{:d} / {:d} = {}".format(a, b, result))
    finally:
      new_val = a / b
      print(print("{:d} / {:d} = {}".format(a, b, new_val)))


a = 12
b = 2
result = safe_print_division(a,b)

print("#########")

a = 12
b = 0
result = safe_print_division(a ,b)