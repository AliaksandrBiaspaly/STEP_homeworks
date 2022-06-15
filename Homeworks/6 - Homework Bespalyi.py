def generator1():
    for number in ['apple', 'water', 'toast']:
        yield number

fruit = generator1()
print(next(fruit))
print(next(fruit))
print()

weather = iter(['rain', 'sun', 'cold', 'hurrican', 'windy'])
for i in weather:
    # print(next(weather, 'STOP'))
    print(i)
#print(next(weather))
#print(next(weather))
print()
class Calculator:
    # calculate any numbers
    first = 4
    second = 8

multiply = Calculator()
divine = Calculator()
plus = Calculator()
minus = Calculator()

multiply = Calculator.first * Calculator.second
print(multiply)


#class MyCalc:


