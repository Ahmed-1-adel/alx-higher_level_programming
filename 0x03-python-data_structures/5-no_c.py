#!/usr/bin/python3
def no_c(my_string):
    lisallchars = list(my_string)
    for char in lisallchars:
        if char == 'c' or char == 'C':
            lisallchars.remove(char)
    return("".join(lisallchars))
