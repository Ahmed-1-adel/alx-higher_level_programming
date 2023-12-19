#!/usr/bin/python3
def safe_print_list(my_list = [], x = 0):
    """ Searching in My_list, If found the same number in val x or not
        and Return number the list 
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        return None
    print()
    return count
