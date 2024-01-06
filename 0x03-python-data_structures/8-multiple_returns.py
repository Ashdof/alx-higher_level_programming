#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Return length of string and first character as a tuple

    sentence: a string
    """
    n = len(sentence)

    if n == 0:
        return 0, None

    return n, sentence[0]
