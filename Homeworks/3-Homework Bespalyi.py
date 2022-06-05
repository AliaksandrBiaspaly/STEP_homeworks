# Functions

# 1.Cоздадим пустую функцию, которая ничего не возвращает
def empty_func():
    pass


print('Задание 2')


# 2.Написать функцию, которая принимает число, возвращает его значение умноженное на два.

def multyply_2(a):
    return a * 2


print(multyply_2(7))
print('Задание 3')


# 3 Напишем функцию, которая определяет параметр на чётность. Если чётное число принтим (‘yes’) в ином случае (‘no’).

def even_number(a):
    if a % 2 == 0:
        return print('Yes')
    else:
        return print('No')


print(even_number(7))
print('Задание 4')


# 4 Пишем функцию, принимающую два аргумента. После чего проверим, если первое число больше 10, принтим (‘да’). Если
# меньше(‘нет’).

def number_10(a, b):
    if a > 10:
        return print('Yes')
    else:
        return print('No')


print(number_10(11, 12))
print('Задание 5')

# Написать лямбда функцию, которая делит по модулю(%) два аргумента.,
N = lambda arg1, arg2: arg1 % arg2
print(N(20, 6))
print()

# УСЛОЖНЕННЫЕ ЗАДАЧИ ПО ЦИКЛАМ

# Вычислить факториал числа
'''n = int(input('Enter factorial number : '))
result = 1
for i in range(n):
    result *= i+1
print('Factorial ', n, ' is ', result)'''

# Ряд Фибоначчи
'''n = int(input('Enter number of Fibonachi sequence : '))
fib1 = 0
fib2 = 1
fib_sum = 0
if n == 0 :
    print('Fibonachi sequence from ', n, ' is ', 0)
else :
    for i in range (2,n+2):
        i +=1
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        print(fib1, end=' ') '''

# FizzBuzz, программа печатает числа от 1 до 100, вместо числе кратным 3 печатать Fizz, кратным 5  - Buzz, если 3 и 5 - FizzBuzz

'''for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')

    elif i % 3 == 0 :
        print ('Fizz' )

    elif i % 5 == 0 :
        print('Buzz')

    else :
        print(i)'''

# Переворот числа (interview)
'''#вариант 1
a = input('Enter number ')
b = a[:: -1]
print('Reverse number is :', b)'''

#вариант 2
'''a = input('Enter number ')
b = ''
for i in a :
    b = i + b
print(b)'''


# Найти наиб цифру введенного числа
a = input('Enter natural number ')
b = ''
for i in a :
    if i > b :
        b = i
print('Max digital is: ', b)