class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchaseHistory = []

    def addPurchase(self, item):
        self.purchaseHistory.append(item)

    def printPurchaseHistory(self):
        print(f"Клиент: {self.name}, История покупок: {self.purchaseHistory}")


customer = Customer("Mega Customer", "test@test.test")
customer.addPurchase("tv")
customer.addPurchase("phone")
customer.printPurchaseHistory()
