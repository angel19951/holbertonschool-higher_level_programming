#!/bin/bash/python3


def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return None
    return length, sentence[0]
