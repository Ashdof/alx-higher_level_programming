#!/usr/bin/python3
"""A module with a function that implements indentiation in strings"""


def text_indentation(text):
    """Indent texts

    Description:
        This function prints a text with 2 new lines after each of these
        characters: ., ? and :

    Args:
        text (string): the argument

    Raises:
        TypeError if text is not a string

    Return:
        Nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
