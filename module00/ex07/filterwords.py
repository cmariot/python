import sys
import re


def error():
    print("ERROR")
    exit(1)


def str_to_integer(string: str):
    """
    Takes a string and returns an integer if it's a valid integer
    """
    try:
        return int(string)
    except ValueError:
        error()


def filterwords(S: str, N: str):
    len_to_filter = str_to_integer(N)
    # Remove all punctuation symbols from the S
    str_without_punct: str = re.sub(r'[^\w\s]', '', S)
    # Split the string into a list of words
    str_list: list[str] = str_without_punct.split()
    # Append all words with a length > len_to_filter
    final_list = [word for word in str_list if len(word) > len_to_filter]
    print(final_list)


if __name__ == "__main__":
    nb_args = len(sys.argv) - 1
    if (nb_args != 2):
        error()
    else:
        filterwords(sys.argv[1], sys.argv[2])
