"""unittest"""

import unittest
from product import Product, ProductDiscountError
from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
            Este metodo de clase se ejecuta ejecuta antes de todas las pruebas.
        """
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        """
            Este metodo de clase se ejecuta despues de todas las pruebas.
        """
        pass

    def setUp(self) -> None:
        """
            Se ejecuta antes de cada prueba. por ejemplo crear un objeto antes de la prueba.
        """
        self.name = "Iphone"
        self.price = 500.00
        self.smartphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

    def tearDown(self) -> None:
        """
            Se ejecuta despues de cada prueba. por ejemplo restablecer el objeto despues de la prueba.
        """
        pass

    def test_product_object(self):
        name = "Apple"
        price = 1.70
        product = Product(name, price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price)

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)

    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty())

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_product())

    def test_shopping_in_cart_cart(self):
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name="Example", price=10.0, discount=11.0)


if __name__ == "__main__":
    unittest.main()
