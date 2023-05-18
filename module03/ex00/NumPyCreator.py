import numpy as np


class NumPyCreator:

    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.array(itr)

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.random(shape)


if __name__ == "__main__":

    npc = NumPyCreator()

    print(1, npc.from_list([[1, 2, 3], [6, 3, 4]]))

    print(2, npc.from_list([[1, 2, 3], [6, 4]]))

    print(3, npc.from_tuple(("a", "b", "c")))
    print(4, npc.from_iterable(range(5)))
    shape = (3, 5)
    print(5, npc.from_shape(shape))
    print(6, npc.random(shape))
