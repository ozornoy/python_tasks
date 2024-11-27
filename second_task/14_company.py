class Company:
    def __init__(self, name: str, employees: int, revenue: float):
        self.name = name
        self.employees = employees
        self.revenue = revenue

    def printCompanyInfo(self):
        print(f"Компания: {self.name}, Сотрудников: {self.employees}, Доход: {self.revenue}")


company = Company("Mega Company", 22, 123123.22)
company.printCompanyInfo()
