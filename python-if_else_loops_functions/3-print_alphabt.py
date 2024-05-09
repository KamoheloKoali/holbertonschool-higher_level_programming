#!/usr/bin/python3
for i in range(97, 123):
    if "{:c}".format(i) == "e" or "{:c}".format(i) == "q":
        continue
    print("{:c}".format(i), end="")
