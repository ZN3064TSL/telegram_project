import json
import aiohttp
from translate import Translator


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


def translator_e_to_r(text):
    '''
    Переводчик текста с английского на русский (будет работать позже)
    :param text:
    :return:
    '''

    translator = Translator(from_lang='English', to_lang='Russian')
    translated_text = translator.translate(text)
    return translated_text


def joined(chat_id):
    '''
    Функция добавления id чата с пользователем в файл
    :param chat_id:
    :return:
    '''

    with open('joined.txt', 'a') as file:
        file.write(str(chat_id) + '\n')


def get_joined_users_id(db):
    '''
    Функция получения id всех пользвателей из файла
    :param db:
    :return:
    '''

    with open(db, 'r') as file:
        chats = file.read().split()
        if chats:
            return chats
        return None
