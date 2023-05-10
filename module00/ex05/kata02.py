kata = (2023, 5, 10, 15, 18)


def int_len(n: int):
    """
    Return the number of digits of the integer
    """
    str_n = str(n)
    return len(str_n)


def invalid_date(t: tuple):
    """
    Check if the tuple contains only integers
    """
    for i in range(len(t)):
        if (not isinstance(t[i], int)):
            print("ERROR, the tuple contains non-integer value(s)")
            return True
    if (t[0] < 0
        or t[1] < 1 or t[1] > 12
        or t[2] < 1 or t[2] > 31
        or t[3] < 0 or t[3] > 23
            or t[4] < 0 or t[4] > 59):
        print("ERROR, the tuple contains invalid value(s)")
        return True
    elif (int_len(t[0]) > 4 or
          int_len(t[1]) > 2 or
          int_len(t[2]) > 2 or
          int_len(t[3]) > 2 or
          int_len(t[4]) > 2):
        print("ERROR, the tuple contains invalid value(s) 2")
        return True
    return False


def print_date(t: tuple):
    """
    Print the date
    """
    if (len(t) != 5):
        print("ERROR, the tuple must contain 5 values")
        exit(1)
    elif (invalid_date(t)):
        print("ERROR, the tuple must contain only integers")
        print("Usage: (year, month, day, hour, minute)")
        exit(1)
    print(f"{t[1]:02d}/{t[2]:02d}/{t[0]:04d} {t[3]:02d}:{t[4]:02d}")


print_date(kata)
