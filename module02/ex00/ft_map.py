def ft_map(function, iterable):
    for element in iterable:
        yield function(element)
    return None


if __name__ == "__main__":

    x = [1, 2, 3, 4, 5]

    output = ft_map(lambda dum: dum + 1, x)
    print(output)

    output = list(ft_map(lambda t: t + 1, x))
    print(output)
