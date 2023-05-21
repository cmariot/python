from time import sleep
from my_minipack.progress import ft_progress
from my_minipack.logger import log


@log
def main():
    list = range(500)
    for elem in ft_progress(list):
        sleep(0.01)
    print()


if __name__ == "__main__":
    main()
