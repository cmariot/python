import time
import shutil


def ft_progress(iterable,
                length=shutil.get_terminal_size().columns - 2,
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

    total = len(iterable)
    start = time.time()
    for i, item in enumerate(iterable, start=1):
        elapsed_time = time.time() - start
        eta = elapsed_time * (total / i - 1)
        current_percent = (i / total) * 100
        filled_length = int(length * i / total)
        if eta == 0.0:
            eta_str = '[DONE]    '
        elif eta < 60:
            eta_str = f'[ETA {eta:.0f} s]'
        elif eta < 3600:
            eta_str = f'[ETA {eta / 60:.0f} m]'
        else:
            eta_str = f'[ETA {eta / 3600:.0f} h]'
        percent_str = f'[{current_percent:6.2f} %] '
        progress_str = fill * filled_length + empty * (length - filled_length)
        counter_str = f' [{i:>{len(str(total))}}/{total}] '
        if elapsed_time < 60:
            elapsed_time_str = f' [Elapsed-time {elapsed_time:.2f} s]'
        elif elapsed_time < 3600:
            elapsed_time_str = f' [Elapsed-time {elapsed_time / 60:.2f} m]'
        else:
            elapsed_time_str = f' [Elapsed-time {elapsed_time / 3600:.2f} h]'
        bar = ("\033[F\033[K " + progress_str + "\n"
               + elapsed_time_str
               + counter_str
               + percent_str
               + eta_str)
        print(bar, end=print_end)
        yield item


if __name__ == '__main__':
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.05)
    print()
