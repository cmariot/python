import numpy as np


class NumPyCreator:

    def from_list(self,
                  lst: 'list',
                  dtype=list) -> 'np.array':
        """
        takes in a list and returns its corresponding NumPy array.
        Args:
            lst: list
        Returns:
            NumPy array
        """
        return np.array(lst, dtype=dtype)

    def from_tuple(self,
                   tpl: 'tuple',
                   dtype=tuple) -> 'np.array':
        """
        takes in a tuple and returns its corresponding NumPy array.
        Args:
            tpl: tuple
        Returns:
            NumPy array
        """
        return np.array(tpl, dtype=dtype)

    def from_iterable(self,
                      itr: 'np.iterable',
                      dtype=object) -> 'np.array':
        """
        takes in an iterable and returns an array which contains all
        of its elements.
        Args:
            itr: iterable
        Returns:
            NumPy array
        """
        return np.array(itr, dtype=dtype)

    def from_shape(self,
                   shape: 'tuple[int, int]',
                   value=0,
                   dtype=object) -> 'np.array':
        """
        returns an array filled with the same value.
        Args:
            shape: tuple of int
            value: int
        Returns:
            NumPy array
        """
        return np.full(shape, value, dtype=dtype)

    def random(self,
               shape: 'tuple[int, int]') -> 'np.array':
        """
        returns an array filled with random values.
        Args:
            shape: tuple of int
        Returns:
            NumPy array
        """
        return np.random.random(shape)

    def identity(self,
                 n: int,
                 dtype=object) -> 'np.array':
        """
        returns an array representing the identity matrix of size n.
        Args:
            n: int
        Returns:
            NumPy array
        """
        return np.identity(n, dtype=dtype)


if __name__ == "__main__":

    npc = NumPyCreator()

    shape = (3, 5)

    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print(npc.from_list([[1, 2, 3], [6, 4]]))

    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_tuple(["a", "b", "c"]))

    print(npc.from_iterable(range(5)))

    print(npc.from_shape(shape))

    print(npc.random(shape))

    print(npc.identity(4))
