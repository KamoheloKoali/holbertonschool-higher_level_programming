#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for item in range(x):
        try:
            print(f"{my_list[item]}", end="")
        except IndexError:
            break
        else:
            printed += 1
    print()
    return printed
