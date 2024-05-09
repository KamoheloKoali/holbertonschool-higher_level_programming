#!/usr/bin/python3
def islower(c):
    char = ord(c)
    for i in range(97, 123):
        if char == i:
            return True
    return False
