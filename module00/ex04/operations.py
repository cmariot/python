import sys


def str_to_integer(string: str):
    """
    Takes a string and returns an integer if it's a valid integer
    """
    return int(string)


def operations(a: str, b: str) -> None:
    """
    Print the result of the four elementary mathematical operations
    """
    a: int = int(a)
    b: int = int(b)
    print(f"Sum:\t\t{a + b}")
    print(f"Difference:\t{a - b}")
    print(f"Product:\t{a * b}")
    if (b == 0):
        print("Quotient:\tERROR (div by zero)")
        print("Remainder:\tERROR (modulo by zero)")
    else:
        print(f"Quotient:\t{a / b}")
        print(f"Remainder:\t{a % b}")
    return


if (__name__ == "__main__"):
    nb_args: int = len(sys.argv) - 1
    if (nb_args != 2):
        print("Usage: python operations.py <number1> <number2>")
        exit(1)

    try:
        nb1: int = int(sys.argv[1])
        nb2: int = int(sys.argv[2])
    except ValueError:
        print("InputError: operations.py takes only 2 integers as arguments")
        print("Usage: python operations.py <number1> <number2>")
    else:
        operations(nb1, nb2)
