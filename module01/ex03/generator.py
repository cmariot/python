import random


def shuffle(array: 'list[str]') -> 'list[str]':
    shuffled_array: list[str] = []
    for i in range(len(array)):
        random_index: int = random.randint(0, len(array) - 1)
        shuffled_array.append(array[random_index])
        array.pop(random_index)
    return shuffled_array


def generator(string: str, sep: str = " ", option: str = "none") -> str:
    """
    Splits the text according to sep value and yield the substrings.
    option precise if an action is performed to the substrings before
    it is yielded.
    """
    if (not isinstance(string, str)
        or not isinstance(sep, str)
        or not isinstance(option, str)
            or option not in ["none", "shuffle", "unique", "ordered"]):
        return "ERROR"
    substrings: list[str] = string.split(sep)
    if option == "shuffle":
        substrings = shuffle(substrings)
    elif option == "ordered":
        substrings.sort()
    elif option == "unique":
        substrings = list(dict.fromkeys(substrings))
    for substring in substrings:
        yield substring


if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."

    print("\nOption : none")
    for words in generator(text, sep=" "):
        print(words)

    print("\nOption : shuffle")
    for words in generator(text, sep=" ", option="shuffle"):
        print(words)

    print("\nOption : ordered")
    for words in generator(text, sep=" ", option="ordered"):
        print(words)

    print("\nOption : unique")
    for words in generator(text, sep=" ", option="unique"):
        print(words)

    print("\nError management :")
    for words in generator(text, sep=" ", option="error"):
        print(words)

    print()
