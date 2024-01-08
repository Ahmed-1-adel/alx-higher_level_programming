#!/usr/bin/python3
"""Module With class MyList"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Method that sorted a list"""
        print(sorted(list(self)))
