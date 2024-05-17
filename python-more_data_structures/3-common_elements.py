#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for item in set1:
        if item in set2:
            new_set.add(item)
    return new_set
