class Person:
    def __init__(self, name="", age=0, gender=""):
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")


unknown_person = Person()
first_person = Person("First person", 30)
second_person = Person("Second person", 30, "male")

unknown_person.print_info()
first_person.print_info()
second_person.print_info()
