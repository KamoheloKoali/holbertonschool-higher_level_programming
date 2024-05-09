#!/usr/bin/python3
def print_last_digit(number):
    last_num = abs(number) % 10
    if number < 0:
        last_num = -abs(last_num)
    return last_num

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
