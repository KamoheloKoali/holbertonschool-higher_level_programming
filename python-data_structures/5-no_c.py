#!/usr/bin/python3
def no_c(my_string):
    index = 0
    for char in my_string:
        if char == "C" or char == "c":
            new = list((my_string))
            new.pop(index)
            return str(new)
        index += 1
    return my_string
