from vector import Vector

if __name__ == "__main__":

    try:
        v0 = Vector([])
        print(v0)

        v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        print(v1)

        v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
        print(v2)

        v3 = Vector(10)
        print(v3)

        v4 = Vector((5, 10))
        print(v4)

        v5 = Vector([[2.0]])
        print(v5)

        v6 = Vector([[5.0], ])
        print(v6)

    except Exception as e:
        print(e)

    print("ici:", v1 + v1)
    print(v2.__add__(v2))
    print(v3.__add__(v3))
    print(v5.__add__(v6))
