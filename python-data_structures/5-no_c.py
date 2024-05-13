#!/usr/bin/python3
def no_c(my_string):
    index = 0
    new_string = ""
    new = list((my_string))
    for char in my_string:
        if char == "C" or char == "c":
            new.pop(index)
        else:
            index += 1
    for item in new:
        new_string += item
    return new_string
