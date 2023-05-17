def ft_filter(function, iterable):
    for element in iterable:
        if function is None:
            if element:
                yield element
        elif function(element) is True:
            yield element


def is_even(x):
    return not (x % 2)


if __name__ == "__main__":

    x = [1, 2, 3, 4, 5]

    output = ft_filter(lambda dum: not (dum % 2), x)
    print(output)

    output = list(ft_filter(lambda dum: not (dum % 2), x))
    print(output)

    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    iterator = ft_filter(None, iterable)
    lst_even = list(iterator)
    print(lst_even)
