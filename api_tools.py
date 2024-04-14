from project_tools import get_response


# Импорт необходимых библиотек

async def apod():
    '''
    Функция выполняющая асинхронный запрос ежедневной картинки или видео
    :return:
    '''

    url = 'http://api.nasa.gov/planetary/apod'

    params = {
        'api_key': 'hE19M0YbWOLxyWWhu46Ginmp3fod4PGOBcVPLyan'
    }

    response = await get_response(url, params=params)
    print(response)
    if response:
        apod_info = {'apod_title': response['title'],
                     'apod_media_type': response['media_type'],
                     'apod_info': response['explanation'],
                     'content_url': response['url']}
        return apod_info


async def epic():
    '''
    Функция выполняющая асинхронный запрос даты и
    последнего изображения Земли сделанного телескопом Кассегрена
    :return:
    '''

    url = 'http://api.nasa.gov/EPIC/api/natural/'

    params = {
        'api_key': 'hE19M0YbWOLxyWWhu46Ginmp3fod4PGOBcVPLyan'
    }

    response = await get_response(url, params=params)
    response = response[-1]
    if response:
        date = {
            'year': response['date'].split()[0].split('-')[0],
            'mouth': response['date'].split()[0].split('-')[1],
            'day': response['date'].split()[0].split('-')[2]
        }
        url = (f'https://api.nasa.gov/EPIC/archive/natural/'
               f'{date['year']}/{date['mouth']}/{date['day']}/png/{response['image']}.png?api_key={params['api_key']}')

        epic_info = []
        epic_info.append(date)
        epic_info.append(url)
        return epic_info


async def mars_rover_photo():
    '''
    Функция выполняющая асинхронный запрос даты и
    последних изображений Марса сделанного марсаходами
    :return:
    '''

    url = 'http://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2024-02-19'

    params = {
        'api_key': 'hE19M0YbWOLxyWWhu46Ginmp3fod4PGOBcVPLyan'
    }

    response = await get_response(url, params=params)
    if response:
        date = response['photos'][0]['rover']['max_date']
        url = f'http://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}'
        response = await get_response(url, params=params)
        if response:
            mars_rover_photo_info = {'photos': [i['img_src'] for i in response['photos']],
                                      'date': date}
            return mars_rover_photo_info
