#!/usr/bin/python3
def no_c(my_string):
    listAllChars = list(my_string)
    for char in listAllChars:
        if char == "c" or char == "C":
            listAllChars.remove(char)
        else:
            return("".join(listAllChars))
    