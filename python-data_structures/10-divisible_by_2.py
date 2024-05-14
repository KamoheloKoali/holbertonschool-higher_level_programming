#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list((my_list))
    for num in new_list:
        if num % 2 == 0:
            new_list[new_list.index(num)] = True
        else:
            new_list[new_list.index(num)] = False
    return new_list
