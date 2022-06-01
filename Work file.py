'''my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    my_list[i] += 5
    print(my_list)'''

'''m = -5
id(m)
n = 255
id(n)'''

# LOOP 23.05.2022
'''money = 10
while money > 0:
    print('We have ' + str(money) + ' BTC')
    money -= 1
while money == 0:
    print('We have no money')
    break'''

'''enter password
print ("Enter your password")
password = input()
while password != "12345":
    print("Try again, incorrect password")
    password = input()
print("Password correct, welcome to HELL")'''

'''import random

random_number = random.randint(1, 20)
print(random_number)
y = 0

while y < 5:
    print("Enter a number from 1 to 25")
    x = int(input())
    y += 1

    if y == 5:
        print("You lose.Game over")
        print("You have reached a max quantity of attempts")
        break

    if random_number != x:
        print("You lose. Try again, ")
    else:
        print(" Correct !!! Welcome to HELL !!! ")
        break'''

# 25.05.2022

'''for  i in n :
    print(i)
    x = [i+1 for i in n]

while x = 1 :'''
    

    # i - iterator

'''x = ''
while x != "1" :
    print("NO")
    x = input()'''

'''for i in range(2):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(50, 0, -2):
    print(i)


x = [i+5 for i in range(1,10)]
print(x)

for i in range(10):
    pass'''

'''from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done() '''


def hello():
    print('hello')


hello()
hello()


def xxx():
    return 'hello'
print(xxx())


'''def xxx(x):
    return 'hello', str(x)
print(xxx('username'))
print(xxx('Alex'))
print(xxx('good bye'))

def summ(num1,num2):
    return num1 + num2
print(summ(2,4))'''

'''def calc():
    print('Enter 1 number')
    x = int(input())
    print('Enter 2 number')
    y = int(input())
    return x + y
print(calc())'''

'''def calc(x, y):
    print(x+y)
print(calc())'''

# MAP
nums = [1,2,3,4,5]
def multiply(x):
    return x*10
new_nums = list(map(multiply, nums))
print (new_nums)

#FILTER '''
'''nums = [1,2,3,4,5]
def multiply(x):
    return  x>2
new_nums = list(filter(multiply, nums))
print (new_nums)

def add(x,y):
    return x+y*2

def do_twice(add,x,y):
    return add(add(x,y),add(x,y))

elem = 10
elem2 = 20

print(do_twice(add(elem, elem2)))
print(add(x,y))'''

'''v = int(input ())
print("v = 6") if v > 0 else print("v = -6")

for character in '123456789':
    print (character)

nums = []
for _ in range(0, 10):
  nums.append(int(input()))
    return sum(nums)'''

sum = 0
for i in range(10):
    sum += int(input("Enter a number: "))
print('Total sum is ', sum)



