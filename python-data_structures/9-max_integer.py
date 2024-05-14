#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    largest_num = my_list[0]
    for number in my_list:
        if number > largest_num:
            largest_num = number
    return largest_num
