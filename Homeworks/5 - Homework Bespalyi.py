# Создадим функцию с простыми командами Обернём её в декоратор, который бы дополнял возможности функции.

def bonus_Petrov(Petrov):
    def wrapper():
        Petrov()
        print("Year bonus salary is 8000$ ")
        print("Personal bonus achievement is 3000$ ")

    return wrapper()


@bonus_Petrov
def salary_Petrov():
    x = str(input("Enter the surname :"))
    return print("Month salary is 1500$") if x == "Petrov" else print('nothing found')


print(salary_Petrov())

# Использовать функцию map и filter

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

# Создадим чистую и нечистую функцию.
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


#Написать функцию, которая определяет, является ли год високосным. Пользователь
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


# Сделать функцию поиска минимума и максимума в списке.

def maximum(data_list):
    return max(data_list)

data_list = [2, 5, 6, 33, 78,4, 45, -3]
print(maximum(data_list))


def minimum(data_l):
    return min(data_l)

data_l = [2, 5, 6, 33, 78,4, 45, -3]
print(minimum(data_l))

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и
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

# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True,
# если такая дата есть в нашем календаре, и False иначе.*

from datetime import date
correctDate = None
try:
    newDate = date(2009,2,29)
    correctDate = True
except ValueError:
    correctDate = False
print(str(correctDate))