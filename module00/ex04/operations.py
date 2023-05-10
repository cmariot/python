
import sys


def invalid_args_type(arg1: int, arg2: int) -> bool:
    """
    Check if the arguments are not numbers
    """
    if (arg1.isnumeric() and arg2.isnumeric()):
        return False
    return True


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
    if (nb_args == 0):
        print("Usage: python operations.py <number1> <number2>")
    elif (nb_args != 2 or invalid_args_type(sys.argv[1], sys.argv[2])):
        print("InputError: only numbers\n\nUsage: python operations.py <number1> <number2>")
    else:
        operations(sys.argv[1], sys.argv[2])
