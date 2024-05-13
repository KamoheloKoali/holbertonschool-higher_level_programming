#!/usr/bin/python3
def no_c(my_string):
    index = 0
    for char in my_string:
        if char == "C" or char == "c":
            my_string[index] = ""
        index += 1
    return my_string
