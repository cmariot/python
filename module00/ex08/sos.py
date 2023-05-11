import sys

MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}


def encrypt(message: str) -> str:
    morse = ''
    for letter in message:
        if letter.isspace():
            morse += "/ "
        elif letter.isalnum():
            morse += (MORSE_CODE_DICT[letter] + ' ')
        else:
            print("ERROR")
            exit(1)
    return morse


if __name__ == "__main__":
    i = 1
    while i < len(sys.argv):
        if (i < len(sys.argv) - 1):
            print(encrypt(sys.argv[i].upper()), end="/ ")
        else:
            print(encrypt(sys.argv[i].upper()))
        i += 1
