#!/usr/bin/python3

def no_c(my_string):
    mod_string = ""

    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        else:
            mod_string += char

    return mod_string
