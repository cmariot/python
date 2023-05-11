import sys


def usage():
    print("whois.py takes an integer as argument")
    print("and prints whether it's a odd, even or zero.")
    print("example : python3 whois.py 42")


def too_many_args():
    print("whois.py takes only one argument")


def str_to_integer(string: str):
    """
    Takes a string and returns an integer if it's a valid integer
    """
    try:
        return int(string)
    except ValueError:
        print("whois.py takes only an integer as argument")
        exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    elif len(sys.argv) > 2:
        too_many_args()
    else:
        int: int = str_to_integer(sys.argv[1])
        if int == 0:
            print("I'm Zero.")
        elif int % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
