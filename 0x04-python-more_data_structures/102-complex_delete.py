#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ky = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            ky.append(k)
    for key in ky:
        del a_dictionary[k]
    return a_dictionary
