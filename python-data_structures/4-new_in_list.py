#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = list((my_list))
    if idx > -1 and idx < len(copy):
        copy[idx] = element
    return copy
