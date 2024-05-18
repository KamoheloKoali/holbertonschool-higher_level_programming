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


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
