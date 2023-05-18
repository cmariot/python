def ft_map(function, iterable):
    if not hasattr(function, '__call__'):
        raise TypeError(f"'{type(function).__name__}' object is not callable")
    elif not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    for element in iterable:
        yield function(element)


if __name__ == "__main__":

    x = [1, 2, 3, 4, 5]

    iterator = ft_map(lambda dum: dum + 1, x)

    print(iterator)
    print(list(iterator))

    try:
        ite = ft_map(lambda dum: dum + 'a', 42)
        print(list(ite))
    except TypeError as e:
        print(e)
