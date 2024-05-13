#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last = -1
    for num in my_list:
        print("{:d}".format(my_list[last]))
        last += - 1
