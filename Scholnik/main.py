import sqlite3
from FDataBase import FDataBase

DATABASE = 'main.db'
dbase = None

# Соединение с БД
def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn

# Создание БД
def create_db():
    global dbase

    db = connect_db()
    with open('sq_db.sql', mode="r") as file:
        db.cursor().executescript(file.read())
    db.commit()

    dbase = FDataBase(db)


# Ввод входных данных
def input_data():
    # Формат ввода: id telegram сессии, сслыка на канал для накрутки, на сколько нужно подписать в часах
    with open("input.txt", mode="r") as file:
        for line in file:
            splitLine = line.split()
            dbase.addQuery(splitLine[0], splitLine[1], int(splitLine[2]))


# Проверка таблицы на истекшее время жизни записей и удаление таковых
def TryUnsubscribe():
    dbase.searchQuery()

if __name__ == '__main__':
    create_db() # Создание бд и подключение к ней

    input_data() # Расскоментить для ввода данных из файла input.txt

    TryUnsubscribe() # Функция, которая проходит по всей таблице и ищет записи, время жизни которых истекло