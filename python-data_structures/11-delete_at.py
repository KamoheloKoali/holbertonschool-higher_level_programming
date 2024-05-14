#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if not my_list:
        return my_list
    if idx >= 0 and idx < len(my_list):
        for item in my_list:
            if item != my_list[idx]:
                new_list.append(item)
        return new_list
    return my_list
