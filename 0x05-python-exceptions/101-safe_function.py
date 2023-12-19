#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        value = fct(*args)
        return value
    except Exception as exc:
        print("Exception: {}".format(exc), file=sys.stderr)
        return None
