import asyncio
from project_tools import get_response


async def apod():
    url = 'http://api.nasa.gov/planetary/apod'

    params = {
        'api_key': 'hE19M0YbWOLxyWWhu46Ginmp3fod4PGOBcVPLyan'
    }
    response = await get_response(url, params=params)
    if response:
        apod_info = {'apod_title': response.json()['title'],
                     'apod_info': response.json()['explanation'],
                     'image_url': response.json()['hdurl']}
        print(apod_info)


asyncio.run(apod())