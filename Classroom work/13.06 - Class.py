# 13.06.22 Class

# Создать класс, создать подклассы, изменить с их помощью атрибуты()
class Calculator:
    # calculate any numbers
    # переменные - это атрибуты
    first = 4
    second = 8

    def __init__(self): # Почитать!!!
        x = 9
        y = 78

    def __init__(self, x, y): # Почитать!!!
        self.x = x
        self.y = y

    def __new__(cls, *args, **kwargs): # первее init
        print(1+3)

print(Calculator(2,5))

multiply = Calculator()
plus = Calculator()


print(multiply)

multiply.first = 5
plus.second = 10

print(Calculator.first)
print(multiply.first)