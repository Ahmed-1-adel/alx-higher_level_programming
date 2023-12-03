#!/usr/bin/python3
def no_c(my_string):
    lisAllChars = list(my_string)
    for char in lisAllChars:
        if char == 'c' or char == 'C':
            lisAllChars.remove(char)
    return("".join(lisAllChars))