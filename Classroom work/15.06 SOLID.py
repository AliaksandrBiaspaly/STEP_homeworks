from email.header import UTF-8

file = open('tekst.txt', 'r', encoding="utf8")
print(file.read(120))
file.close()

# создает новый файл, если его не существует
file = open('tekst2.txt', 'w', encoding="utf-8")
print(file.write('RUSS фвыф'))
file.close()

# то же самое, только короче
with open('tekst.txt', 'w', encoding="utf8") as file:
    print(file.read())

with open('tekst.txt', 'w', encoding="utf8") as file:
    for i in file:
        print(i)


# SOLID