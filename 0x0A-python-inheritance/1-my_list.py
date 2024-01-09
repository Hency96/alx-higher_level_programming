#!/usr/bin/python3
""" inherits from the list class"""


class MyList(list):
    """class that inherits from parent class list"""
    def print_sorted(self):
        """printing a sorted list"""
        print(sorted(self))
