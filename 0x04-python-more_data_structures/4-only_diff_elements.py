#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    not_common = []

    for i in set_1:
        if i not in set_2:
            not_common.append(i)

    for j in set_2:
        if j not in set_1:
            not_common.append(j)

    return not_common
