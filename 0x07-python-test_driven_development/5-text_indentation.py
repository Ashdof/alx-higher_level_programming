#!/usr/bin/python3
"""A module with a function that indents a strings with newline characters"""


def text_indentation(text):
    """
    Print two new lines after selected punctuations

    Args:
        text (str): the string text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        m = s.split(d)
        s = ""
        for i in m:
            i = i.strip(" ")
            s = i + d if s == "" else s + "\n\n" + i + d

    print(s[:-3], end="")
