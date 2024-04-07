import json
import aiohttp
from translate import Translator


def get_config(file):
    with open(file, 'r') as json_file:
        config = json.load(json_file)
        return config


def joined(user_id):
    with open('joined.txt', 'a') as file:
        file.write(user_id + '\n')


async def get_response(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


def translator_e_to_r(text):
    translator = Translator(from_lang='English', to_lang='Russian')
    translated_text = translator.translate(text)
    return translated_text

def get_joined_users_id(db):
    with open(db, 'r') as file:
        users = file.read().split()
        if users:
            return users
        return None
