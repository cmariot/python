kata = (0, 4, 132.42222, 10000, 12345.67)


def print_tuple(t: tuple):
    """
    Print the tuple
    """
    tuple_len = len(t)
    if (tuple_len == 0):
        print("The tuple is empty")
        exit(1)
    elif (tuple_len != 5):
        print("ERROR, the tuple must contain 5 values")
        exit(1)
    elif (not isinstance(t[0], int) or t[0] < 0 or t[0] > 99 or
          not isinstance(t[1], int) or t[1] < 0 or t[1] > 99 or
          not isinstance(t[2], float) or
          not isinstance(t[3], int) or
          not isinstance(t[4], float)):
        print("ERROR, the tuple must contain only integers and floats")
        print("Usage: (module, ex, t, n, f)")
        exit(1)

    print(f"module_{t[0]:02d}, ex_{t[1]:02d} : ", end="")
    print(f"{t[2]:.2f}, {t[3]:.2e}, {t[4]:.2e}")


print_tuple(kata)
