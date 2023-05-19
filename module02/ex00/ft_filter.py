def ft_filter(function, iterable):

    """
    Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """

    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable).__name__}'"
                        + " object is not iterable")
    elif function is None:
        for element in iterable:
            if element:
                yield element
    else:
        if not hasattr(function, '__call__'):
            raise TypeError(f"'{type(function).__name__}'"
                            + " object is not callable")
        for element in iterable:
            if function(element) is True:
                yield element


def no_arg():
    return 0


def plus_one(x):
    return x + 1


def is_more_than_5(x):
    return (x > 5)


if __name__ == "__main__":

    # x = [1, 2, 3, 4, 5]

    # iterator = ft_filter(lambda dum: not (dum % 2), x)
    # list_even = list(ft_filter(lambda dum: not (dum % 2), x))
    # print(list_even)

    # iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # iterator = ft_filter(is_more_than_5, iterable)
    # lst_5 = list(iterator)
    # print(lst_5)

    # iterator = ft_filter(None, iterable)
    # lst_none = list(iterator)
    # print(lst_none)

    # function = None
    # function = "not_callable"
    # function = no_arg
    function = is_more_than_5

    # iterable = 0
    # iterable = "string"
    # iterable = 'a'
    # iterable = []
    # iterable = [True, False, True, False]
    iterable = [1, 2, 3, 4, 5, 6, 7, 8]

    try:
        ite = ft_filter(function, iterable)
        lst = list(ite)
        print("My filter   :", lst)
    except Exception as error:
        print("My filter exception   :", error)

    try:
        ite = filter(function, iterable)
        lst = list(ite)
        print("Real filter :", lst)
    except Exception as error:
        print("Real filter exception :", error)
