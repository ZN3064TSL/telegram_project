import asyncio
import requests
from project_tools import translator_e_to_r, get_response


# Импорт необходимых библиотек

async def apod():
    '''
    Функция выполняющая асинхронный запрос ежедневной картинки
    :return:
    '''

    url = 'http://api.nasa.gov/planetary/apod'

    params = {
        'api_key': 'hE19M0YbWOLxyWWhu46Ginmp3fod4PGOBcVPLyan'
    }

    response = await get_response(url, params=params)
    if response:
        apod_info = {'apod_title': response['title'],
                     'apod_info': response['explanation'],
                     'image_url': response['hdurl']}
        return apod_info
