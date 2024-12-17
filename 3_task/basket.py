import uuid
from typing import List

from interfaces import IBasket
from product import IProduct


class Basket(IBasket):
    def __init__(self):
        self.id = uuid.uuid4()
        self.products: List[IProduct] = []

    def add_products(self, *products: IProduct):
        for product in products:
            self.products.append(product)

    def remove_product(self, product: IProduct):
        try:
            self.products.remove(product)
        except ValueError:
            print("Товар не был найден в корзине")

    def clear(self):
        self.products = []
