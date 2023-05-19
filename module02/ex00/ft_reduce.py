from functools import reduce
import copy


def ft_reduce(function, iterable):
    """
        Apply function of two arguments cumulatively.
        Args:
          function_to_apply: a function taking an iterable.
          iterable: an iterable object (list, tuple, iterator).
        Return:
          A value, of same type of elements in the iterable parameter.
          None if the iterable can not be used by the function.
    """
    if not hasattr(function, '__call__'):
        raise TypeError(f"'{type(function).__name__}' object is not callable")
    elif not iterable:
        raise Exception("ft_reduce() of empty sequence with no initial value")
    elif not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    # Elif object does not support item assignment :

    iter_copy = copy.deepcopy(iterable)
    for i, element in enumerate(iter_copy):
        if i == 0:
            continue
        iter_copy[i] = function(iter_copy[i - 1], element)
    return iter_copy[-1]


def plus(u, v):
    return u + v


if __name__ == "__main__":

    # function = None
    # function = "not_callable"
    # function = no_arg
    function = plus

    # iterable = 0
    iterable = "string"
    # iterable = 'a'
    # iterable = []
    # iterable = [True, False, True, False]
    # iterable = [1, 2, 3, 4, 5, 6, 7, 8]
    # iterable = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

    try:
        ite = ft_reduce(function, iterable)
        print("My reduce   :", ite)
    except Exception as error:
        print("My reduce exception   :", error)

    try:
        ite = reduce(function, iterable)
        print("Real reduce :", ite)
    except Exception as error:
        print("Real reduce exception :", error)
