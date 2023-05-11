import time


def ft_progress(iterable,
                length=50,
                fill='█',
                empty='░',
                print_end='\r'):
    """
    Progress bar generator
    This function displays a progress bar for an iterable object
    and yields its items.

    Parameters:
    - iterable (list): An iterable object.
    - length (int, optional): The length of the progress bar. Default is 50.
    - fill (str, optional): The character used to fill the progress bar.
    - print_end (str, optional): The character used to separate printed output.

    Returns:
    - generator: A generator that yields the items of the iterable object.

    Example usage:
    ```
        for i in ft_progress(range(100)):
            time.sleep(0.1)
    ```
    """

    start = time.time()
    total = 0
    for _ in iterable:
        total += 1
    filled_length = 0
    fmt_percent = '{0:3.0f}%'
    fmt_eta = '{0:5.2f}s'
    fmt_et = '{0:.2f}s'
    i = 0
    while (i < total):
        percent = (i + 1) / total * 100
        filled_length = int(length * (i + 1) // total)
        elapsed_time = time.time() - start
        eta = elapsed_time * (total / (i + 1) - 1)
        bar = "[ETA:" + fmt_eta.format(eta) + "]"\
            + " [" + fmt_percent.format(percent) + '] '\
            + fill * filled_length\
            + empty * (length - filled_length) + ' '\
            + str(i + 1) + "/" + str(total) \
            + " | elapsed time " + fmt_et.format(elapsed_time)
        print(bar, end=print_end)
        i += 1
        yield i


if __name__ == "__main__":
    listy = (range(1000))
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
