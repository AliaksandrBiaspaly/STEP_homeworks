'''def generator1():
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


#class MyCalc:'''

""" 1.  Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
(отвечающий за добавку к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия
 добавки, а иначе отобразится следующая фраза: «Обычная газировка».
"""


class Soda():  # create class Soda to define the type of sparkling water

    def __init__(self, add):
        """ свойства напитка"""
        self.add = add

    def show_my_drink(self):
        if self.add:
            print("Газировка и", self.add)
        else:
            print("Обычная газировка")


drink1 = Soda("Апельсин")
drink2 = Soda("Киви")
drink3 = Soda("")

print(drink2.add)

drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()

""" 2.Николай – оригинальный человек. 
Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст.
Но на этом он не успокоился. 
Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”. 
В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет,
 а если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то
 и вздумает так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество»
  или метод «приветствие», то ничего у такого хитреца не получится).
Для ограничения количества наборов свойств и методов в экземпляре применяется специальный магический
 атрибут __slots__."""
print()


class Nikola():
    __slots__ = "name", "age"

    def __init__(self, age, name = "Николай"):
        self.name = name
        self.age = age

        if self.name != "Николай":
            print(f"Я не {self.name}, а Николай")
        # else:
        #     print(self.name)



    # def show_name(self):
    #     if self.name != "Николай":
    #         print(f"Я не {self.name}, а Николай")
    #     else:
    #         print(self.name)

    def greeting(self):
        pass

person2 = Nikola(36, "Николай")
print(f"Я действительно {person2.name}")
print()
person1 = Nikola(45, "Максим")
print(f"Я действительно {person1.name}")
person1.greeting() # Метод привет не работает, ничего не происходит
person1.last_name = "Васильевич"

#person1.show_name()
#Nikola.show_name(person1)
# #Nikola.show_name(person2)

""" 3. """