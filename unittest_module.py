"""Docstring"""
import unittest


class TestExampleTest(unittest.TestCase):
    """ Clase para prueba unitaria con unittest, debe heredar de unittest.TestCase """

    def test_sum_integer(self):
        number_1 = 10
        number_2 = 20
        result = number_1 + number_2

        self.assertEqual(result, 30)


if __name__ == '__main__':
    unittest.main()
