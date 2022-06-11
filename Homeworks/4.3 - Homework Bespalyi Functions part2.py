#1 Создадим функцию с простыми командами Обернём её в декоратор, который бы дополнял возможности функции.

def bonus_Petrov(Petrov):
    def wrapper():
        Petrov()
        print("Year bonus salary is 8000$ ")
        print("Personal bonus achievement is 3000$ ")

    return wrapper()


@bonus_Petrov
def salary_Petrov():
    return print("Month salary is 1500$")

print(salary_Petrov())

#2 Использовать функцию map и filter

def exchange_currency(byn) :
    return byn*2.58

x = [2, 34, 10, 20000, 539]
y = list(map(exchange_currency, x))
print(y)


def odd_numbers(x):
    if x % 2 == 0 :
        return False
    else :
        return True

numbers = [1 ,2 , 3, 4, 5 ,6, 7, 8, 9, 10]
odd_result = list(filter(odd_numbers, numbers ))

print (odd_result)
print(type(odd_result))

#3 Создадим чистую и нечистую функцию.
import random

#pure function
def sum(a,b):
    return a+b
print(sum(4,6))
print(sum(4,6))
print(sum(4,6))

#not pure function
def sum_1(x):
    return x*random.randrange(1,25)
print(sum_1(1))
print(sum_1(1))
print(sum_1(1))


#4 Написать функцию, которая определяет, является ли год високосным. Пользователь
#вводит год, если он високосный, то функция возвращает True. Если нет, то False


def leap_year(year:int):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

x = int(input("Enter a year: "))
print(leap_year(x))


#5 Сделать функцию поиска минимума и максимума в списке.

def maximum(data_list):
    return max(data_list)

data_list = [2, 5, 6, 33, 78,4, 45, -3]
print(maximum(data_list))


def minimum(data_l):
    return min(data_l)

data_l = [2, 5, 6, 33, 78,4, 45, -3]
print(minimum(data_l))

#6 Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и
# возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень)

def season(month_num):
    if 6 > month_num > 2:
        return print("Spring")
    elif 9 > month_num > 5:
        return print("Summer")
    elif 12 > month_num > 8:
        return print("Autumn")
    else:
        return print("Winter")

month = int(input("Enter month number or 999 for exit: "))

while month > 12:
    if month > 12 and month != 999 :
        month = int(input("Enter month number from 1 to 12 \nor 999 for exit: "))
    # print(season(month))
    else:
        quit(month)

quit(month) if month == 999 else print(season(month))

#7  Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True,
# если такая дата есть в нашем календаре, и False иначе.*

from datetime import date
correctDate = None
try:
    newDate = date(2009,2,29)
    correctDate = True
except ValueError:
    correctDate = False
print(str(correctDate))

# Тут выводит только True, с False так и не получилось
'''from datetime import date


def valid_date(ymd):
    if ymd == ValueError:
        return False
    else:
        return True


ymd = str(date(2022, 2, 29))
print(valid_date(ymd)) '''

#8      Список [16, -17, 2, 78.7, False, False, {‘True’: True}, 555, 12, 23, 42, ‘DD’] Функция,
# принимает на вход список -выбирает из него все int и float -составить из него новый
# список, отсортированный от наименьшего значения большему'''


def just_int_float(a):
    b = list(filter(lambda x: isinstance(x, int), a))
    c = list(filter(lambda x: isinstance(x, float), a))
    d = list(filter(lambda x: isinstance(x, bool), a))
    result = list(set(b) - set(d)) + c
    z = sorted(result)
    print(z)


list_a = [16, -17, 2, 78.7, False, False, {"True": "True"}, 555, 12, 23, 42, 'DD']
just_int_float(list_a)
