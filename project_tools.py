import json
import aiohttp
import sqlite3


# Импорт необходимых библиотек


async def get_response(url, params):
    '''
    Функция нужна для произведения асинхронных запросов
    чтобы избежать длительного ожиданя получения информаци
     от бота в период большого наплыва пользователей
    :param url:
    :param params:
    :return:
    '''

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


def get_config(file):
    '''
    Функция для получения информации конфигурации бота
    :param file:
    :return:
    '''

    with open(file, 'r') as json_file:
        config = json.load(json_file)
        return config


def joined(db, chat_id, user_name):
    '''
    Функция добавления id чата с пользователем в файл
    :param chat_id:
    :return:
    '''

    con = sqlite3.connect(db)

    cur = con.cursor()

    result = cur.execute("""INSERT INTO joined_users VALUES (chat_id, user_name)""")

    con.commit()
    con.close()



def get_joined_users_id(db):
    '''
    Функция получения id всех пользвателей из базы данных
    :param db:
    :return:
    '''

    con = sqlite3.connect(db)

    cur = con.cursor()

    result = cur.execute("""SELECT * FROM joined_users""").fetchall()

    print(result)

    return result

    con.close()