#!/usr/bin/python3
def print_last_digit(number):
    last_num = abs(number) % 10
    if number < 0:
        last_num = -abs(last_num)
    print(last_num)
