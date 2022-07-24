import sqlite3 as sql

connection = sql.connect('employees.db')
if connection:
    print("Подключен к SQLite")


# cursor = connection.cursor()
# print("Переменные Python успешно вставлены в таблицу Employees")


class DataBaseWork():

    def __init__(self):
        # self.con = sql.connect('employees.db')
        self.cursor = connection.cursor()

    def create_table(self):
        self.cursor = connection.cursor()

        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Employees(
                        employee_id INTEGER PRIMARY KEY,
                        name TEXT,
                        manager_id TEXT,
                        job_id TEXT,
                        department_id TEXT,
                        salary REAL ) 
                         """)
        connection.commit()

    def insert_data(self, entities):
        self.cursor = connection.cursor()

        self.cursor.execute("""INSERT INTO Employees (employee_id, name, manager_id, job_id, department_id, salary) 
                VALUES (?, ?, ?, ?, ?, ?)""", entities)
        connection.commit()

    def update_dept(self, change_dept):
        self.cursor = connection.cursor()

        self.cursor.execute("UPDATE Employees SET department_id = 70 WHERE employee_id = 7", change_dept)

        connection.commit()

    def delete_data(self):
        self.cursor = connection.cursor()

        self.cursor.execute("DELETE FROM Employees WHERE employee_id = 8")
        connection.commit()

    def sql_close(self):
        print("Соединение разорвано")
        return connection.close()


Employee = DataBaseWork()
Employee.create_table()

entities = (12,'Putilo','Petrova','IT_PROG','70',1000)
Employee.insert_data(entities)

change_dept = ()
Employee.update_dept(change_dept)

Employee.delete_data()

Employee.sql_close()
