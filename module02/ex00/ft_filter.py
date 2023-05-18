def ft_filter(function, iterable):
    if function is not None and not hasattr(function, '__call__'):
        raise TypeError(f"'{type(function).__name__}' object is not callable")
    elif not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    for element in iterable:
        if function is None:
            if element:
                yield element
        elif function(element) is True:
            yield element


def is_more_than_5(x):
    return (x > 5)


if __name__ == "__main__":

    x = [1, 2, 3, 4, 5]

    iterator = ft_filter(lambda dum: not (dum % 2), x)
    list_even = list(ft_filter(lambda dum: not (dum % 2), x))
    print(list_even)

    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    iterator = ft_filter(is_more_than_5, iterable)
    lst_5 = list(iterator)
    print(lst_5)

    iterator = ft_filter(None, iterable)
    lst_none = list(iterator)
    print(lst_none)
