#!/usr/bin/python3


def best_score(a_dictionary):
    if bool(a_dictionary) == False:
        return None
    else:
        return (max(a_dictionary, key=a_dictionary.get))
