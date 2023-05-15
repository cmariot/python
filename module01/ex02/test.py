from vector import Vector


def plusOne(arg):
    return arg + 1


if __name__ == "__main__":

    # Column vector of shape n * 1
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected output:
    # Vector([[0.0], [5.0], [10.0], [15.0]])

    # Row vector of shape 1 * n
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected output
    # Vector([[0.0, 5.0, 10.0, 15.0]])

    v2 = v1 / 2.0
    print(v2)
    # Expected output
    # Vector([[0.0], [0.5], [1.0], [1.5]])

    try:
        v1 / 0.0
    except Exception as e:
        print(e)
        # Expected ouput
        # ZeroDivisionError: division by zero.

    try:
        2.0 / v1
    except Exception as e:
        print(e)
        # Expected output:
        # NotImplementedError: \
        # Division of a scalar by a Vector is not defined here.

    # Column vector of shape (n, 1)
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    # Expected output
    # (4,1)
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    # Expected output
    # [[0.0], [1.0], [2.0], [3.0]]

    # Row vector of shape (1, n)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    # Expected output
    # (1,4)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    # Expected output
    # [[0.0, 1.0, 2.0, 3.0]]

    print("Example 1:")
    # Example 1:
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)
    # Expected output:
    # (4,1)
    print(v1.T())
    # Expected output:
    # Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v1.T().shape)
    # Expected output:
    # (1,4)

    print("Example 2:")
    # Example 2:
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v2.shape)
    # Expected output:
    # (1,4)
    print(v2.T())
    # Expected output:
    # Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v2.T().shape)
    # Expected output:
    # # (4,1)

    print()
    print("Test forEach :")
    v1 = Vector([[0.0, ]])
    v3 = v1.__forEach__(plusOne)
    print(v3)

    print("V3 + V3 = ", v3 + v3)
