def ft_reduce(function, iterable):
    """
        Apply function of two arguments cumulatively. Args:
          function_to_apply: a function taking an iterable.
          iterable: an iterable object (list, tuple, iterator).
        Return:
          A value, of same type of elements in the iterable parameter.
          None if the iterable can not be used by the function.
    """
    if not hasattr(function, '__call__'):
        raise TypeError(f"'{type(function).__name__}' object is not callable")
    elif not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    for i, element in enumerate(iterable):
        if i == 0:
            continue
        iterable[i] = function(iterable[i - 1], element)
    return iterable[-1]


if __name__ == "__main__":
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    reduced = ft_reduce(lambda u, v: u + v, lst)
    print(reduced)
