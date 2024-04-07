from project_tools import get_response, translator_e_to_r


async def apod():
    url = 'http://api.nasa.gov/planetary/apod'

    params = {
        'api_key': 'hE19M0YbWOLxyWWhu46Ginmp3fod4PGOBcVPLyan'
    }
    response = await get_response(url, params=params)
    if response:
        apod_info = {'apod_title': translator_e_to_r(response['title']),
                     'apod_info': translator_e_to_r(response['explanation']),
                     'image_url': response['hdurl']}
        return apod_info
