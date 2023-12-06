#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        n = 0
        dn = 0
        for tup in my_list:
            n += (tup[0] * tup[1])
            dn += (tup[1])
        return (n/dn)
    return 0
