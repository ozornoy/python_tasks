from interfaces import IOrders, IBasket
from order import Order


class Orders(IOrders):
    def __init__(self):
        self.list = []

    def create_order(self, basket: IBasket):
        if len(basket.products) == 0:
            print("Корзина пуста. Для оформления заказа добавь товар в корзину")
        else:
            order = Order(basket.products)
            self.list.append(order)
            basket.products = []
            return order

    def pay_for_order(self, order):
        found_order = next(
            (customer_order for customer_order in self.list if order == customer_order), None
        )
        if not found_order:
            print(f"Заказ с id:{order.id} не найден")
        else:
            found_order.paid_status = True
