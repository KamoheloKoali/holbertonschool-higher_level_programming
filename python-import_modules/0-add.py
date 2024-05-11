#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{a} + {b} = {add}".format(a = a, b = b, add = add(a, b)))
