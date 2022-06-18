""" Docstring """


class User:
    """ Permite representar a un usuario. """

    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo user.

        Args:
            username (str): Username of User.
            password (str): password of user.

        Tests:
            >>> palindrome("anita lava la tina")
            True
            >>> palindrome("codigofacilito")
            False
            >>> sentence_test = 'Oso'
            >>> palindrome(sentence_test)
            True
        """
        self.username = username
        self.password = password


def palindrome(sentence: str) -> bool:
    """ Permite conocer si un string es, o no, un palindrome.
        python3 -m doctest unittest_python.py
        python3 -m doctest unittest_python.py -v: More info
    Args:
        sentence: (str) string a evaluar.
    Returns:
        bool: True or False.

    """
    sentence = sentence.lower().replace(' ', '')

    return sentence == sentence[::-1]
