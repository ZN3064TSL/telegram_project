from project_tools import translator_e_to_r
import requests


def apod():
    '''
    Функция выполняющая запрос ежедневной картинки
    :return:
    '''

    url = 'http://api.nasa.gov/planetary/apod'

    params = {
        'api_key': 'hE19M0YbWOLxyWWhu46Ginmp3fod4PGOBcVPLyan'
    }

    response = requests.get(url, params=params).json()
    if response:
        apod_info = {'apod_title': response['title'],
                     'apod_info': response['explanation'],
                     'image_url': response['hdurl']}
        return apod_info
