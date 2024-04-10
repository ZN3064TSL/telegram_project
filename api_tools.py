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
