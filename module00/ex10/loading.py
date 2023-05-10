import time


def ft_progress(listy):
    for i in listy:
        yield i


if __name__ == "__main__":
    time_elapsed = 0
    sleep_time = 0.01
    range_size = 300
    remaining_range = range_size
    loading_bar_size = 80

    listy = range(range_size)
    for elem in ft_progress(listy):
        time_elapsed += sleep_time
        remaining_range -= 1
        ETA = float(remaining_range * sleep_time)
        percent = (elem + 1) * 100 / range_size

        number_of_blocks = int(percent * loading_bar_size / 100)
        number_of_spaces = loading_bar_size - number_of_blocks
        sequence1 = "{:■<" + str(number_of_blocks) + "}"
        sequence2 = "{: <" + str(number_of_spaces) + "}"
        progress_bar = sequence1.format("") + sequence2.format("")

        print("ETA: %.2fs" % ETA, end=' ')
        print("[%3d%%]" % percent, end=' ')
        print("%4d/%4d |" % (elem + 1, range_size), end=' ')
        print("[ %s ]" % progress_bar, end=' ')
        print("elapsed_time %.2fs" % time_elapsed, end='\r')

        time.sleep(sleep_time)

    print("")
