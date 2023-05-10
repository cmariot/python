import sys

if (__name__ == "__main__"):
    if (len(sys.argv) != 3):
        print("ERROR")
    else:
        try:
            nb: int = int(sys.argv[2])
            if (nb < 0):
                print("ERROR")
            else:
                words: list = sys.argv[1].split()
                filtered_words: list
                # = list(
                #  filter(lambda word: len(word) > nb, words))
                print(filtered_words)
        except ValueError:
            print("ERROR")
