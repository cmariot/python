def ft_filter(function, iterable):
    for element in iterable:
        if function(element) is True:
            yield element
    return None


if __name__ == "__main__":

    x = [1, 2, 3, 4, 5]

    output = ft_filter(lambda dum: not (dum % 2), x)
    print(output)

    output = list(ft_filter(lambda dum: not (dum % 2), x))
    print(output)
