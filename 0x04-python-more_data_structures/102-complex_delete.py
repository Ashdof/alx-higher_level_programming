#!/use/bin/python3

def complex_delete(a_dictionary, value):
    """
    Delete a key with a specific value

    Args:
    a_dictionary: the dictionary object
    value: the value in the dictionary object to be deleted
    """
    keys = list(a_dictionary.keys())

    for key in keys:
        if key == a_dictionary.get(key):
            del a_dictionary[key]

    return (a_dictionary)
