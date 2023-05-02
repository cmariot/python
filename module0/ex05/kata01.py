# Dictonary
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}


def check_if_str(d: dict):
    """
    Check if the dictionary contains only strings
    """
    for key, value in d.items():
        if (not isinstance(key, str) or not isinstance(value, str)):
            print("ERROR, the dictionary contains non-string value(s)")
            exit(1)
    return


def print_dict(d: dict):
    """
    Print the dictionary
    """
    if (len(d) == 0):
        print("The dictionary is empty")
    else:
        check_if_str(d)
        for key, value in d.items():
            print(f"{key} was created by {value}")


print_dict(kata)
