# Записать в файл числа, которые ввел пользователь.
#  Достать их из файла и записать в массив строк.

#  Следующий массив будет содержать список чисел, которые он перевел из строк.

#   Используйте функцию map для преобразования строк в числа.

#   Реализовать обработку возможных исключений при таком преобразовании.

'''print('Введите 3 числа')
a = int(input())
c = int(input())
d = int(input())
b = [a,c,d]
x = []
y = []

for i in b:
    with open('database.txt', 'a+', encoding = "utf-8") as file:
        file.write(str(i) + '\n')


unpacking = open('database.txt', 'r')
n = [i.strip() for i in unpacking]

print(n)

num = map(lambda x: int(x), n)
print(list(num))
unpacking.close()'''

# Solving from Viktor
'''my_list = []


def inputs():
    cycle = True
    while cycle:
        a = input()
        if a != "end" and len(a) > 0:
            my_list.append(a)
        elif len(a) == 0:
            continue
        else:
            cycle = False
            write_in_file()


def write_in_file():
    with open('test.txt', "w+", encoding='utf8') as file:
        file.write(str(my_list))
    read_file()


def read_file():
    with open('test.txt', "r+", encoding='utf8') as file:
        my_str = file.read().replace("'", '')
        new_list = my_str.strip("[]").split(", ")
        try:
            T3 = list(map(int, new_list))
        except ValueError:
            print(T3)
            print(type(T3[1])) # print for checking


inputs()'''

'''import calendar
yy = 2022
mm = 6

print(calendar.month(yy, mm))'''


# Написать функцию класс калькулятор.

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def multiply(self):
        return self.x * self.y

    def division(self):
        try:
            return self.x / self.y
        except ZeroDivisionError:
            return print(f"На 0 делить нельзя")


calc = Calculator(6, 0)
calc.division()
