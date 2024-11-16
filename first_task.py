"""
Проверка делимости на 5 и 7
Напишите функцию, которая принимает целое число и возвращает true,
если оно делится на 5 и на 7 одновременно, и false в противном случае.
"""


def is_divisible_by_5_and_7(number: int):
    return number % 5 == 0 and number % 7 == 0


"""
Определение принадлежности числа интервалу
Создайте функцию, которая принимает число и проверяет, входит ли оно в интервал от 10 до 20 включительно. 
Если число попадает в интервал, верните true, иначе — false.
"""

def included_in_range_from_10_to_20(number: int) -> bool:
    return 10 <= number <= 20


"""
Проверка на квадрат числа
Напишите функцию, которая принимает два числа и возвращает true, 
если одно из чисел является квадратом другого, и false в противном случае.
"""

def first_number_is_square_of_second(first_number: int, second_number: int) -> bool:
    return first_number == second_number ** 2 or second_number == first_number ** 2


"""
Проверка последней цифры
Создайте функцию, которая принимает число и проверяет, заканчивается ли оно на 5. Верните true, если заканчивается, и false, если нет.
"""

def if_number_ends_with_five(number):
    return str(number)[-1] == "5"


"""
Проверка, является ли сумма цифр четной
Реализуйте функцию, которая принимает число, суммирует его цифры и возвращает true, если сумма четная, и false, если нечетная.
"""

def is_event_amount(number):
    return sum(int(digit) for digit in str(number)) % 2 == 0

"""
Сравнение двух чисел по модулю
Напишите функцию, которая принимает два числа и возвращает true, если модули чисел равны, и false в противном случае.
"""

def compare_by_absolute_value(a, b):
    return abs(a) == abs(b)

"""
Проверка знака числа
Создайте функцию, которая принимает число и возвращает "Positive", если оно положительное,
"Negative", если оно отрицательное, и "Zero", если оно равно нулю.
"""

def is_positive(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

"""
Проверка делимости на 2 или 3
Напишите функцию, которая принимает число и возвращает true, если оно делится на 2 или на 3, и false в противном случае.
"""

def is_divisible_by_two_or_three(number):
    return number % 2 == 0 or number % 3 == 0

"""
Четность суммы двух чисел
Создайте функцию, которая принимает два числа и возвращает "Even", если сумма чисел четная, и
"Odd", если нечетная.
"""

def compare_parity_of_two_numbers(a, b):
    return "Even" if (a + b) % 2 == 0 else "Odd"

"""
Определение числа, кратного и 4, и 6
Создайте функцию, которая проверяет, делится ли число на 4 и на 6 одновременно. Верните true, если да, и false, если нет.
"""

def is_divisible_by_4_and_6(number):
    return number % 4 == 0 and number % 6 == 0

"""
Проверка суммы на четность и кратность 10
Реализуйте функцию, которая принимает два числа и возвращает "Even and Divisible by 10", 
если их сумма четная и делится на 10, "Even but not Divisible by 10", 
если сумма четная, но не делится на 10, и "Odd", если сумма нечетная.
"""

def is_sum_even_and_multiple_of_10(a, b):
    summ = a + b
    return "Even and Divisible by 10" \
        if summ % 2 == 0 and summ % 10 == 0 \
        else "Even but not Divisible by 10" if summ % 2 == 0 and summ % 10 != 0 \
        else "Odd"


"""
Максимум трех чисел
Напишите функцию, которая принимает три числа и возвращает наибольшее из них.
"""

def max_of_three(a, b, c):
    # return max(a, b, c)
    return a if b < a > c else b if a < b > c else c

"""
Проверка на палиндромность числа
Создайте функцию, которая принимает целое число и проверяет, является ли оно палиндромом (например, 121 или 12321). Верните true, если да, и false, если нет.
"""

def is_palindrome(number):
    return str(number) == str(number)[::-1]

"""
Кратность чисел и их сумма
Реализуйте функцию, которая принимает два числа. Если оба числа кратны 3, верните их сумму; если одно из них кратно 3, верните удвоенное значение второго числа; если ни одно не кратно 3, верните
null.
"""

def check_multiples_and_sum(a, b):
    if a % 3 == 0 and b % 3 == 0:
        return a + b
    elif a % 3 == 0 and b % 3 != 0:
        return b * 2
    elif a % 3 != 0 and b % 3 == 0:
        return a * 2
    elif a % 3 != 0 and b % 3 != 0:
        return None



"""
Проверка возраста на категорию
Напишите функцию, которая принимает возраст и возвращает категорию: Child (до 12 лет), Teenager (от 13 до 17 лет), Adult (от 18 до 64 лет) или Senior (от 65 лет и старше).
"""

def check_age_category(age):
    if age == 12:
        return "Child"
    elif 13 <= age <= 17:
        return "Teenager"
    elif 18 <= age <= 64:
        return "Adult"
    elif age >= 65:
        return "Senior"


"""
Проверка на делимость с остальным значением
Создайте функцию, которая принимает два числа и проверяет, делится ли первое число на второе с остатком равным 2. Верните true, если делится с остатком 2, и false - если нет.
"""

def check_divisibility_with_remainder(a, b):
    return a % b == 2
