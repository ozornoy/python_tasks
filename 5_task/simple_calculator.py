from typing import Union, Callable

Number = Union[int, float]
Operation = Callable[[Number, Number], Number]


class Calculator:
    def __init__(self):
        self.__result = 0.0

    @staticmethod
    def __validate_number(number: Number) -> None:
        if not isinstance(number, (int, float)):
            raise ValueError("The input must be integer or float.")

    def apply_operation(self, operation: Operation, number: Number) -> 'Calculator':
        self.__validate_number(number)
        self.__result = operation(self.__result, number)
        return self

    def equals(self) -> Number:
        return self.__result

    def reset(self) -> None:
        self.__result = 0


def add(x: Number, y: Number) -> Number:
    return x + y


def subtract(x: Number, y: Number) -> Number:
    return x - y


def multiply(x: Number, y: Number) -> Number:
    return x * y


def divide(x: Number, y: Number) -> Number:
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y


calculator = Calculator()
print(calculator.apply_operation(add, 2).equals())
