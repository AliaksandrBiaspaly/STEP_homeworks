# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Alex, home work below\n')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
my_name = 'Aleksandr'
favourite_band = 'Rammstein'
favourite_colour = 'turquoise'
favourite_movie = 'Severance'
print("my name is  ", my_name)
print("my favourite band is ", favourite_band)
print("my favourite colour is ", favourite_colour)
print("my favourite movie is ", favourite_movie)

y = str("helbhyyo")
x = tuple(y[-2])
print(x)
print(y[2])

Elements = [3, True, 'Витя', 2.0]  # Создание списка с разными типам данных
Elements.insert(0, 999)
print(Elements)

mylist = [mylist for mylist in 'list']
print(mylist)

a = [i * i for i in range(1, 10)]
print(a)

# for i in range(1,10):
#   a.append(i)
#  print(a)

my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    my_list[i] += 5
    print(mylist)
print(max(mylist))