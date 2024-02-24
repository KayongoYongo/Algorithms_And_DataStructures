#!/usr/bin/python3

def common_elements(set_1, set_2):
    common = []

    for s in set_1:
        if s in set_2:
            common.append(s)

    return common
