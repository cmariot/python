class Vector:

    def __init__(self,
                 values: 'list[float]'
                 or 'list[list[float]]'
                 or int
                 or 'tuple[int, int]'):
        self.values = values
        self.shape = self._get_shape(values)

    def _get_shape(self, values: list) -> tuple:
        """Get the shape of the vector"""

        # Check if values is a list
        if isinstance(values, list):

            # Check if the list is empty
            if not values:
                return (0, 1)

            # Check if values is a list of floats
            elif (len(values) == 1
                  and isinstance(values[0], list)
                  and all(isinstance(value, float) for value in values[0])):
                return (1, len(values[0]))

            # Check if values is a list of lists of single float
            elif (all(isinstance(value, list) for value in values)
                  and all(len(value) == 1 for value in values)
                  and all(isinstance(value[0], float) for value in values)):
                return (len(values), 1)

        # Check if values is a size
        elif isinstance(values, int):
            self.values = [[float(value)] for value in range(values)]
            return (values, 1)

        # Check if values is a range
        elif (isinstance(values, tuple)
              and len(values) == 2
              and isinstance(values[0], int)
              and isinstance(values[1], int)
              and values[0] < values[1]):
            self.values = [[float(value)]
                           for value in range(values[0], values[1])]
            return (len(range(values[0], values[1])), 1)

        raise TypeError("Vector can only be initialized with :\n"
                        + "- a list of a list of floats\n"
                        + "- a list of lists of single float\n"
                        + "- a size: Vector(3) -> [[0.0], [1.0], [2.0]]\n"
                        + "- a range: Vector((3, 6)) -> [[3.0], [4.0], [5.0]]")

    def dot(self, other: 'Vector') -> float:
        """Dot product of two vectors"""
        if self.shape != other.shape:
            raise ValueError("Cannot dot vectors of different shapes")
        return sum([self.values[i][0] * other.values[i][0]
                    for i in range(self.shape[0])])

    def T(self) -> 'Vector':
        """Transpose the vector"""
        return Vector([[self.values[j][i]
                        for j in range(self.shape[0])
                        for i in range(self.shape[1])
                        ]])

    # must be identical, i.e we expect that print(vector) and vector within
    # python interpretor behave the same
    # __str__
    # __repr__

    def __str__(self) -> str:
        """Return the vector as a string"""
        return f"Vector({self.values})"

    def __repr__(self) -> str:
        """Return the vector as a string"""
        return f"Vector({self.values})"

    # add & radd : only vectors of same shape.
    # __add__
    # __radd__

    def __add__(self, other: 'Vector') -> 'Vector':
        """Add two vectors"""
        if self.shape != other.shape:
            raise ValueError("Cannot add vectors of different shapes")
        return Vector([[self.values[i][j] + other.values[i][j]
                        for j in range(self.shape[1])]
                       for i in range(self.shape[0])])

    def __radd__(self, other: 'Vector') -> 'Vector':
        """Add two vectors"""
        return self.__add__(other)

    # sub & rsub: only vectors of same shape.
    # __sub__
    # __rsub__

    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtract two vectors"""
        if self.shape != other.shape:
            raise ValueError("Cannot subtract vectors of different shapes")
        return Vector([[self.values[i][j] - other.values[i][j]
                        for j in range(self.shape[1])]
                       for i in range(self.shape[0])])

    def __rsub__(self, other: 'Vector') -> 'Vector':
        """Subtract two vectors"""
        return self.__sub__(other)

    # truediv : only with scalars (to perform division of Vector by a scalar).
    # __truediv__
    def __truediv__(self, other: float) -> 'Vector':
        """Divide a vector by a scalar"""
        if not isinstance(other, (float, int)):
            raise TypeError("Can only divide a vector by a scalar")
        elif float(other) == 0.0:
            raise ZeroDivisionError("ZeroDivisionError: division by zero.")
        return Vector([[self.values[i][j] / other
                        for j in range(self.shape[1])]
                       for i in range(self.shape[0])])

    # rtruediv : raises an NotImplementedError with the message
    # "Division of a scalar by a Vector is not defined here."
    # __rtruediv__
    def __rtruediv__(self, other: float) -> 'Vector':
        """Divide a vector by a scalar"""
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here.")

    # mul & rmul: only scalars
    # (to perform multiplication of Vector by a scalar).
    # __mul__
    # __rmul__
    def __mul__(self, other: float) -> 'Vector':
        """Multiply a vector by a scalar"""
        if not isinstance(other, (float, int)):
            raise TypeError("Can only multiply a vector by a scalar")
        ret = []
        if self.shape == (1, 1):
            return Vector([[self.values[0][0] * other]])
        elif self.shape[0] == 1:
            for i in range(self.shape[1]):
                ret.append(self.values[0][i] * other)
            return Vector([ret])
        elif self.shape[1] == 1:
            for i in range(self.shape[0]):
                ret.append([self.values[i][0] * other])
            return Vector(ret)

    def __rmul__(self, other: float) -> 'Vector':
        """Multiply a vector by a scalar"""
        return self.__mul__(other)
