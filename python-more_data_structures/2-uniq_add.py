#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique_elements = set((my_list))
    for num in unique_elements:
        result += num
    return result
