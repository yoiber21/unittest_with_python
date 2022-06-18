"""Docstring"""


class ProductDiscountError(Exception):
    """ Clase con captura de error propio. """
    pass


class Product:
    """
        Product class.
    """

    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price
        self.discount = discount

        if discount > price:
            raise ProductDiscountError("Error en el precio.")
