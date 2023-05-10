import sys


def usage():
    print("exec.py takes a string as argument")
    print("python3 exec.py 'Hello World!'")


def merge_strings(strings: list):
    """
    Takes a list of strings and returns a single string,
    with each string separated by a space
    """
    return " ".join(strings)


def swap_letters_case(string: str):
    """
    Takes a string and returns a new string with the case of each
    letter swapped.
    """
    return string.swapcase()


def reverse_string(string: str):
    """
    Takes a string and returns a new string with the letters in reverse order
    """
    return string[::-1]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        merged = merge_strings(sys.argv[1:])
        swapped = swap_letters_case(merged)
        reversed = reverse_string(swapped)
        print(reversed)
