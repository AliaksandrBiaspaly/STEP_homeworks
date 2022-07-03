import sqlite3 as sql

# БД - таблица
# СУБД - управление таблицей

connector = sql.connect('cats.db')
cursor = connector.cursor()

# добавляет в БД
cursor.execute(
    """
        CREATE TABLE IF NOT EXIST cats (
        poroda TEXT,
        age INTEGER,
        color TEXT
        )
    """)

connector.commit() # применение всех изменений в БД
connector.close()


# допускается ввод через массив
'''cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]

cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
    UPDATE cars SET price = price+1000
""") '''