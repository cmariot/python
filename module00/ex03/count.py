import sys
import string


def text_analyzer(to_analyze: str = None):
    """
    Analyzes a text to_analyze and prints information about its composition.

    Parameters:
    to_analyze (str): The text to be analyzed. If None, the function prompts
    the user to input a text.

    Returns:
    None: The function only prints the analysis results.

    Raises:
    TypeError: If the input text is not a to_analyze.

    The function counts the number of upper and lower case letters,
    punctuation marks, and spaces in the input text.
    It then prints a summary of the results, including the total number of
    characters, the number of upper and lower case letters, the number of
    punctuation marks, and the number of spaces.

    Example usage:
    >>> text_analyzer("Hello, World!")
    The text contains 13 character(s):
    - 2 upper letter(s)
    - 8 lower letter(s)
    - 2 punctuation mark(s)
    - 1 space(s)
    >>> text_analyzer()
    What is the text to analyse ?
    This is a sample text.
    The text contains 20 character(s):
    - 0 upper letter(s)
    - 16 lower letter(s)
    - 1 punctuation mark(s)
    - 3 space(s)
    """

    if to_analyze is None:
        print("What is the text to analyse ?")
        text_analyzer(input())
    elif (type(to_analyze) != str):
        print("The text must be a to_analyze")
    else:
        upper_case = 0
        lower_case = 0
        punctuation = 0
        spaces = 0

        for char in to_analyze:
            if char.isupper():
                upper_case += 1
            elif char.islower():
                lower_case += 1
            elif char.isspace():
                spaces += 1
            elif char in string.punctuation:
                punctuation += 1

        print(f"The text contains {len(to_analyze)} character(s):")
        print(f"- {upper_case} upper letter(s)")
        print(f"- {lower_case} lower letter(s)")
        print(f"- {punctuation} punctuation mark(s)")
        print(f"- {spaces} space(s)")
    return


if __name__ == "__main__":
    number_arguments: int = len(sys.argv) - 1
    if (number_arguments == 0):
        text_analyzer()
    elif (number_arguments == 1):
        text_analyzer(sys.argv[1])
    else:
        print("Error: too many arguments.")
