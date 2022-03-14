import math
import sqlite3
import time


# Класс с методами работы с бд
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    # Добавление нового запроса в таблицу
    def addQuery(self, idUser, channelLink, forTime):
        try:
            # Время занесения в таблицу = нынешнее время в секундах
            sendTime = math.floor(time.time())

            # Время отписки = время отправки + на сколько часов
            killTime = sendTime + (forTime * 60 * 60)

            #
            # Сюда вставить код для подписки на канал
            #

            # Вставка записи в таблицу
            self.__cur.execute("INSERT INTO querys VALUES(?, ?, ?, ?)", (idUser, channelLink, sendTime, killTime))
            self.__db.commit()

        except sqlite3.Error as e:
            print("Ошибка запроса подписки (добавление в БД) " + str(e))
            return False

        return True


    # Поиск записей, время жизни которых истекло и которые требуется удалаить из таблицы
    def searchQuery(self):
        try:

            # Вытаскиваем id сессии(user_id), время отписки(for_time)
            self.__cur.execute("SELECT user_id, for_time FROM querys")

            nowTime = math.floor(time.time())

            # Проходим по всем записям из таблицы, проверяем, истекло ли время подписки
            for entry in self.__cur:
                #print(nowTime, entry[1])
                if(nowTime >= entry[1]):
                    self.DeleteQuery(entry[0])
                    #print(f"MINUS {entry[0]}")

        except sqlite3.Error as e:
            print("Ошибка запроса поиска записи " + str(e))
            return False

        return True

    # Удаление запроса из таблицы по id сессии
    def DeleteQuery(self, idUser):
        try:

            #
            # Сюда вставить код для отписки от канала
            #

            # Удаление записи из таблицы
            self.__cur.execute(f"DELETE FROM querys WHERE user_id='{idUser}'")
            self.__db.commit()

        except sqlite3.Error as e:
            print("Ошибка запроса отписки (удаление из БД) " + str(e))
            return False

        return True