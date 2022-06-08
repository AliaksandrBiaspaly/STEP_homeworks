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