def ft_reduce(function_to_apply, iterable):
    """
        Apply function of two arguments cumulatively. Args:
          function_to_apply: a function taking an iterable.
          iterable: an iterable object (list, tuple, iterator).
        Return:
          A value, of same type of elements in the iterable parameter.
          None if the iterable can not be used by the function.
    """
    for i, element in enumerate(iterable):
        if i == 0:
            continue
        iterable[i] = function_to_apply(iterable[i - 1], element)
    return iterable[-1]


if __name__ == "__main__":
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

    iter = ft_reduce(lambda u, v: u + v, lst)
    print(iter)
