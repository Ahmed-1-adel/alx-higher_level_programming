#!/usr/bin/python3

"""module with method is_kind_of_class"""

def is_kind_of_class(obj, a_class):
    """ Check if an object is an instance or inherited instance of a class
    Args:
        obj (any): The object to check
        a_class (type) : Method to check in obj or not
    """
    
    return isinstance(obj, a_class)
