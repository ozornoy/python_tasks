class Employee:
    def __init__(self, name, position, salary):
        self._name = name
        self._position = position
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def printEmployeeInfo(self):
        print(f"Сотрудник: {self.name}, Должность: {self.position}, Зарплата: {self.salary}")

    def increaseSalary(self, percentage):
        self.salary = self.salary + (self.salary / 100 * percentage)


cto = Employee("First employee", "CTO", 260)
manager = Employee("First employee", "Manager", 1240)
cto.increaseSalary(25)
manager.increaseSalary(100)
cto.printEmployeeInfo()
manager.printEmployeeInfo()
