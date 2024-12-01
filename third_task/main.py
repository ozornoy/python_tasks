from third_task.customer import Customer
from third_task.order import Order
from third_task.product import Iphone, ComputerMouse

products_dict = {
    "iphone_15_pro": Iphone(name="iPhone 15 Pro", color="Silver", price=1199, storage=256),
    "iphone_14": Iphone(name="iPhone 14", color="Blue", price=899, storage=128),
    "logitech_mx_master_3s": ComputerMouse(name="Logitech MX Master 3S", color="Gray", price=99, dpi=8000),
    "razer_deathadder_v3": ComputerMouse(name="Razer DeathAdder V3", color="Black", price=69, dpi=26000),
    "steelseries_rival_5": ComputerMouse(name="SteelSeries Rival 5", color="White", price=59, dpi=18000),
}

customer1 = Customer("Федоров Федор Федорович", "test@test.test", "+79999999999")

customer1.remove_from_basket(products_dict["steelseries_rival_5"])
# Товар не был найден в корзине

customer1.create_order()
# "Корзина пуста. Для оформления заказа добавь товар в корзину"

customer1.add_to_basket(products_dict["iphone_15_pro"], products_dict["logitech_mx_master_3s"])
print(len(customer1.basket.products))
# 2

customer1.remove_from_basket(products_dict["iphone_15_pro"])
print(len(customer1.basket.products))
print(customer1.basket.products[0].name)
# 1
# "Logitech MX Master 3S"


fake_order = Order(list(products_dict))
customer1.pay_for_order(fake_order)
# "Заказ с id:{order.id} не найден"

customer1_order = customer1.create_order()
print(len(customer1.basket.products))
print(customer1_order.paid_status)
customer1.pay_for_order(customer1_order)
print(len(customer1.basket.products))
print(customer1_order.paid_status)
# 1
# False
# 0
# True
