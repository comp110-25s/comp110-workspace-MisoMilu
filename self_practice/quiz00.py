"""Some fun functions..."""


def quadruple(x: int) -> int:
    """Quadruple an int!"""
    print("quadruple(" + str(x) + ")")
    return double(x=double(x=x))


def double(x: int) -> int:
    """Double an int!"""
    print("double(" + str(x) + ")")
    return 2 * x


print(quadruple(x=2))
