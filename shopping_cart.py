"""Docstring"""
from product import Product


class ShoppingCart:
    """
        Class ShoppingCart
    """

    def __init__(self) -> None:
        # self.__products = list()
        # Utilizar anotaciones.
        self.__products: list[Product] = []

    @property
    def products(self) -> list:
        """
        Devuelve los productos.
        Returns:
             object
        """
        return self.__products.copy()

    def add_product(self, product: Product) -> None:
        """
        Add product.

        Args:
            product: (obj)
        """
        assert type(product) == Product
        self.__products.append(product)

    def empty(self) -> bool:
        """
        Verfica si el objeto esta vacio.
        Returns:
            bool
        """
        return len(self.__products) == 0

    def has_product(self) -> bool:
        """
        Verfica que tenga un objeto.
        Returns:
            bool
        """
        return not self.empty()

    def remove_product(self, product) -> None:
        """
        Remove product of cart.
        Args:
            product: (int)

        Returns:
            None
        """
        self.__products.remove(product)
