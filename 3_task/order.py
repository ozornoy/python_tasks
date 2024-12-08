import uuid


class Order:
    def __init__(self, products: list, paid_status: bool = False):
        self.id = uuid.uuid4()
        self.products = products
        self.paid_status = paid_status
