import numpy as np


class NumPyCreator:
    """
    NumPyCreator class
    Creates NumPy arrays from various inputs.
    """

    def from_list(self,
                  lst: 'list' = [],
                  dtype=object) -> 'np.array':
        """
        takes in a list and returns its corresponding NumPy array.
        a list of numbers will create a 1D array,
        a list of list will create a 2D array,
        Args:
            lst: list
        Returns:
            NumPy array
        """
        return np.array(lst, dtype=dtype)

    def from_tuple(self,
                   tpl: 'tuple' = (),
                   dtype=None) -> 'np.array':
        """
        takes in a tuple and returns its corresponding NumPy array.
        Args:
            tpl: tuple
        Returns:
            NumPy array
        """
        return np.array(tpl, dtype=dtype)

    def from_iterable(self,
                      itr: 'np.iterable' = [],
                      dtype=None) -> 'np.array':
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
                   dtype=None) -> 'np.array':
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
                 dtype=float) -> 'np.array':
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

    print("FROM LIST")
    print("\n0 x 0 array :\n",
          npc.from_list())
    print("\n1 x 0 array :\n",
          npc.from_list([]))
    print("\n1 x 1 array :\n",
          npc.from_list([[42]]))
    print("\n1 x 6 array :\n",
          npc.from_list([[1, 2, 3, 6, 3, 4]]))
    print("\n2 x 3 array :\n",
          npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print("\n3 x 3 array :\n",
          npc.from_list([[1, 2, 3], [6, 3, 4], [1, 2, 3]]))
    print("\nLines of different lengths:\n",
          npc.from_list([[1, 2, 3], [6, 4]]))

    print("\nFROM TUPLE")
    print("\n0 x 0 array :\n",
          npc.from_tuple())
    print("\n1 x 0 array :\n",
          npc.from_tuple(()))
    print("\n1 x 1 array :\n",
          npc.from_tuple((42,)))
    print("\n1 x 6 array :\n",
          npc.from_tuple((1, 2, 3, 6, 3, 4)))
    print("\n2 x 3 array :\n",
          npc.from_tuple(((1, 2, 3), (6, 3, 4))))
    print("\n3 x 3 array :\n",
          npc.from_tuple(((1, 2, 3), (6, 3, 4), (2, 5, 3))))

    print("\nFROM ITERABLE")
    print("\n0 x 0 array :\n",
          npc.from_iterable(range(5, 0)))
    print("\n1 x 0 array :\n",
          npc.from_iterable(range(0, 5)))
    print("\n1 x 3 array :\n",
          npc.from_iterable(range(0, 6, 2)))
    print("\nfrom str",
          npc.from_iterable("test"))
    print("",
          npc.from_iterable((1, 2, 3, 6, 3, 4)))
    print("",
          npc.from_iterable([[1, 2, 3], [6, 3, 4]]))
    print("",
          npc.from_iterable(((1, 2, 3), (6, 3, 4))))

    print("\nFROM SHAPE")
    print("\n0 x 0 array :\n", npc.from_shape((0, 0)))
    print("\n1 x 0 array :\n", npc.from_shape((1, 0)))
    print("\n0 x 1 array :\n", npc.from_shape((0, 1)))
    print("\n1 x 1 array :\n", npc.from_shape((1, 1)))
    print("\n1 x 6 array :\n", npc.from_shape((1, 6)))
    print("\n2 x 3 array :\n", npc.from_shape((2, 3)))

    print("\nRANDOM")
    print("\n0 x 0 random array :\n", npc.random((0, 0)))
    print("\n1 x 0 random array :\n", npc.random((1, 0)))
    print("\n0 x 1 random array :\n", npc.random((0, 1)))
    print("\n1 x 1 random array :\n", npc.random((1, 1)))
    print("\n1 x 6 random array :\n", npc.random((1, 6)))
    print("\n2 x 3 random array :\n", npc.random((2, 3)))

    print("\nIDENTITY")
    print("\n0 identity array :\n", npc.identity(0))
    print("\n1 identity array :\n", npc.identity(1))
    print("\n2 identity array :\n", npc.identity(2))
    print("\n3 identity array :\n", npc.identity(3))
    print("\n4 identity array :\n", npc.identity(4))
