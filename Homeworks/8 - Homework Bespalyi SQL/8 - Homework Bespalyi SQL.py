"""1)  импортировать пакет sqlite3
Он предоставляет API, который понадобится для создания базы данных """
import sqlite3 as sql

'''2) Используйте функцию sqlite3.connect() для создания базы данных. Будет создан объект подключения.
Имя нашей базы данных - «employees.db». Сохраняем подключение к объекту подключения.
В следующий раз, когда мы запустим этот файл ****.py, он просто подключается к базе данных,
и если базы данных нет, он создаст ее. '''
connection = sql.connect('employees.db')

'''3) Создайте таблицу базы данных
Чтобы создать таблицу в базе данных, нам нужно использовать объект курсора.
Чтобы создать объект курсора, используйте метод connection.cursor().
С помощью этого объекта курсора мы теперь можем выполнять команды и запросы в базе данных.'''
cursor = connection.cursor()

''' 4) Наша первая команда - создать таблицу Employees.
    Используйте  метод cursor.execute(),  чтобы написать запрос CREATE TABLE.  
     В этом коде мы написали команду, которая создаст таблицу с ее именами столбцов и типами данных.'''

cursor.execute ("""
                CREATE TABLE IF NOT EXISTS Employees(
                employee_id INTEGER PRIMARY KEY,
                name TEXT,
                manager_id TEXT,
                job_id TEXT,
                department_id TEXT,
                salary REAL,
                start_worktime REAL) 
                 """)

''' 5) Зафиксируйте эти изменения в базе данных.
Чтобы зафиксировать изменения в базе данных, используйте метод connection.commit()'''
connection.commit()



''' 7) Добавление данных в таблицу'''

'''cursor.execute("""INSERT INTO Employees
                VALUES ('1','Ivanov','Petrova','IT_PROG','50',3000,9),
                        ('2','Sidorov','Petrova','IT_PROG','50',2000,13),
                        ('3','Novikova','Petrova','IT_PROG','50',2500,9),
                        ('4','Petrova','Noskovin','SALES','50',4000,10),
                        ('5','Polyakov','Noskovin','SALES','50',5000,9),
                        ('6','Ivanov','Petrova','IT_PROG','50',2000,10),
                        ('7','Kostin','Borsch','CEO','50',7000,10),
                        ('8','Minina','Polyakov','FINANCE','50',2500,9),
                        ('9','Bespaly','Polyakov','FINANCE','50',10000,13),
                        ('10','Ivashka','Polyakov','FINANCE','50',7000,9);
                        """ )'''
connection.commit()

# Получить список с информацией обо всех сотрудниках
cursor.execute("SELECT * FROM Employees")


# Добавляем столбец с именем, который забыли, и вносим в эту колонку данные
#cursor.execute("ALTER TABLE Employees ADD COLUMN firstname TEXT")
# cursor.execute("UPDATE Employees SET firstname = 'David' WHERE employee_id = 1")
# cursor.execute("UPDATE Employees SET firstname = 'Aleks' WHERE employee_id = 2")
# cursor.execute("UPDATE Employees SET firstname = 'Sveta' WHERE employee_id = 3")
# cursor.execute("UPDATE Employees SET firstname = 'Evgeniy' WHERE employee_id = 4")
# cursor.execute("UPDATE Employees SET firstname = 'Maksim' WHERE employee_id = 5")
# cursor.execute("UPDATE Employees SET firstname = 'Anton' WHERE employee_id = 6")
# cursor.execute("UPDATE Employees SET firstname = 'Aleksey' WHERE employee_id = 7")
# cursor.execute("UPDATE Employees SET firstname = 'Nikola' WHERE employee_id = 8")
# cursor.execute("UPDATE Employees SET firstname = 'David' WHERE employee_id = 9")
# cursor.execute("UPDATE Employees SET firstname = 'Anton' WHERE employee_id = 10")

# connection.commit()

#** Удалить лишние строки пустые
# cursor.execute("DELETE FROM Employees WHERE name IS NULL")
# connection.commit()

# 2) Получить список всех сотрудников с именем David
cursor.execute("SELECT * FROM Employees WHERE firstname = 'David'")

# 3) Список сотрудников IT_PROG
cursor.execute("SELECT * FROM Employees WHERE job_id = 'IT_PROG'")

# 4) Список сотрудников из 50 отдела и зп >4000
cursor.execute("SELECT * FROM Employees WHERE department_id = '50' AND salary>4000")

# 5) Список сотрудников у кого фамилия заканчивается на а
cursor.execute("SELECT * FROM Employees WHERE name LIKE '%a'")

# 6) В фамилии содержится 2 буквы n
cursor.execute("SELECT * FROM Employees WHERE name LIKE '%n%n%'")

# 7) Получить отчет по департаменту с мин и макс зп,








''' 6) Закрыть соединение с БД'''
#connection.close()