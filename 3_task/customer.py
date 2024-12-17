from basket import Basket
from orders import Orders
from interfaces import IBasket, IOrders


class Customer:
    def __init__(self, fio: str, email: str, phone: str, basket: IBasket = None,
                 orders: IOrders = None):
        self.fio = fio
        self.email = email
        self.phone = phone
        self.basket = basket or Basket()
        self.orders = orders or Orders()

    def add_products_to_basket(self, *products):
        self.basket.add_products(*products)

    def remove_product_from_basket(self, product):
        self.basket.remove_product(product)

    def clear_basket(self):
        self.basket.clear()

    def create_order(self):
        return self.orders.create_order(self.basket)

    def pay_for_order(self, order):
        self.orders.pay_for_order(order)
