#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cound = len(sys.argv)
    if cound == 1:
        print("{} arguments.".format(cound - 1))
    elif cound == 2:
        print("{} argument:".format(cound - 1))
    else:
        print("{} arguments:".format(cound - 1))
    for i in range(1, cound):
        print("{}: {}".format(i, sys.argv[i]))
