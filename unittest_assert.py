""" Docstring """


def sum_positive_number(n1: int, n2: int) -> int:
    """
    Args:
        n1: (int)
        n2: (int)

    Returns:
        int: n1 + n2
    """
    try:
        assert n1 > 0 and n2 > 0, "Solo se puede sumar numeros positivos"
        return n1 + n2
    except AssertionError as err:
        print(err)


if __name__ == "__main__":
    sum_positive_number(-10, 9)
    # try:
    #     assert 10 == 11, "Lo siento esta prueba no fue success."
    # except AssertionError as err:
    #     print(err)
