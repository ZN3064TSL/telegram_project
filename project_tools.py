import json
import aiohttp
#from googletrans import Translator

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

#def translator_e_to_r(text):
#    translator = Translator()
#    translated_text = translator.translate(text, dest='ru')
#    return translated_text.text

