kata = "The right format"


def print_str(s: str):
    """
    Print the string
    """
    if (not isinstance(s, str)):
        print("ERROR, the argument is not a string")
    elif (len(s) > 42):
        print("ERROR, the string is too long")
    else:
        print(f"{s:->42}", end="")


print_str(kata)
