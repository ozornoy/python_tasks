from third_task.basket import Basket
from third_task.order import Order


class Customer:
    def __init__(self, fio: str, email: str, phone: str):
        self.fio = fio
        self.email = email
        self.phone = phone
        self.basket = Basket()
        self.orders = []

    def add_to_basket(self, *products):
        for product in products:
            self.basket.products.append(product)

    def remove_from_basket(self, product):
        try:
            self.basket.products.remove(product)
        except ValueError:
            print("Товар не был найден в корзине")

    def clear_basket(self):
        self.basket.products = []

    def create_order(self):
        order = None
        if len(self.basket.products) == 0:
            print("Корзина пуста. Для оформления заказа добавь товар в корзину")
        else:
            order = Order(self.basket.products)
            self.orders.append(order)
        return order

    def pay_for_order(self, order):
        found_order = next(
            (cusotmer_order for cusotmer_order in self.orders if order == cusotmer_order), None
        )
        if not found_order:
            print(f"Заказ с id:{order.id} не найден")
        else:
            found_order.paid_status = True
            self.basket.products = []
