# 1 Написать типы для всех задач из прошлого дз

from typing import TYPE_CHECKING

def exchange_currency(byn: float) -> float:
    return byn * 2.58


def sum(a: int, b: int) -> int:
    return a + b


def sum_1(x: int) -> int :
    return x * random.randrange(1, 25)


def leap_year(year: int) -> int:
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def maximum(data_list: list) -> int:
    return max(data_list)


data_list = [2, 5, 6, 33, 78, 4, 45, -3]
print(maximum(data_list))


def minimum(data_l: list):
    return min(data_l)


data_l = [2, 5, 6, 33, 78, 4, 45, -3]
print(minimum(data_l))


def season(month_num: int) -> None:
    if 6 > month_num > 2:
        return print("Spring")
    elif 9 > month_num > 5:
        return print("Summer")
    elif 12 > month_num > 8:
        return print("Autumn")
    else:
        return print("Winter")


def just_int_float(a: list) -> list:
    b = list(filter(lambda x: isinstance(x, int), a))
    c = list(filter(lambda x: isinstance(x, float), a))
    d = list(filter(lambda x: isinstance(x, bool), a))
    result = list(set(b) - set(d)) + c
    z = sorted(result)
    print(z)


list_a = [16, -17, 2, 78.7, False, False, {"True": "True"}, 555, 12, 23, 42, 'DD']
just_int_float(list_a)


# 2 Написать функцию типа [i: int, n: int, a: str] -> any

def example(x: int, n: int, a: str) -> any:
    a = '8'
    n = str(n + 1)
    return str(x) + n + a


s = ""
print(list(example(1, 3, s)))


# 3 Написать функцию по типу x: str -> int

def hello(x: str) -> int:
    return int(x, 0)


z = "0b1010"
print((hello(z)))
print(type(hello(z)))


# 4 Написать функцию для суммы чисел, для нее написать декоратор, который возводит в степень результаты
# и выводит на экран в виде (степень суммы чисел x,y = )

def squard(result_sum):
    def wrapper(x, y):
        zz = round(result_sum(x, y) ** 2, 2)
        print("степень суммы чисел: x= ", x, "y = ", y, " равно ", zz)
    return wrapper


@squard
def sum(first: float, second: float):
    return round(first + second, 2)


sum(2.33, 5.4)
sum(2.5, 5.4444)


# 6 Для перебора массива использовать yield, достать 5 элемент массива через next()

def generator_numbers(n: int):
    for number in range(n):
        yield number


my_list = generator_numbers(100000)
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))