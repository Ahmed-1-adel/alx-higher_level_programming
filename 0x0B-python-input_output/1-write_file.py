#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'r', encoding="UTF-8") as file:
        return len(list(file))
