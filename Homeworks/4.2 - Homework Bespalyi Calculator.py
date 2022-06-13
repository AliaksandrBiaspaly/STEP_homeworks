print("Welcome to the best calc in the world you've ever seen")
print("You can always thank to the creator Aleks Bespalyi")
print()

q1 = float(input("Enter first number :"))
operation = str(input("Enter operation of calculation:\n * - multiplay \n \ - divide \n + - plus \n - - minus \n"))
q2 = float(input("Enter second number :"))

if operation == '*':
    print('Answer is ', q1, operation, q2, ' = ', q1 * q2)
if operation == '/':
    print('Answer is ', q1, operation, q2, ' = ', q/q2)
if operation == '+':
    print('Answer is ', q1, operation, q2, ' = ', q1 + q2)
if operation == '-':
    print('Answer is ', q1, operation, q2, ' = ', q1 - q2)


# Метод isdigit поможет, он возвращает True, если строка состоит только из чисел.
# Так можно сделать проверку вводимых пользователем данных:

i = ""
while i.isdigit() == False:
    i = input("Введите число: ")
    if i == "выход":
        break
    elif i.isdigit() == False:
        print("Неверное значение")
if i != "выход":
    i = int(i)
