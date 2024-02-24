#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    k = list(a_dictionary.keys())
    v = list(a_dictionary.values())

    return k[v.index(max(v))]
