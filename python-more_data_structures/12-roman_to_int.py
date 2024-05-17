#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    roman_list = roman_dict.keys()
    prev_key = ""

    if not isinstance(roman_string, str) or not roman_string:
        return 0
    for letter in roman_string:
        if letter in roman_dict:
            for key in roman_list:
                if roman_list[0] != key:
                    prev_key = roman_list[roman_list.index(key) - 1]
                else:
                    prev_key = key
                if letter == key:
                    if roman_dict[key] <= roman_dict[prev_key]:
                        result += roman_dict[key]
                    else:
                        result -= roman_dict[key]
    return result
