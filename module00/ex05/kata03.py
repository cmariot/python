kata = "The right format"


def print_str(s: str):
    """
    Print the string
    """
    if (not isinstance(s, str)):
        print("ERROR, the argument is not a string")
        exit(1)
    str_len = len(s)
    if (str_len == 0):
        print("The string is empty")
    elif (str_len > 42):
        print("ERROR, the string is too long")
    else:
        print(f"{s:->42}", end="")


print_str(kata)
