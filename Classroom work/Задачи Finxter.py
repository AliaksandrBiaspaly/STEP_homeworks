def f(xs):
    # print(list(x for x in xs))
    print(xs.count(2))
    return list(
        {x for x in xs if xs.count(x) > 1}
    )


xs = [1, 2, 2, 3, 4, 2, 4]
print(f(xs))
print()


# [2, 4] печатаем списком числа из исходного списка только те числа, которые согласно условию
# if xs.count(x) > 1 повторяются больше 1 раза

def f(xs):
    print(list(x for x in xs))
    # print (xs.count(2))
    return list(
        x for x in xs if xs.count(x) > 1
    )


xs = [1, 2, 2, 3, 4, 2, 4]
print(f(xs))
print()
# Убираем {}, и результат несколько иной
# [2, 2, 4, 2, 4] - то есть стандартный генератор, который перебирает и выводит списком все значения,
# которые повторяются больше 1 раза

# Аналогичное решение без функции с возможностью получить чистые числа (распаковка)
# mylist = [int(i) for i in input().split()]
# print(type(mylist[2]))
#
# result = []
# print(mylist)
# for i,item in enumerate(mylist):
#     if mylist.count(item) > 1:
#         result += [mylist[i]]
#
# print(*list(result)) # распаковываем список с помощью *
# # [2, 4, 6, 7, 2, 7, 44]
# # 2 7 2 7
# print()
# def func(x):
#     return x + 1
# f = func
# print(f(2) + func(2))

# print()
# num = list(map(int, input().split()))
#
# for x in num:
#     if int(x) % 2:
#         x += 1
#         print(sum([x]))
#     # print(sum(x))

# Печать суммы всех нечетных чисел из списка, вводимого вручную
print(sum([int(q) for q in input().split() if int(q) % 2]))


# Функция для реверса строки + уменьшение регистра
def solution(string):
    # res = [x for x in string]
    res = list(reversed(string))
    res = "".join(res)
    return res.lower()


print(solution("Привет"))

# Приведение всех элементов к 1 типу
names = ['Java', 'Python', 1]
names = [str(i) for i in names]
print()

import re
text = 'Spiderman'
matches = re.findall('...', text) # три точки - это три любые символа, делит текс на список из элементов, каждый из которых состоит из 3 символов
print(matches)
result = len(matches[2])
print(result)
print()

# Множество берет номер по списку и номер элемента, то есть 0 -0, 1 -1, 2 -, идем по диагонали
matrix = [ (0, 1, 1),
           (2, 1, -1),
           (-1, 0, 3), ]
d = [row[col] for col, row in enumerate(matrix)]
print(d)
print()

# Рекурсия
def recursive_function(x, y):
    if (x%2==0):
        return x
    else:
        y = y + 3
    return recursive_function(x-y, y)

print(recursive_function(19,3))
print()
word = "galaxy"
print(word[4:60])
print()

a = ['Mary', 'had', 'a', 'lamb']
for i in range(len(a)):
    #print(i, a[i], end='')
    print(a[i], end=' ')
print('\n-------------------------------------------------')
# Рекурсия на 2 функции
def ping(i):
    if i>0:
        return pong(i-1)
    else:
        return "0"

def pong(i):
    if i>0:
        return ping(i-1)
    else:
        return "1"

print(ping(6))