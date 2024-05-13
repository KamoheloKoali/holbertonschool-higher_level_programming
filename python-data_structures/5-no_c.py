#!/usr/bin/python3
def no_c(my_string):
    index = 0
    for char in my_string:
        if char == "C" or char == "c":
            new_string = " "
            new = list((my_string))
            new.pop(index)
            for item in new:
                new_string += item
            return new_string
        index += 1
    return my_string
