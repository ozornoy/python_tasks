import uuid


class Order:
    def __init__(self, products: list, paid_status: bool = False):
        self.id = uuid.uuid4()
        self.products = products
        self.paid_status = paid_status
        self.total_price = self.__total_price()

    def __total_price(self):
        return sum(product.price for product in self.products)
