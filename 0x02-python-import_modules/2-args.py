#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cound = len(sys.argv)
    if cound == 1:
        print("{} arguments.".format(cound - 1))
    elif cound == 2:
        print("{} argument:".format(cound - 1))
    else:
<<<<<<< HEAD
        print("{} argumetns:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))  
=======
        print("{} arguments:".format(cound - 1))
    for i in range(1, cound):
        print("{}: {}".format(i, sys.argv[i]))
>>>>>>> 8c77c232c9cdb82a743878435dc860bd8714e898
