def ft_map(function, iterable):

    """
    Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """

    if not hasattr(function, '__call__'):
        raise TypeError(f"'{type(function).__name__}' object is not callable")
    elif not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    for element in iterable:
        yield function(element)


if __name__ == "__main__":

    # iterator = ft_map(lambda dum: dum + 1, x)
    # print(iterator)
    # print(list(iterator))

    # try:
    #     ite = ft_map(lambda dum: dum + 'a', 42)
    #     print(list(ite))
    # except TypeError as e:
    #     print(e)

    def no_arg():
        return 0

    def plus_one(x):
        return x + 1

    # function = None
    # function = "not_callable"
    # function = no_arg
    function = plus_one

    # iterable = 0
    # iterable = "string"
    # iterable = 'a'
    # iterable = []
    iterable = [1, 2, 3, 4]

    try:
        ite = ft_map(function, iterable)
        lst = list(ite)
        print("My map   :", lst)
    except Exception as error:
        print("My map exception   :", error)

    try:
        ite = map(function, iterable)
        lst = list(ite)
        print("Real map :", lst)
    except Exception as error:
        print("Real map exception :", error)
