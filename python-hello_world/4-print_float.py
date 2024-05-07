#!/usr/bin/python3

number = 3.14159

decimal_places = 2
formatted_number = "{:.{}f}".format(number, decimal_places)
print(f"Float: {formatted_number}")
