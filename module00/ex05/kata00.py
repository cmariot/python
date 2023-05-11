# A tuple of integers
kata = (8, 42, 100)


def check_if_int(t: tuple):
    """
    Check if the tuple contains only integers
    """
    for i in range(len(t)):
        if (not isinstance(t[i], int)):
            print("ERROR, the tuple contains non-integer value(s)")
            exit(1)
    return


def print_integer_tuple(t: tuple):
    """
    Print the tuple
    """
    tuple_len = len(t)
    if (tuple_len == 0):
        print("The tuple is empty")
    else:
        check_if_int(t)
        print(f"The {tuple_len} numbers are: ", end="")
        for i in range(tuple_len):
            print(t[i], end="")
            if (i < tuple_len - 1):
                print(", ", end="")
            else:
                print("")


print_integer_tuple(kata)
